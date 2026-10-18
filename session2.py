# school_student_scores = [20,18,12,7,9,2,16]
# print(school_student_scores)
# print(type(school_student_scores))
# print(school_student_scores[2])

# school_student_names = ["amir","alii","reza","ahmad"]

# Update Element
# school_student_names[1] = "ali"
# print(school_student_names)

# Add Element

# username = input("please enter username: ")
# append
# school_student_names.append(username)
# print(school_student_names)

# school_student_names.append("mohammad")
# print(school_student_names)

# insert
# school_student_names.insert(1,"arsham")
# print(school_student_names)

# Delete

# del
# del school_student_names[1]
# print(school_student_names)

# pop
# deleted_student = school_student_names.pop(3)
# print(school_student_names)
# print(deleted_student)

# deleted_student = school_student_names.pop()
# print(school_student_names)
# print(deleted_student)

# remove
# school_student_names.remove("reza")
# print(school_student_names)


# clear
# school_student_names.clear()
# print(school_student_names)

# # Example Delete From a range
# a = [1, 3, 5, 7, 9, 11, 13]

# # Delete elements between index 2 and 4 (inclusive)
# del a[2:5]

# print(a)



# school_student_names = ["amir","alii","reza","ahmad"]
# school_student_scores = [20,18,12,7,9,2,16]

# SORT-NUMBERS
# school_student_scores.sort(reverse=True)
# print(school_student_scores)

# SORT-STRINGS
# school_student_names.sort()
# print(school_student_names)

# SORTED
# sorted_names = sorted(school_student_names)
# print(sorted_names)
# print(school_student_names)

# REVERSE

# school_student_names.reverse()
# print(school_student_names)

# REVERSED
# reversed_names = list(reversed(school_student_names))
# print(reversed_names)
# print(school_student_names)


# len
# print(len(school_student_names))

# name = "amir hossein hajitabar"
# print(len(name))

# sum
# print(sum(school_student_scores))
# max
# print(max(school_student_scores))
# min
# print(min(school_student_scores))


# calculate average
# print(sum(school_student_scores)/len(school_student_scores))

# cars = ["benz","bmw","prado"]
# carsales_car = cars[:]

# cars.append("prosche")
# carsales_car.append("lexus")
# print(cars)
# print(carsales_car)

# names = ["John", "Charles", "Smith"]
# print(" ".join(names))



# CONDITIONS
# indent
# score = int(input("please enter score: "))
# if score > 10:
#     print("pass")
# else:
#     print("fail")


# username = input("pelase enter username: ")
# if username == "admin":
#     print("welcome")
# else:
#     print("need login again")

# AND

# username = input("please enter username: ")
# password = input("please enter password: ")
# if username=="admin" and password=="admin":
#     print("welcome")
# else:
#     print("invalid")

# OR

# physic_score = 20
# math_score = 10

# if physic_score>10 or math_score>10:
#     print("pass")
# else:
#     print("fail")

# ELIF

# seasson = int(input("please enter seasson: "))
# if seasson==1:
#     print("bahar")
# elif seasson==2:
#     print("tabestan")
# elif seasson==3:
#     print("paiiz")
# elif seasson==4:
#     print("zemstan")
# else:
#     print("invalid input")


school_student_names = ["amir","alii","reza","ahmad"]

search = input("please enter name for search: ")
if search in school_student_names:
    print("exist")
else:
    print("not-exist")
