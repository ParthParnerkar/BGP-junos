from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get
import json # optional.. can use for a better json o/p


nr = InitNornir(config_file="config.yaml", dry_run=True)

print(nr.inventory.hosts)

results = nr.run(task=napalm_get, getters=["facts", "interfaces"])


info = nr.inventory.hosts['host1.cmh']
print(info['domain'])



print_result(results)
