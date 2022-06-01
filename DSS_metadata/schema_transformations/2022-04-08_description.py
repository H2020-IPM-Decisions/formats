#!/usr/bin/python3

# 2022-04-08
# Changes the description property from an object with 5 string type properties: 
# created_by, age, assumptions, peer_review and other
# TO => string
# ALSO adds the "Purpose" property - a short description
# The current description string is moved to the "other" property
# Usage: ./2022-04-08_description.py [YAMLfilename]
# Returns the new YAML to stdout
# Requires the ruamel.yaml module: https://yaml.readthedocs.io/en/latest/basicuse.html
# Tor-Einar Skog, NIBIO

import sys
from ruamel.yaml import YAML


if len(sys.argv) == 1:
    print("Usage: ./2022-04-08_description.py [YAMLfilename]")
    exit(0)

yaml_filename = sys.argv[1]
#print(sys.argv[1])
yaml = YAML() 
try:
    with open(yaml_filename,'r') as f:
        yaml_data = yaml.load(f)
        for model in yaml_data["models"]:
            old_description = model["description"]
            new_description = "%s\nSOURCE: %s\nASSUMPTIONS: %s\nREFERENCE: %s" % (
                old_description["other"],
                old_description["created_by"],
                old_description["assumptions"],
                old_description["peer_review"],
            )
            model["description"] = new_description
            model["purpose"] = ""
            #print(new_description)
        yaml.dump(yaml_data,sys.stdout)
        
except FileNotFoundError:
    print("File %s was not found. Exiting." % yaml_filename)

#f.close()