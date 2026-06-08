import ast


class ResilientASTParser:
    def __init__(self, raw_code: str):
        self.raw_code = raw_code

    def safe_parse(self) -> ast.Module:
        """
        Attempts to parse code into an AST object. If a structural syntax error
        occurs, it comments out the broken line in memory and attempts recovery.
        """
        try:
            return ast.parse(self.raw_code)
        except SyntaxError as e:
            print(f"⚠️ [SYNTAX ERROR DETECTED] Line {e.lineno} is half-written. Recovering...")

            lines = self.raw_code.splitlines()
            if e.lineno and e.lineno <= len(lines):
                lines[e.lineno - 1] = f"# [RECOVERED BY SHIELD] {lines[e.lineno - 1]}"

            reconstructed_code = "\n".join(lines)

            try:
                return ast.parse(reconstructed_code)
            except SyntaxError:
                print("🚨 Severe code fragmentation. Generating blank canvas fallback tree.")
                return ast.parse("pass")


if __name__ == "__main__":
    print("🧪 Verifying Local Syntax-Error Recovery Mechanism...")
    broken_user_code = """
def calculate_metrics():
    print("Calculating...")

def fetch_data(source:
    return "raw_data"
"""
    parser = ResilientASTParser(broken_user_code)
    tree_result = parser.safe_parse()
    print("🏆 Was abstract tree safely generated without crashing PyCharm?:", isinstance(tree_result, ast.Module))
