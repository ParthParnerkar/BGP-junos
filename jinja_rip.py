import jinja2


interfaces = ['GigabitEthernet0/0', 'GigabitEthernet0/1', 'GigabitEthernet0/2']
ip = ['192.168.10.1', '192.168.10.2', '192.168.10.3']
variables = {
    'protocol': 'rip',
    'network1': '192.168.10.0',
    'network2': '192.168.20.0'
    'interfaces': interfaces,
    'ip': ip
}
file_name = 'config.j2'
with open(file_name) as f:
    rip_template = f.read()

tmp = jinja2.Template(rip_template)
print(tmp.render(variables))
