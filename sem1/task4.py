import math

result = []
for num in range(2500):
    if str(num)[-1] != '1': continue
    elif math.modf(math.sqrt(num))[0] != 0: continue
    result.append(num)
print(result)
