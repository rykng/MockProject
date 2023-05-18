import random
import string


# https://www.educative.io/edpresso/how-to-generate-a-random-string-in-python
class RandomGenUtil():

    def get_random_digits(length=1):
        list_digits = string.digits
        ran_digits = ''.join(random.choice(list_digits) for i in range(length))
        return ran_digits

    def get_random_alphabets(length=1):
        list_letters = string.ascii_letters
        ran_letters = ''.join(random.choice(list_letters) for i in range(length))
        return ran_letters

    def get_random_lowercase(length=1):
        list_letters = string.ascii_lowercase
        ran_letters = ''.join(random.choice(list_letters) for i in range(length))
        return ran_letters

    def get_random_uppercase(length=1):
        list_letters = string.ascii_uppercase
        ran_letters = ''.join(random.choice(list_letters) for i in range(length))
        return ran_letters

    def get_random_punctuation(length=1):
        list_letters = string.punctuation
        ran_letters = ''.join(random.choice(list_letters) for i in range(length))
        return ran_letters

    def get_random_all(length=1):
        list_letters = string.ascii_letters + string.digits
        ran_letters = ''.join(random.choice(list_letters) for i in range(length))
        return ran_letters

    # check if number is a odd number
    def is_odd(num):
        return num % 2 != 0

    def is_even(num):
        return num % 2 == 0

    # 2d4+3 means roll 2 die-4s and add 3 to the roll.
    def roll(dice_equation):

        if "+" not in dice_equation:
            dice_equation = dice_equation + "+0"

        dice_str, base_hit = dice_equation.split("+")
        num_dice, die_sides = dice_str.split("d")

        total = 0
        for i in range(int(num_dice)):
            total = total + random.randint(1, int(die_sides))

        total = total + int(base_hit)
        return total
