import json

# A Python dictionary
data = {
  "name": "John Doe",
  "age": 30,
  "isStudent": True,
  "courses": ["History", "Math"]
}

# Convert the dictionary to a JSON string
json_string = json.dumps(data)

# Print the JSON string
print(json_string)


json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Use json.loads() to parse the string into a Python dictionary
python_dict = json.loads(json_string)
print(python_dict)