from app.core.ast_analyzer import SemanticCodeAnalyzer


class ImpactRouter:
    @staticmethod
    def identify_affected_functions(source_code: str, modified_lines: list[int]) -> dict:
        """Matches modified line modifications against the AST function coordinates."""
        analyzer = SemanticCodeAnalyzer(source_code)
        blueprint = analyzer.extract_functional_blueprint()

        report = {
            "altered_functions": [],
            "risk_level": "LOW"
        }

        # Scan each function discovered in the AST file tree
        for func_name, meta in blueprint["functions"].items():
            func_start_line = meta["line_number"]

            # Simple boundary rule: if change happens within 10 lines of the function start
            for mod_line in modified_lines:
                if func_start_line <= mod_line <= (func_start_line + 10):
                    if func_name not in report["altered_functions"]:
                        report["altered_functions"].append(func_name)

        if len(report["altered_functions"]) > 0:
            report["risk_level"] = "HIGH"

        return report


if __name__ == "__main__":
    print("🧪 Verifying local impact checking module...")
    sample_script = """
def core_billing_engine():
    pass

def minor_frontend_label():
    pass
"""
    # Simulate a developer modifying line 3 (inside core_billing_engine)
    simulated_changes = [3]
    print("🚨 Impact Analysis:", ImpactRouter.identify_affected_functions(sample_script, simulated_changes))
