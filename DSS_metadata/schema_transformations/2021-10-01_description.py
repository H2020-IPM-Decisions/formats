#!/usr/bin/python3

# 2021-10-01
# Changes the description property from a string to an object with 5 string type properties: 
# created_by, age, assumptions, peer_review and other
# The current description string is moved to the "other" property
# Usage: ./2021-10-01_description.py [YAMLfilename]
# Returns the new YAML to stdout
# Requires the ruamel.yaml module: https://yaml.readthedocs.io/en/latest/basicuse.html
# Tor-Einar Skog, NIBIO

import sys
from ruamel.yaml import YAML


if len(sys.argv) == 1:
    print("Usage: ./2021-10-01_description.py [YAMLfilename]")
    exit(0)

yaml_filename = sys.argv[1]
#print(sys.argv[1])
yaml = YAML() 
try:
    with open(yaml_filename,'r') as f:
        yaml_data = yaml.load(f)
        for model in yaml_data["models"]:
            old_description = model["description"]
            old_citation = model.get("citation",None)
            new_description = {
                "other":old_description,
                "created_by":"",
                "age":"",
                "assumptions":"",
                "peer_review": old_citation if old_citation is not None else ""
            }
            model["citation"] = None
            model["description"] = new_description

            #print(new_description)
        yaml.dump(yaml_data,sys.stdout)
        
except FileNotFoundError:
    print("File %s was not found. Exiting." % yaml_filename)

#f.close()