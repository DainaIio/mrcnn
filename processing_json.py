import json
import re
import os
import datetime

files = []
for filename in os.listdir('./'):
    if os.path.isfile(os.path.join('./', filename)):
        files.append(filename)
jsonfiles = []
regex = re.compile(r'(.json)$')
for file in files:
    if regex.search(file):
        jsonfiles.append(file)

now = datetime.datetime.now()
new_dir_name = "processed_json_" + now.strftime("%m%d%H%M")
os.mkdir(new_dir_name)

for json_name in jsonfiles:
    fr = open(json_name, 'r')
    json_dict = json.load(fr)
    fr.close()
    new_dict = {}
    new_dict["imageWidth"] = json_dict["imageWidth"]
    new_dict["imageHeight"] = json_dict["imageHeight"]
    new_dict["shapes"] = json_dict["shapes"]
    new_dict["imagePath"] = json_dict["imagePath"]
    new_name = new_dir_name + "/" + json_name
    fw = open(new_name, "w")
    json.dump(new_dict, fw, indent=4)
    fw.close()
