import json


with open("data.json") as f:
	d = json.load(f)

c = ""

for city in d:
	city = city["name"]
	c = c + f"<li>{city}</li>" + "\n"

c = "<ul>" + c + "</ul>"
with open("cities.txt", "w") as f:
	f.write(c)