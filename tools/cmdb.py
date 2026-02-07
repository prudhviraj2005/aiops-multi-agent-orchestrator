class CMDBLookupTool:
    def run(self, service_id: str):
        return {
            "service_id": service_id,
            "owner": "Payments Team",
            "dependencies": ["auth-service", "db-primary"],
            "runbook_id": "RB-CHK-001",
            "change_window": "02:00-04:00 UTC"
        }
