import prompt
from random import randrange
import random
import operator as op
rand_ops = {"+": op.add, "-": op.sub, "/": op.truediv, "*": op.mul}


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print('What is the result of the expression?')
    count = 1
    rand_ops = {"+": op.add, "-": op.sub, "*": op.mul}
    while count < 4 and count > 0:
        op_key = random.choice(list(rand_ops.keys()))
        first_num = randrange(1, 100)
        second_num = randrange(1, 100)
        print(f'Question: {first_num} {op_key} {second_num}')
        result = rand_ops[op_key](first_num, second_num)
        answer = prompt.string('Your answer: ')
        if int(answer) == result:
            print('Correct!')
            print('Congratulations, ' + name + '!')
            count = count + 1
        else:
            print(answer + ' is wrong answer ;(. \
            Correct answer was ' + str(result) + '.')
            print('Let\'s try again,' + name)
            count = -1


if __name__ == '__main__':
    main()
