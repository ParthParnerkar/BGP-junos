from jnpr.junos import Device
from lxml import etree
from jnpr.junos.utils import config



def bgp_connection():
    """
    This script is a basic script to configure BGP on a Juniper Device. BG
    """
    global dev
    dev = Device(host='',user='',passwd='', normalize=True)
    dev.open(gather_facts=True)
    cnf = "" #Enter your bgp configuration here. Should be a XML RPC
    dev.rpc.load_config(cnf) # This can be used to load the XML configuration of BGP on your junos device

def get_info_if_present(bgp_connection):
    if bgp_connection():
        rpc = dev.rpc.get_bgp_summary_information()
        rpc_xml = etree.tostring(rpc, pretty_print=True, encoding='unicode')





