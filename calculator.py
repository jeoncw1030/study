# 1. 숫자는 0~9까지 들어갈 수 있습니다. (두 자리 안됨)
# 2. 사칙연산(+.-.*./)만 가능합니다.
# 3. 0을 사용할 수 있습니다.


def calc(str):
    first_list = list(str)
    for n in first_list :
        if '' #공백일때
        #연산기호일때
        #숫자일때
    

def hungry(num): 
    if num==0 :
        print(num)
        return
    result = ''
    if num%3 == 0 :
        result = 'fizz' 

    if num%5 ==0 :
        result += 'buzz'
    else:
        result = num
    print(result)


if __name__ == '__main__':
    str = input('Enter the arithmetic expression : ')
    calc(str)

    print('calculation result : %s = %',str, OOO)
    
    
    
    
    for n in range(31):
        hungry(n)