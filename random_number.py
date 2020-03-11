from random import seed
from random import shuffle
from random import randrange
import sys


sequence = [i for i in range(20)]
shuffle(sequence)

def generate_sequence(tc):
    num_of_ppl = []
    shuffle(tc)
    arr = []

    x = 0
    while x <= (len(tc)-3):
        num_of_ppl.append(randrange(2, 4, 1))
        x = sum(num_of_ppl)

    remaining_people = (num_of_ppl[-1] + (len(tc) - sum(num_of_ppl)))
    num_of_ppl[-1] = remaining_people

    for ele in num_of_ppl:
        arr.append(tc[:ele])
        del tc[:ele]

    return arr


num_of_ppl = []
num_of_ppl.append(randrange(2, 4, 1))
print(num_of_ppl)
