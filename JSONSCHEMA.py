from xml.dom.minidom import TypeInfo
from jsonschema import validate
import jsonschema
import json
import os

from nbformat import ValidationError


json_schema_file_name = "跨链业务数据模型v2.5.2.json"
json_output_file_name = "output.json"

current_location  = os.path.abspath(os.path.dirname(__file__))
json_location = os.path.join(current_location,"json")


json_schema_file = os.path.join(json_location,json_schema_file_name)
json_output_file = os.path.join(json_location,json_output_file_name)



with open(json_schema_file)  as load_f:
    json_schema = json.load(load_f)
    
with open(json_output_file)  as load_f:
    json_output = json.load(load_f)
    


validation = validate(instance=json_output,schema=json_schema)

if validation is None:
    print('ok')
