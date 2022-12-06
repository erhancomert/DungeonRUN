
# Det här skriptet är bara "sandlådan" som jag använde innan jag la in allt i menyn. 

import json

with open('file.json') as user_file:
    file_contents = user_file.read()
    print(file_contents)
name = input(": ")
if name in file_contents:
    print("no")
else:
    a = []
    fname = "file.json"

    entry = [{
        "name": name
    }]
    with open(fname) as feedsjson:
        feeds = json.load(feedsjson)

    feeds.append(entry)
    with open(fname, mode='w') as f:
        f.write(json.dumps(feeds))