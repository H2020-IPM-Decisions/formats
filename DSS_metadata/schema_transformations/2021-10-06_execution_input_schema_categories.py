#!/usr/bin/python3

# 2021-10-06
# Changes the execution property:
# Introduces the input_schema_categories property,
# which is looks e.g. like this:
# "input_schema_categories": {
#   "hidden": ["modelId"],
#	"system": [],
#	"user_init": ["configParameters.dateGs31","configParameters.date3rdUpperLeafEmerging"],
#	"triggered": [],
#	"internal": ["configParameters.thresholdRelativeHumidity","configParameters.thresholdLeafWetness"] 
# }
# 
# The current input_schema_hidden_properties is moved to the "hidden"property
# Usage: ./2021-10-06_execution_input_schema_categories.py [YAMLfilename]
# Returns the new YAML to stdout
# Requires the ruamel.yaml module: https://yaml.readthedocs.io/en/latest/basicuse.html
# Tor-Einar Skog, NIBIO

import sys
from ruamel.yaml import YAML


if len(sys.argv) == 1:
    print("Usage: ./2021-10-06_execution_input_schema_categories.py [YAMLfilename]")
    exit(0)

yaml_filename = sys.argv[1]
#print(sys.argv[1])
yaml = YAML() 
try:
    with open(yaml_filename,'r') as f:
        yaml_data = yaml.load(f)
        for model in yaml_data["models"]:
            execution = model["execution"]
            old_hidden = execution.get("input_schema_hidden_properties",None)
            input_schema_categories = {
                "hidden": old_hidden
            }
            if execution.get("input_schema_hidden_properties", None) is not None:
                del(execution["input_schema_hidden_properties"])
            execution["input_schema_categories"] = input_schema_categories

            #print(new_description)
        yaml.dump(yaml_data,sys.stdout)
        
except FileNotFoundError:
    print("File %s was not found. Exiting." % yaml_filename)

#f.close()