from random import shuffle
from participant_list import read
from send import work

def pick(args):
    people = read(print=False)
    choices = evaluate(people)
    if args.nosend:
        print(list(choices))
    else:
        work(choices)

def evaluate(list_of_folks):
    shuffle(list_of_folks)
    return _pair_generator(list_of_folks)


def _pair_generator(list_of_folks):
    for i in range(len(list_of_folks)):
        yield list_of_folks[i-1][0], list_of_folks[i][1], list_of_folks[i][0]  # [send this name],[to this mail],[receiver's name]
