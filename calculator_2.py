# 1. 숫자는 0~9까지 들어갈 수 있습니다. (두 자리 안됨)
# 2. 사칙연산(+.-.*./)만 가능합니다.
# 3. 0을 사용할 수 있습니다.


def calculator(str):
    numbers = []
    operator = []
    middle_num = 0

    for s in str:
        if s.isdigit():
            numbers.append(s)
        elif s != ' ':
            operator.append(s)

    while operator:
        o = operator.pop()        
        right_num = int(numbers.pop())
        left_num = int(numbers.pop())

        if o == '+':
            middle_num = left_num+right_num
        elif o == '-':
            middle_num = left_num-right_num
        elif o == '*':
            middle_num = left_num*right_num
        elif o == '/':
            middle_num = left_num/right_num
        #if middle_num < 0:
        #    middle_num *= -1
        numbers.append(middle_num)

    return middle_num

    

if __name__ == '__main__':
    example = [
        '1+1 - 4',
        '3+1 - 4',
        '4+ 1 + 1',
        '5 +1',
        '5 * 2',
        '8/ 2',
    ]
    for e in example:
        result = calculator(e)
        print('calculation result : {} = {}'.format(e, result))
