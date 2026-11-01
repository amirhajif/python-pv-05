# reception - untill damad come - if garson come dont say welcome
# while True:
#     name = input("please enter name: ")
#     if name == "garson":
#         continue
#     if name == "damad":
#         break
#     print(f"welcome mr/mrs {name}")

# an app for teacher and show average of score - import student score - ask to continue or not?
# counter = 0
# sum = 0
# while True:
#     score = int(input("please enter score: "))
#     sum += score
#     counter +=1
#     option = input("do you want continue?(y/n): ").lower()
#     if option=="n":
#         break

# print(sum/score)

# n=int(input("please enter number: "))
# sum=0
# while True:
#     sum += n%10
#     n = n//10
#     if n==0:
#         break

# print(sum)

# 157
# n=int(input("please enter number: "))
# sum=0
# while n>0:
#     sum += n%10
#     n = n//10
#     # 15 ---> 1 ---> 

# print(sum)

# DICITONARY

# student = {
#     "name":"amir",
#     "age":26,
#     "score":19.8
# }

# print(student)
# print(type(student))

# # show a value of a key
# print(student["name"])

# # update a value of key
# student["score"] = 18.8
# print(student)

# # add key and value
# student["school_name"] = "alghadir"
# print(student)

# # get
# # print(student["father_name"])

# print(student.get("math_score",0))
# print(student.get("father_name","we dont have this key"))

# # delete a key & value
# del student["score"]
# print(student)

# students = []

# while True:
#     name = input("please enter name: ")
#     age = int(input("please enter age: "))
#     score = int(input("please enter score: "))

#     student = {
#         "name":name,
#         "age":age,
#         "score":score
#     }

#     students.append(student)

#     option = input("do you want to contunye?(y/n): ")
#     if option=="n":
#         break

"""
[
            {'name': 'amir', 'age': 25, 'score': 20},
            {'name': 'reza', 'age': 19, 'score': 18},
            {'name': 'jafar', 'age': 18, 'score': 17}
            
]
"""

# for student in students:
#     print(f"student {student['name']} : age -> {student['age']} and score -> {student['score']}")


# student = {
#     "name":"amir",
#     "age":26,
#     "score":19.8
# }

# # items
# # print(student.items()) # [('name', 'amir'), ('age', 26), ('score', 19.8)]

# # for key,value in student.items():
# #     print(f"{key}---->{value}")


# # keys
# print(student.keys()) # ['name', 'age', 'score']

# # values
# print(student.values()) # ['amir', 26, 19.8]



# Create Menu

"""
1-say hello
2-say bye
3-say name
4-exit
enter option:
"""
while True:
    option = int(input("""
1-say hello
2-say bye
3-say name
4-exit
enter option: """))

    # option = int(input("1-say hello\n2-say bye\n3-say name"))
    if option==1:
        print("hello")
    elif option==2:
        print("bye")
    elif option==3:
        print("amir")
    else:
        break
    
