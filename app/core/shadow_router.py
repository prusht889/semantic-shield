import json


class BlastRadiusIsolator:
    def __init__(self, impact_report: dict):
        self.report = impact_report

    def generate_containment_strategy(self) -> str:
        """
        Generates an automated Feature-Flag and Canary infrastructure blueprint
        to safely deploy high-risk code changes behind a digital shield.
        """
        altered_funcs = self.report.get("altered_functions", [])

        containment_blueprint = {
            "status": "CONTAINMENT_SHIELD_ACTIVE",
            "feature_flag_gate": {
                "flag_id": f"ff_shield_{'_'.join(altered_funcs)}",
                "default_state": "DISABLED",
                "rollout_percentage": {
                    "internal_developers": 100,
                    "public_users": 0  # Complete isolation from public production traffic
                }
            },
            "canary_telemetry": {
                "monitored_impact_nodes": altered_funcs,
                "error_threshold_trigger": "2.0%",
                "action_on_failure": "AUTOMATED_IMMEDIATE_ROLLBACK"
            }
        }
        return json.dumps(containment_blueprint, indent=2)
