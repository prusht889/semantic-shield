import datetime


class ResilientPipelineGate:
    def __init__(self, impact_report: dict, force_override: bool = False):
        self.report = impact_report
        self.force_override = force_override
        self.audit_log_path = "security_audit.log"

    def evaluate_gate_clearance(self) -> bool:
        """
        Determines if the code change can proceed.
        Implements an emergency escape valve to prevent blocking developers indefinitely.
        """
        risk = self.report.get("risk_level", "LOW")

        # 1. EMERGENCY ESCAPE VALVE: Bypass the block if the force flag is active
        if self.force_override:
            print("⚠️ [EMERGENCY OVERRIDE ACTIVATED] Developer bypassed the security gate.")
            self._log_bypass_incident("DEVELOPER_FORCED_BYPASS")
            return True  # Allow the code to pass through the gate immediately

        # 2. STANDARD BLOCK LOGIC: Stop high-risk code changes
        if risk == "HIGH":
            print("\n❌ [GATE BLOCKED] Your changes have an unverified architectural blast radius!")
            print(f"Altered functions detected: {self.report.get('altered_functions')}")
            print("\n💡 HOW TO MOVE FORWARD TO UNSTUCK YOURSELF:")
            print("👉 Fix the functions to maintain backwards compatibility.")
            print("👉 Run your command with the '--no-shield' flag if this is an urgent hotfix.")
            return False  # Stop the pipeline execution

        # 3. SAFE PASSAGE: Allow low-risk changes
        print("✅ [GATE PASSED] Low structural risk detected. Moving forward smoothly.")
        return True

    def _log_bypass_incident(self, reason: str):
        """Creates a local audit trail for security accountability when a bypass occurs."""
        timestamp = datetime.datetime.utcnow().isoformat()
        log_entry = (
            f"[{timestamp}] BYPASS TRIGGERED | Reason: {reason} | "
            f"Impacted Areas: {self.report.get('altered_functions')}\n"
        )
        with open(self.audit_log_path, "a") as f:
            f.write(log_entry)


if __name__ == "__main__":
    print("🧪 Verifying Pipeline Safety Gate Engine...")

    # Simulate a dangerous change scenario that could cause a deadlock
    dangerous_report = {
        "altered_functions": ["process_credit_card_payment"],
        "risk_level": "HIGH"
    }

    print("\n--- Scenario A: Normal Execution (Blocked) ---")
    gate_a = ResilientPipelineGate(dangerous_report, force_override=False)
    gate_a.evaluate_gate_clearance()

    print("\n--- Scenario B: Emergency Override Used (Passed) ---")
    gate_b = ResilientPipelineGate(dangerous_report, force_override=True)
    success = gate_b.evaluate_gate_clearance()
    print("🚀 Did the pipeline successfully proceed?:", success)
