# users = []
# if len(users)==0:
#     print("list empty")
# else:
#     print("list not empty")

# users = []

# if users:
#     print("not empty")
# else:
#     print("empty")


# LOOP
# users = ["amir","ali","reza","ahmad"]
# for user in users:
#     print(f"welcome mr {user}")

"""
welcome mr amir
welcome mr ali
welcome mr reza
welcome mr ahmad
"""


# users = ["amir","ali","reza","ahmad"]
# for user in users[::-1]:
#     print(f"welcome mr {user}")


# scores = [20,12,8,13,20,2,9]
"""
20 ---> pass
12 ---> pass
8  ---> fail
.....
"""
# for score in scores:
#     if score>=12:
#         print(f"{score} --> pass")
#     else:
#         print(f"{score} --> fail")
            
# numbers = [10,14,-15,19,0,-10,0]

# for number in numbers:
#     if number>0:
#         print(f"{number} is positive")
#     elif number==0:
#         print(f"{number} is zero")
#     else:
#         print(f"{number} is negative")


# numbers = [10,2,12,20,14,8]
# # show sum of numbers in list --> dont use of sum
# sum = 0
# for number in numbers:
#     # sum = sum + number
#     sum += number
# print(sum)


# numbers = [10,23,12,19,14,89]
# # count the number of even and odd number in the list
# even_counter = 0
# odd_counter = 0
# for number in numbers:
#     if number%2==0:
#         # even_counter = even_counter + 1
#         even_counter+=1
#     else:
#         odd_counter = odd_counter + 1

# print(f"count of even number: {even_counter}")
# print(f"count of odd number:  {odd_counter}")

# for i in range(0,15):
#     print("hello",end=" ")

# n= int(input("please enter n: "))
# for i in range(0,n+1):
#     print(i)

# factoriel
# n=int(input("please enter n: "))
# factoriel = 1
# for i in range(1,n+1):
#     # factoriel = factoriel * i
#     factoriel *= i

# print(factoriel) 

# BREAK ---> Stop
# CONTINUE ---> edame

# for i in range(0,10):
#     if i==6:
#         break
#     print(i)

# for i in range(0,10):
#     if i==6:
#         continue
#     print(i)


# WHILE
# i=0
# while i<10:
#     print("hello")
#     i=i+1

# factoriel - while

# n=int(input("please entre n: "))

# i=1
# fact=1
# while i<=n:
#     fact = fact * i
#     i=i+1
# print(fact)


# Peymayesh dar list
# names = ["amir","ali","reza","ahmad"]
# i=0
# while i<len(names):
#     print(names[i])
#     i=i+1


# TUPLE

# salaries = (1000,2000,3000)
# print(type(salaries))
# print(salaries)
# print(salaries[1])
# # salaries[1]=2500
# for salary in salaries:
#     print(salary)


# users = ["amir","ali","reza","ahmad"]
# print(users.index("ali"))

names = ("amir","ali","reza","ahmad")

print(names.index("ali"))
