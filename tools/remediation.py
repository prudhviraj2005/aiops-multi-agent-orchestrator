class ChangeMgmtTool:
    def create_change(self, remediation_plan: dict):
        return {
            "change_id": "CHG-2026-001",
            "status": "CREATED"
        }

    def approve_change(self, change_id: str):
        return {
            "change_id": change_id,
            "approved": True
        }
