# Mines required data from and creates usable training examples

# import sklearn as skl
from xml.etree import ElementTree as ET
import sys
import os
import subprocess

# Parse bug description and fetch BUG data
def get_bug_data(bug_id):
    """
    Obtain Bug data from Bug.get api at
    https://github.com/bwiedemann/obsbugzilla
    And then use XML RPC APIs to obtain relevant data
    Possible return in JSON serialized format
    """
    pass

# Parse SR and fetch SR data
def get_sr_data(sr_number):
    """
    Use osc commands to get values for the SR Number.
    osc api request/<SR_number> 
    And then use XML ElementTree APIs to obtain the Relevant data
    Possibly formatted in JSON serialized format
    """
    pkg_update = {'request': sr_number,
                  'sources': None,
                  'targets': None}
    p = subprocess.Popen(['osc', 'api', 'request/%d' % sr_number],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    output, error = p.communicate()

    doc = ET.fromstring(output)
    action = doc.find("action")
    if action.attrib['type'] == "submit":
        sources = list(doc.iter("source"))
        src_info = []
        if sources:
            for source in sources:
                src_info.append({'package': source.attrib['package'],
                                 'project': source.attrib['project']})


        targets = list(doc.iter("target"))
        tgt_info = []
        if targets:
            for target in targets:
                tgt_info.append({'package': target.attrib['package'],
                                 'project': target.attrib['project']})

        pkg_update['sources'] = src_info
        pkg_update['targets'] = tgt_info
    return pkg_update

def gen_data(input_file):
    """
    Using input_file containing list of Submit Request numbers
    against each resolved bug, this function uses get_bug_data()
    and get_sr_data() functions defined above to generate 
    comprehensive data mapping several details from the bug 
    description and comments and corresponding packages where
    the issues were resolved and SRs provided.
    """
    data_json = {}
    

if __name__=="__main__":
    sr_number = int(sys.argv[1])
    print ("Fetching data for Submit Request: " + str(sr_number))
    pkg_info = get_sr_data(sr_number)
    print ("Package Details: " + str(pkg_info))
