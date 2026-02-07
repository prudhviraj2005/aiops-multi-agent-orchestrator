class QueryLogsTool:
    def run(self, provider: str, log_filter: str, time_range: str):
        return {
            "provider": provider,
            "filter": log_filter,
            "errors": [
                "TimeoutException",
                "DatabaseSlowQuery"
            ],
            "error_count": 14
        }
