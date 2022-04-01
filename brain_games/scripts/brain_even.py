import prompt
from random import randrange


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        num = randrange(100)
        result = ''
        if num % 2 == 0:
            result = 'yes'
        else:
            result = 'no'
        print('Question:' + str(num))
        answer = prompt.string('Your answer? ')
        if answer == result:
            print('Correct!')
            count = count + 1
        else:
            print(answer + ' is wrong answer ;\
                (. Correct answer was ' + result + '.')
            count = 0
    print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
