
# JSON is syntax for storing and exchangeing the data
# JSON is a text,written with Javascript object Notation
# JSON need built-in package called JSON
import json
# Read json data
x = '{"id": 10, "name": "Amit", "city": "Sangli"}'

y = json.loads(x)
print(y['name'])

# Native datatype dictionary convert into JSON
z = {"id": 10, "name": "Amit Patil", "city": [
    "Sangli", "Pune"], "Percentage": 66.00, "status": True}

w = json.dumps(z)
print(w)
