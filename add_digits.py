import sys


def add_digits(number: int):
    digit_summation = 0
    while(number > 0):
        digit_summation += number % 10
        number = number // 10

    return digit_summation


if __name__ == "__main__":
    print(sys.argv[0])
    if(len(sys.argv) == 1):
        raise RuntimeError(
            "Need to pass the number to calculate sum of digits")
    elif(len(sys.argv) == 2):
        number = int(sys.argv[1])
        temp_number = number
        while(True):
            if((temp_number // 10) == 0):
                break
            digit_summation = add_digits(temp_number)
            temp_number = digit_summation

        print(digit_summation)
    else:
        raise RuntimeError("Just provide one number")
