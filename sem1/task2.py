import random

def qsort(sequence):
    if len(sequence) <= 1:
        return sequence
    greater = []
    equally = []
    less = []
    random_num = random.choice(sequence)
    for num in sequence:
        if num > random_num: greater.append(num)
        elif num < random_num: less.append(num)
        else: equally.append(num)
    return qsort(greater) + equally + qsort(less)

sequence = [random.randint(1, 100) for i in range(20)]
print(sequence)
print(qsort(sequence))
