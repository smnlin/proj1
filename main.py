import json

person = {"name": "John", "age": 30, "hasChildren": True, "titles": ["engineer", "programmer"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

with open("person.json", "w") as jsFile:
    json.dump(person, jsFile, indent=4)

newPerson = json.loads(personJSON)
print(newPerson)