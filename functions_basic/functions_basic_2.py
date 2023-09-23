#1) countdown
def countdown(num):
    result = []
    for i in range(num,-1,-1):
        result.append(i)
    return result
print(countdown(5))

#2) print and return
def print_return(list):
    print(list[0])
    return list[1]
print(print_return([1,2]))

#3) first plus length
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))

#4)values greater than second
def greater_than_second(list):
    if len(list) < 2:
        return False
    result = []
    for i in range(0, len(list)):
        if list[i] > list[1]:
            result.append(list[i])
    print(len(result))
    return result
print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))

#5) this length, that value
def length_value(size, value):
    result = []
    for i in range(0, size):
        result.append(value)
    return result
print(length_value(4,7))
print(length_value(6,2))