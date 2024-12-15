# 1 задание

def greet(name):
    return "Hello, "+name
print(greet("Misha"))

def square(number):
    return number*number
print(square(3))

def max_of_two(x, y):
    return max(x, y)
print(max_of_two(2, 8))

# 2 задание

def describe_person(name, age=30):
    return "The person's name is " + name + " and he's " + str(age) + " years old"
print(describe_person("Nick"))
print(describe_person("Kevin", 18))

# 3 задание

def is_prime(number):
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True
print(is_prime(32), is_prime(29))
