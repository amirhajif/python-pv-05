# user = {
#     "username":"amir",
#     "password":"amir123"
# }

# items = list(user.items())
# print(items)
# print(type(items))


# username = "amir"
# password = "amir123"

# print(list(username,password))





# numbers = [24,11,3,99,2,7]
# for i in range(0,len(numbers)):
#     if numbers[0]>numbers[1]:
#         del numbers[0]
#     else:
#         del numbers[1]
#     if len(numbers) == 1:
#         break
# print(numbers)



# number_zero = 0
# number_positive = 0
# sum_positive = 0
# number_negative = 0
# sum_negative = 0
# numbers = [10,-1,0,12,14,-9,-3,0.19,0]
# for number in numbers:
#     if number>0:
#         sum_positive+=number
#         number_positive+=1
#     if number == 0:
#         number_zero+=1
#     if number<0:
#         sum_negative+=number
#         number_negative+=1
# print(round(sum_positive/number_positive,2))
# print(round(sum_negative/number_negative,2))
# print(f"number of zeros are:  {number_zero}")




# numbers = [24,11,3,99,2,7]
# minimum = numbers[0]

# for number in numbers:
#     if number<minimum:
#         minimum = number

# print(minimum)


# SET
# cars = {"bmw","benz","prado","benz"}
# print(cars)

# for car in cars:
#     print(car)

# cars.add("toyota")
# print(cars)

# cars.remove("bmww")
# print(cars)

# cars.discard("bmww")
# print(cars)

cars = {"bmw","benz","prado"}
carsale_cars = {"pride","pego","prado","patrol"}

# all_cars = cars.union(carsale_cars)
# print(all_cars)

# cars.update(carsale_cars)
# print(cars)

# cars.intersection_update(carsale_cars)
# print(cars)

# intersection = cars.intersection(carsale_cars)
# print(intersection)


# symmetric = cars.symmetric_difference(carsale_cars)
# print(symmetric)

# FUNCTION

# definition
def say_hello():
    print("hello")

# parameter
def say_hello_by_name(name):
    print(f"hello mr/mrs {name}")

def rectangle_area(tol,arz):
    print(tol*arz)

def total_price(count,price):
    if count>5:
        print(count*price*0.9)
    else:
        print(count*price)

def factoriel(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i

    print(fact)

def show_names(names):
    for name in names:
        print(name)


def introduce_person(name="amir",age=25):
    print(f"mr/mrs {name} with {age} years old")

# introduce_person("amir",25)
# introduce_person(age=25,name="amir")
introduce_person(age=26)


# call
# say_hello()
# say_hello_by_name("amir")
# rectangle_area(10,8)

# show_names(["amir","ali","reza"])

# keyword-argumants
# default value
