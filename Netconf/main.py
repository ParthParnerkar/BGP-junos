from ncclient import manager
from pprint import pprint
import xml.dom.minidom

# To connect to the device, a router needs to be specified.
router = {
   'host': '10.10.20.48',
   'port': '830',
   'username': 'developer',
   'password': 'C1sco12345'
}
conn = manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False, device_params={'name':'iosxe'})

template = open('template.xml').read()

# To get capabilities
for capability in conn.server_capabilities:
    print('*' * 50)
    print(capability)

edit_info = template.format(interface_name='GigabitEthernet2', interface_desc="Parth edited this")

# To get running config, first specify a router
running_config = conn.edit_config(edit_info, target='running').xml
print(xml.dom.minidom.parseString(running_config).toprettyxml())
