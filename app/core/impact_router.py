import ast


class ImpactRouter:
    @staticmethod
    def identify_affected_functions(raw_code: str, modified_lines: list[int]) -> dict:
        """
        Safely scans for functions. If a code syntax error prevents full AST compilation,
        it automatically falls back to an explicit text token analyzer loop to prevent crashes.
        """
        report = {
            "altered_functions": [],
            "risk_level": "LOW"
        }

        functions_map = {}

        try:
            # First Attempt: Try parsing the standard syntax structure tree
            tree = ast.parse(raw_code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    functions_map[node.name] = node.lineno
        except SyntaxError:
            print("🛡️ [RECOVERY] Syntax anomaly caught inside router. Activating text-boundary scanning...")
            # Fallback Option: Parse function declarations safely as plain text strings
            lines = raw_code.splitlines()
            for idx, line in enumerate(lines):
                clean_line = line.strip()
                if clean_line.startswith("def ") and "(" in clean_line:
                    try:
                        # Extract the word between 'def ' and '(' cleanly
                        func_name = clean_line.split("def ")[1].split("(")[0].strip()
                        functions_map[func_name] = idx + 1
                    except Exception:
                        pass

        # Match modified lines against our mapped function locations
        for func_name, start_line in functions_map.items():
            for mod_line in modified_lines:
                # If a line modification falls within a 15 line window of the function start
                if start_line <= mod_line <= (start_line + 15):
                    if func_name not in report["altered_functions"]:
                        report["altered_functions"].append(func_name)

        if len(report["altered_functions"]) > 0:
            report["risk_level"] = "HIGH"

        return report
