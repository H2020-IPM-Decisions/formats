#!/usr/bin/python3

# 2021-12-10
# Changes the output.warning_status_interpretation property from
# as string to an array like this:
# [
#    {
#        "explanation": "The flight period of the 1st generation is over",
#        "recommended_action": "Consult your advisory service"
#    },
#    {
#        "explanation": "",
#        "recommended_action": ""
#    },
#    {
#        "explanation": "The flight period has not yet begun",
#        "recommended_action": "Consult your advisory service"
#    },
#    {
#        "explanation": "The flight period is beginning, flies can be coming into the field",
#        "recommended_action": "Consult your advisory service"
#    },
#    {
#        "explanation":"Peak flight period",
#        "recommended_action":"Consult your advisory service"
#    }
#]
# It does so by copying the current string into all the explanation items


import sys
from ruamel.yaml import YAML


if len(sys.argv) == 1:
    print("Usage: ./2021-12-10_warning_status_interpretation.py [YAMLfilename]")
    exit(0)

yaml_filename = sys.argv[1]
#print(sys.argv[1])
yaml = YAML() 
try:
    with open(yaml_filename,'r') as f:
        yaml_data = yaml.load(f)
        for model in yaml_data["models"]:
            if model.get("output",None) is None:
                continue
            wsi = model["output"]["warning_status_interpretation"]
            rec_item = {
                "explanation": wsi,
                "recommended_action": ""
            }
            
            model["output"]["warning_status_interpretation"] = []
            for i in range(0,5):
                model["output"]["warning_status_interpretation"].append(dict(rec_item))
        
        yaml.dump(yaml_data,sys.stdout)

except FileNotFoundError:
    print("File %s was not found. Exiting." % yaml_filename)