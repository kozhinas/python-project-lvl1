from brain_games.cli import welcome_user
from brain_games.game_rules import game_rules
# from brain_games.question import question


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    game_rules()
    # question()


if __name__ == '__main__':
    main()
