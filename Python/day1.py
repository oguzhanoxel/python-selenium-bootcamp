# print("Hi I am Elfo")

# title = "Hi I am Title"

# print(title)

# numeric = 3
# string_value = "3"

# if numeric != string_value:
# 	print(f"numeric({numeric}) not equal string_value({string_value})")
# else:
# 	print(f"numeric({numeric}) equal string_value({string_value})")

# HM1

# Numeric Data Types
print("\n---Numeric Data Type---")
numeric_integer = 3
print(f"value: {numeric_integer}, type: {type(numeric_integer)}")

numeric_float = 3.33
print(f"value: {numeric_float}, type: {type(numeric_float)}")

numeric_complex = 10+3j
print(f"value: {numeric_complex}, type: {type(numeric_complex)}")

# String Data Type
print("\n---String Data Type---")
str = "HiIamElfo"

print (str)
print (str[3]) # a
print (str[3:7]) # amEl
print (str[3:]) # amElfo
print (str * 3) # HiIamElfoHiIamElfoHiIamElfo
print (str + " <---- Concreted String")

# List Data Type
print("\n---List Data Type---")

a_list = [13.3, "vitae", 333, "faucibus"]

a_tiny_list = [3, 13, 333]

print (a_list)            # [13.3, "vitae", 333, "faucibus"]
print (a_list[3])         # faucibus
print (a_list[1:3])       # ['vitae', 333]
print (a_list[2:])        # [333, 'faucibus']
print (a_tiny_list * 3)    # [3, 13, 333, 3, 13, 333, 3, 13, 333]
print (a_list + a_tiny_list) # [13.3, 'vitae', 333, 'faucibus', 3, 13, 333]

# Tuple Data Type : Tuples can be thought of as read-only lists
print("\n---Tuple Data Type---")

a_tuple = (13.3, "vitae", 333, "faucibus")
a_tiny_tuple = (3, 13, 333)

# a_tuple[0] = "new string" TypeError: 'tuple' object does not support item assignment
a_list[0] = "new string" 

print ((a_tuple))            # [13.3, "vitae", 333, "faucibus"]
print (a_tiny_tuple)            # [13.3, "vitae", 333, "faucibus"]


# Dictionary
print("\n---Dictionary Data Type---")

user = {
	'username': 'oguzhanoxel',
	'email': 'oguzhanoksel@hotmail.com',
	'password': '123456',
}

print(user)
print(user['username'])
print(user.keys())
print(user.values())

# Boolean
print("\n---Boolean Data Type---")

a = True
print(f"a: {a} type: {type(a)}")
a = False
print(f"a: {a} type: {type(a)}")
