import json

def char_load():
  database = "file.json"
  data = json.loads(open(database).read())

  print("Characters:")
  print(data)
  char_opt = input("Choose character: ")

  for item in data:
      if item["name"] == char_opt:
        name = item['name']
        appearence = item['apperance'] 
        roll = item['roll']
        print('You are ' + name + ', the ' + appearence + ' ' + roll + '.')

char_load()

  #with open('file.json', 'r') as f:
  #  reader = json.load(f)
  #print(reader)

  #for data in reader:
  #    print(data['name'],',',data['apperance'],',', data['roll'])

  #if pick == reader:
  #    name = data['name']
  #    apperance = data['apperance']
  #    roll = data['roll']


  #print(name, apperance, roll)
  #print(reader[0]['name'])