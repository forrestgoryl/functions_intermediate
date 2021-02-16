
#1.
x = [ [5, 2, 3], [10, 8, 9] ]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"}
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"]
}
z = [ {"x": 10, "y": 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30


#2.
def iterateDictionary(list_input):
    for i in range(len(list_input)):
        string = ""
        for item in list_input[i]:
            string += f"{item} - {list_input[i][item]}, "
        string = string[:-2]
        print(string)


#3.
def iterateDictionary2(key_name, list_input):
    for i in range(len(list_input)):
        for key in list_input[i]:
            if key == key_name:
                print(list_input[i][key])


#4. 
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}
def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        print("\n")
