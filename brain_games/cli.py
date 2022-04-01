import prompt

data = {
    'name': ''
}


def welcome_user():
    data['name'] = prompt.string('May I have your name? ')
    print("Hello, " + data['name'])


if __name__ == '__welcome_user__':
    welcome_user()
