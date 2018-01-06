# 2017. 12. 02 (토)

def countdown(number):
    if not number:
        return
    number -= 1
    print(number)
    countdown(number)


if __name__ == '__main__':
    countdown(100)