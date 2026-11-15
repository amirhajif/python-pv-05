# a=int(input("please enter a"))
# b=int(input("please enter b"))


# a,b = int(input("please enter a")),int(input("please enter b"))

# a,b = input("please enter number: ").split(" ") #["1","5"]
# a=int(a)
# b=int(b)
# print(a)
# print(b)

# items = {
#     "burger":500,
#     "sandwich":600
# }

# for item in items:
#     print(item)

# if "burger" in items:
#     print("yes")
# else:
#     print("no")

# Q10
# users = {
# "ali":"1234",
# "sara":"qwerty"
# }

# user_name = input("please enter username:  ")
# pass_word = input("please enter password:  ")

# is_username_exist = user_name in users
# is_password_valid = pass_word == users[user_name]

# if is_username_exist and is_password_valid:
#     print("welcome")
# else:
#     print("invalid username and password!")

            
#Q1

# while True:
#     password = input("please enter your password:   ")
    
#     is_len_valid =len(password)>8
#     is_ch_exist = "@" in password 

#     if is_len_valid and is_ch_exist:
#         break
#     else:
#         print("your password invalid!")
# print("your password saved")

# Q2

# secret = 18
# counter = 0
# while True:
#     hads =int(input("please enter your guessed number:  "))
#     counter+=1
#     if hads> secret:
#         print("reduce your selected number")
#     if hads< secret:
#         print("raise your selected number")        
#     if hads == secret:
#         print(f"congratulation your guess near to {counter} times trying is True!!")
#         break

# Q3
# while True:
#     option = int(input("""
#     1 - sum
#     2 - minus
#     3 - exit
#     please enter option:  """))
#     if option == 1:
#         number1 = int(input(" please enter first number:  "))
#         number2 = int(input(" please enter second number:  "))
#         print(number1+number2)
#     if option == 2:
#         number1 = int(input(" please enter first number:  "))
#         number2 = int(input(" please enter second number:  "))
#         print(number1-number2)
#     if option == 3:
#         break
# print("good bye")
            
# Q4
# sum = 0
# while True:
#     entered_number = int(input(" please enter a number:  "))
#     if entered_number < 0 :
#         break
#     else:
#         sum+=entered_number
# print(sum)


# Q5

# users_info=[]
# while True:
#     user_name = input("please enter your user_name:   ")
#     user_number=int(input("please enter your number:  "))

#     user_info = {
#     "user_name":user_name,
#     "user_number":user_number
#      }
    
#     users_info.append(user_info)
#     option = input('do you want to continue? if no please type s" ')
#     if option == 's"':
#         break

# print(users_info)


# phone_book = {}
# while True:
#     user_name = input("please enter your user_name:   ")
#     user_number=int(input("please enter your number:  "))
#     phone_book[user_name]=user_number
#     option = input('do you want to continue? if no please type s" ')
#     if option == "s":
#         break

# print(phone_book)


# letters = input("please entar a word:    ")
# letters_dict = {}
# letters_set = set(letters)
# for letter in letters_set:
#    count = 0
#    for i in range(0, len(letters)):
#         if letter== letters[i] :
#             count+=1
#    letters_dict.update({letter:count}) 
# print(letters_dict)


# sentence = input("please enter sentence: ")
# letters = {}

# for letter in sentence:
#     if letter in letters:
#         letters[letter] = letters[letter] + 1
#     else:
#         letters[letter] = 1

# print(letters)



# sentence = input("please enter sentence: ")
# letters = {}

# for letter in sentence:
#     letters[letter] = letters.get(letter,0)+1

# print(letters)


# students = [
# {'name':'ali','math':17,'english':18},
# {'name':'sara','math':14,'english':15},
# {'name':'reza','math':19,'english':17}]

# for student in students:
#     average = (student['math']+ student['english'])/2
#     if average > 17:
#         print(f"student:{student['name']} your average is {average} and you are excellent pass!")
#     else:
#         print(f"student:{student['name']} your average is {average} and you   passed!")


# number = int(input("please enter a number:  "))
# # count = 0
# # numbers = []
# revers = 0
# while number > 0:
#     remain = number%10
#     revers = revers*10 + remain
#     number=number//10

# print(revers)
    

# reversed_numbers = list(reversed(numbers))
# sum = 0
# for i in range(0,len(numbers)):
#     pop_number = reversed_numbers.pop()
#     multiple = pop_number*10**(len(reversed_numbers))
#     sum+=multiple
# print(f"the opposite of the entered number is :{sum}")
      
  
# number = int(input("please enter a number:  "))
# original_number = number
# # count = 0
# # numbers = []
# revers = 0
# while number > 0:
#     remain = number%10
#     revers = revers*10 + remain
#     number=number//10

# if original_number == revers:
#     print("palindrome number")
# else:
#     print("not-palindrome number")

def m2(n):
    print(n*2)

def m2_new(n):
    return n*2

# m2(19)

result = m2_new(10)
print(result)


print(m2_new(10))
