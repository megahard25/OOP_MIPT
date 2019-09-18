import math

indicator = True
sequence = []
while indicator:
    number = input()
    if number == "End": break
    try:
        number = float(number)
    except:
        raise TypeError(f"Input must be 'int' or 'float'!")
    sequence.append(number)
if not sequence:
    raise ValueError("Sequence must not be empty!")
print("Max value in sequence: {}".format(max(sequence)))
print("Min value in sequence: {}".format(min(sequence)))
average = lambda seq: sum(seq)/len(seq)
avg_val = average(sequence)
print("Average value in sequence: {}".format(avg_val))
standard_deviation = math.sqrt(sum([(i - avg_val)**2 for i in sequence]))/len(sequence)
print("Standard_deviation of sequence: {}".format(standard_deviation))
