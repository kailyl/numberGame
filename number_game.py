import random
def ans(number, guess):
    a = 0
    b = 0
    for i in range(len(guess)):
        for n in range(len(number)):
            g = guess[i]
            if g == number[n]:
                if i == n:
                    a += 1
                else:
                    b += 1
    print("a"+ str(a) + " b"+ str(b))

def number_generator():
    num = ""
    while len(num) < 4:
        digit = str(random.randint(0,9))
        if digit not in num:
            num += digit
    return num

def game(number):
    guess = ""
    counter = 0
    while guess != number:
        counter += 1
        guess = input("Enter your guess: ")
        ans(number, guess)
    print("you are the winner!!!")
    print("It took you", counter, "turns!")
def main():
    number = number_generator()
    # print(number)
    game(number)
main()