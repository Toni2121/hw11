tuple1: tuple[int] = (99,)
tuple2: tuple[int] = (77, 88, 99)


def return_len():
    tuple3 = (77, 88, 99)
    return len(tuple3)


print(f"tuple's len is: {return_len()}")


def combined_tuple():
    tuple4 = (1, 2, 3)
    tuple5 = (4, 5, 6)
    return tuple4 + tuple5


print(f"combined tuple: {combined_tuple()}")


def similar_numbers(tuple6, tuple7):
    set1 = set((tuple6))
    set2 = set((tuple7))
    similar = set1 & set2
    return similar


tuple6 = (6, 5, 4, 3)
tuple7 = (4, 3, 2, 1)

result = similar_numbers(tuple6, tuple7)
print(f"similar tuple: {result}")

tuple6 = (6, 5, 4, 3)
tuple7 = (4, 3, 2, 1)
similar_numbers(tuple6, tuple7)
different = set(tuple6) ^ set(tuple7)
print(f"similar tuple: {different}")


def tuple_and_index(tuple8, index):
    if index > len(tuple8):
        return None
    else:
        return tuple8[index]


print(f"the number in the desired index is: {tuple_and_index((1, 2, 3, 4, 5), 4)}")


def reversed_tuple(tuple9):
    return tuple(reversed(tuple9))


tuple9 = (1, 2, 3, 4, 5, 6)
print(f"reversed tuple: {reversed_tuple(tuple9)}")


def div_by_ten(tuple10, num1):
    total = 0
    for number in tuple10:
        if num1 % number == 0:
            total += 1
    return total


print(f"amount of dividable number is: {div_by_ten((1, 2, 3, 4, 5), 10)}")


def tuple_mul_num(tuple11, num2):
    return tuple11 * num2


print(f"multiplied tuple: {tuple_mul_num((1, 2), 3)}")


def index_and_element(tuple12):
    tuple13 = [f"Index {index}: {element}" for index, element in enumerate(tuple12)]
    return tuple(tuple13)


print(index_and_element(("Mor", "Dani", "Lior", "Menny")))


def dictionary(tuple14) -> dict:
    tuple14_dict = dict(
        {"biggest number": max(tuple14), "smallest number": min(tuple14), "avg": sum(tuple14) / len(tuple14), \
         "amount of numbers": len(tuple14), "sorted": sorted(tuple14), "rev sorted": (tuple14[::-1])})
    times = {}
    for number in tuple14:
        if number in times:
            times[number] += 1
        else:
            times[number] = 1
    tuple14_dict["Times"] = times
    return (tuple14_dict)


print(dictionary((1, 2, 3, 4, 5, 5)))



def tuple_letters(tuple15: tuple[str]):
    return ''.join(tuple15)


print(tuple_letters(("h", "e", "l", "l", "o")))



def tuple_word(tuple16: tuple[str]):
    letters = [l for l in tuple16]
    return tuple(letters)

print(tuple_word("hello"))



def remove_element(tuple17, num4):
    temp_list = list(tuple17)
    if num4 in temp_list:
        temp_list.remove(num4)
    new_tuple17 = tuple(temp_list)
    return tuple(new_tuple17)

print(f"remove_element: {remove_element((1, 2, 3, 4, 5), 3)}")



def no_double_tuple(tuple18):
    while True:
        temp_list2 = []
        for n in tuple18:
            if n not in temp_list2:
                temp_list2.append(n)
            else:
                continue
        new_tuple18 = tuple(temp_list2)
        return new_tuple18


print(f"no_double_tuple: {no_double_tuple((1, 2, 3, 4, 5, 3, 4))}")



def returns_number_index(tuple19, num3):
    indexes = [index for index, value in enumerate(tuple19) if value == num3]
    return tuple(indexes)


print(f"number's indexes: {returns_number_index((1, 2, 3, 4, 5, 6, 4), 4)}")



def grades():
    user_names_list = []
    user_grades_list = []
    while True:
        user_names = input("please enter names (enter 'done' to finish): ")
        if user_names == 'done':
            break
        else:
            user_names_list.append(user_names)
    while True:
        user_grades: int = int(input("please enter the grades (enter -999 to finish): "))
        if user_grades == -999:
            break
        else:
            user_grades_list.append(user_grades)
    total_list = zip(user_names_list, user_grades_list)
    return tuple(total_list)


print(grades())