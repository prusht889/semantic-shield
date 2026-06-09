import sys
from app.core.ast_analyzer import SemanticCodeAnalyzer
from app.core.recovery_engine import ResilientASTParser
from app.core.impact_router import ImpactRouter
from app.core.gate_engine import ResilientPipelineGate



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
    ast_tree = parser.tree

    # 2. Use the Impact Router to check line changes against the tree structure
    print("⚡ Mapping code structural blast radius...")
    impact_report = ImpactRouter.identify_affected_functions(raw_code, modified_lines)

    # 3. INTERACTIVE UPGRADE: If blocked, print a visual map of the blast radius
    if impact_report.get("risk_level") == "HIGH" and not force_bypass:
        render_visual_blueprint(impact_report.get("altered_functions", []))

    # 4. Use the Gate Engine to decide if we block or pass the code change
    gate = ResilientPipelineGate(impact_report, force_override=force_bypass)
    is_clear = gate.evaluate_gate_clearance()

    if not is_clear:
        print("\n❌ Pipeline rejected. Please resolve the architectural warnings listed above.")
        return False

    print("\n🚀 Pipeline fully cleared! Your code changes are safe to deploy.")
    return True


if __name__ == "__main__":
    # Test 2 & 3 Scenario: Clean python code structure containing two independent functions
    user_code_submission = """
def process_user_login(user_id):
    print("Checking database...")
    return True

def render_homepage():
    print("Loading interface layout...")
    pass
"""
    has_bypass_flag = "--no-shield" in sys.argv
    # Simulate editing Line 3 (Inside Login) AND Line 7 (Inside Homepage) simultaneously
    changed_lines = [3, 7]

    run_semantic_shield(user_code_submission, changed_lines, force_bypass=has_bypass_flag)
