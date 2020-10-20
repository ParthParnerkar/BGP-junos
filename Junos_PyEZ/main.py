from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from lxml import etree
import yaml
import xmltodict
import getpass

__author__ = "Parth Parnerkar"

INVENTORY_FILE = 'inventory.yml'
VARIABLES_FILE = 'vars.yml'

device_parameters = {
    "user": "Parth",
    "passwd": getpass.getpass()
}

def config(connection_params, variables):
    dev = Device(**connection_params)
    dev.open()
    dev.facts_refresh()
    facts = dev.facts

    hostname = facts['hostname']

    config_variable = variables['devices'][hostname]

    conf = Config(dev, mode='private')
    conf.load(template_path='templates/interface_config.conf', template_vars=config_variable  )
    conf.pdiff()
    conf.commit()
    dev.close()


def getting_facts(params):
    global dev
    dev = Device(**params)
    dev.open()
    dev.facts_refresh()
    facts = dev.facts
    dev.close()
    return facts

def get_config():
    config = dev.rpc.get_config()
    pprint(etree.tostring(config, encoding='unicode')) #This will return the complete candidate configuration in XML format

    # If you dont like the XML output and would like to view it as JSON, then we can use the command below, any one would suffice.
    # pprint(xmltodict.parse(etree.tostring(dev.rpc.get_config())))

    # To get a specfic part of the config use the command below, For the purpose of this training, I will filter interfaces from the whole of candidate configuration
    filter = '<interfaces><interface><name/></interface></interfaces>'
    filtered_config = dev.rpc.get_config(filter_xml=filter,options={'inherit':'inherit'})
    pprint(etree.tostring(filtered_config,encoding='unicode'))
    get_routes()

def get_routes():
    routes = dev.display_xml_rpc('show route', format='text')
    routes_python = xmltodict.parse(xml_input=routes)
    return routes_python

def read_yaml_inventory(file=INVENTORY_FILE):
    with open(file) as f:
        result = yaml.load(f)
    return result

def read_output():
    return read_yaml_inventory()['juniper-mx']


def main():
    variables = read_yaml_inventory('vars.yml')
    jun_ip_list = read_output()
    for ip in jun_ip_list:
        params = device_parameters.copy()
        params['host'] = ip
        config(params, variables)
        facts = getting_facts(params)
        pprint(facts) # THIS WILL PRINT OUT THE DEVICE FACT
    print(variables)
    pass


if __name__ == '__main__':
    main()





