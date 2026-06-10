import sys
from app.core.recovery_engine import ResilientASTParser
from app.core.ast_analyzer import SemanticCodeAnalyzer
from app.core.impact_router import ImpactRouter
from app.core.gate_engine import ResilientPipelineGate
from app.core.shadow_router import BlastRadiusIsolator


def render_complete_system_blueprint(full_blueprint: dict):
    """Generates a comprehensive visual map of ALL discovered functional nodes in the target codebase."""
    print("\n🗺️  [GLOBAL CORE BLUEPRINT: TOTAL MODULE SCHEMA]")
    print("======================================================================")
    print("  [Target Codebase Directory Module]")
    print("                │")

    functions = full_blueprint.get("functions", {})
    if not functions:
        print("                └───► (No operational function nodes compiled in this context)")
    else:
        # Step through every discovered system function node to draw the complete map
        for idx, (func_name, meta) in enumerate(functions.items()):
            is_last = (idx == len(functions) - 1)
            connector = "└───" if is_last else "├───"
            print(f"                {connector}► 📦 Node: {func_name}() [Line {meta['line_number']}]")

    print("======================================================================")


def render_visual_blueprint(altered_functions: list):
    """Generates a clean ASCII visual diagram of the architectural blast radius."""
    print("\n📊 [SEMANTIC BLAST RADIUS VISUALIZATION]")
    print("====================================================")
    print("  [Your Code Commit]")
    print("          │")
    print("          ▼")

    for func in altered_functions:
        print(f"  🔥 Modified Node: {func}()")
        print("          │")
        print("          ├──► 🛑 Risk: DOWNSTREAM DEPENDENCY BREACH")
        print("          └──► 🛑 Location: app/core/auth_pipeline")

    print("====================================================")


def run_semantic_shield(raw_code: str, modified_lines: list[int], force_bypass: bool = False):
    """Orchestrates all individual files into a single running pipeline application."""
    print("🛡️ [SemanticShield] Initiating codebase pipeline analysis...")

    # 1. Use the Recovery Engine to compile the code tree safely
    parser = ResilientASTParser(raw_code)
    ast_tree = parser.safe_parse()

    # 2. Extract and display the global code map layout architecture
    analyzer = SemanticCodeAnalyzer(raw_code)
    full_blueprint = analyzer.extract_functional_blueprint()
    render_complete_system_blueprint(full_blueprint)

    # 3. Use the Impact Router to check line changes against the tree structure
    print("⚡ Mapping code structural blast radius...")
    impact_report = ImpactRouter.identify_affected_functions(raw_code, modified_lines)

    # 4. If blocked, print a visual map of the blast radius
    if impact_report.get("risk_level") == "HIGH" and not force_bypass:
        render_visual_blueprint(impact_report.get("altered_functions", []))

    # 5. Deadlock Override Mitigation Hook
    if force_bypass and impact_report.get("risk_level") == "HIGH":
        print("\n🛡️ [CONTAINMENT SHIELD ENGINE GENERATION]")
        print("⚠️ Emergency override bypassed security gates. Compiling isolation schemas...")
        isolator = BlastRadiusIsolator(impact_report)
        print(isolator.generate_containment_strategy())

    # 6. Use the Gate Engine to decide if we block or pass the code change
    gate = ResilientPipelineGate(impact_report, force_override=force_bypass)
    is_clear = gate.evaluate_gate_clearance()

    if not is_clear:
        print("\n❌ Pipeline rejected. Please resolve the architectural warnings listed above.")
        return False

    print("\n🚀 Pipeline fully cleared! Your code changes are safe to deploy.")
    return True


if __name__ == "__main__":
    # PRODUCTION MULTI-FILE SCENARIO: A developer edits the base 'auth_service.py' file!
    target_file_path = "auth_service.py"
    has_bypass_flag = "--no-shield" in sys.argv

    print(f"📖 Reading physical file target from disk: '{target_file_path}'")
    with open(target_file_path, "r") as f:
        real_file_contents = f.read()

    # Simulate editing Line 2 (right inside the critical 'validate_vault_token' signature)
    simulated_changed_lines = [2]

    # Execute the master scanner engine against the real production file stream
    run_semantic_shield(real_file_contents, simulated_changed_lines, force_bypass=has_bypass_flag)
