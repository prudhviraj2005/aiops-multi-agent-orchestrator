class QueryMetricsTool:
    def run(self, provider: str, query: str, time_range: str):
        return {
            "provider": provider,
            "query": query,
            "time_range": time_range,
            "cpu_avg": 92,
            "memory_avg": 78,
            "disk_io": 85,
            "status": "OK"
        }
