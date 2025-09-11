#Numeric Data Type
num1 = 55
num2 = 5.3
print(type(num1), num1)
print(type(num2), num2)

num3 = 6.3j #conplex number
print(type(num3), num3)

#List Data Type
languages = ["Python", "Dart", "Web", 23]
print(type(languages), languages)

#To access items from the list, we use the index number

print(languages[0])
print(languages[3])

#Tuble Date Type
products = ('XBox', 499.99, "Habibi", 23)
print(type(products), products)

productName = products[0]
price = products[1]
print(productName + ":", price)

#String Data Type
name = "Momed Ossufo"
print(type(name), name)

#Set Data Type
student_ids = {112, 114, 117, 113}
print(type(student_ids), student_ids)
print(student_ids)

#Dictionary Data Type
capital_city = {
    "Mozambique": "Maputo", 
    "South-Africa": "Pretoria"
}
print(type(capital_city), capital_city)

print("Capital of Mozambique:", capital_city['Mozambique'])
print("Capital os South-Africa:", capital_city["South-Africa"])