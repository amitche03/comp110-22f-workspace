"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key/
schools.pop("Duke")

# Test for the existence of a key
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else: 
    print("No key 'Duke' in schools")

# Update/ Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200


# Demonstration of dictionary literals

# Empty dictionary literal
schools = {} #same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

points: dict[str, int] = {"Kris": 0, "Kaki": 10}
points["Kaki"] += 100
print(points["Kaki"] == 110)