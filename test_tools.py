from tools.metrics import QueryMetricsTool
from tools.cmdb import CMDBLookupTool

metrics = QueryMetricsTool().run("AWS", "cpu_usage", "5m")
cmdb = CMDBLookupTool().run("checkout-service")

print(metrics)
print(cmdb)
