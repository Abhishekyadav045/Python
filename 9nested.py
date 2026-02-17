# Name={
#     "India":"Delhi" ,
#     "Sri Lanka":"x",
#     "USA" :"Washington",
#     "France" : "abhc"
    
# }
# print(Name)
# print(Name["India"])
# Name["Japan"]="Tokyo"
# print(Name)
# Name["USA"]="New York"
# print(Name)
# del Name["France"]
# print(Name)


# School={
#     "Abhi":85,
#     "anurag":89,
#     "Priya":97,
#     "sachin":98
# }
# print(School.keys())
# print(School.values())
# print(School.items())
# print(School.get("Rahul"))
# School.update({
#     "Naman":94,
#     "Pradum":75,
#     "Aabid":70 })
# print(School)
# School.pop("Priya")
# print(School)
# #School.pop()
# School.clear()
# print(School)


# X={
#     "x":5,
#     "y":6,
#     "Z":5,
#     "w":4
# }
# X.copy()
# X.update({
#     "q":3,
#     "p":9,
#     "o":2
# })
# print(X)


# sentence= input("Enter a sentence:")
# words=sentence.split()
# frequency={}

# for word in words:
#     if word in frequency:
#         frequency[word] +=1
#     else:
#         frequency[word]=1
# print(frequency)



# text=input("Enter a Words:")
# s=text[::-1]
# if text==s:
#     print("jj")
# else:
#     print("ffj")

Students= [
    {"name": "Amit","Age":20},
    {"name":"Neha","Age":22},
    {"name":"Rahul", "Age":19}
]

# print(Students[0]["name"])
# for i in Students:
#     print(i["name"])

# Students.append({
#     "name":"Priya","Age":21
# })
# print(Students) 

Students[2]["age"]=20
print(Students)


