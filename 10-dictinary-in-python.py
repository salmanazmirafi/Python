# # # --------------Chapter -10 Dictionary in python------------------

"""dictionary_name ={
    key:value,
    key:value
}"""

# person = {
#     "first_name": "Jhon",
#     "last_name": "De",
#     "age": 20,
# }

# # creating Dictionary

# person = {
#     "first_name": "Jon",
#     "last_name": "De",
#     "age": 20,
# }
# print(person["first_name"])
# print(person["last_name"])
# print(person["age"])

# get method
# print(person.get("first_name"))

# # adding item
# person["hobbies"] = "Programming"
# print(person)

# # changing new items
# person["first_name"] = "Salman Azmi Rafi"
#
# print(person)

# # remove on item's value
# person.pop("age")
# print(person)

# # nested dictionary
employee_data = {
    "Manager": {
        "Name": "Salman",
        "age": 40,
        "Id": "93fi3083029"
    },
    "Programmer": {
        "Name": "Rafi",
        "age": 30,
        "Id": "203894938"
    },
    "salary": {
        "Manager": 45000,
        "Programmer": 34000,
    },
}

print("Manager Name : ", employee_data["Manager"]["Name"], "Manager Id : ", employee_data["Manager"]["Id"], "Manager "
                                                                                                            "Salary :"
                                                                                                            " ",
      employee_data["salary"]["Manager"])
