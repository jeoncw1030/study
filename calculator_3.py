# 1. 숫자는 0~9까지 들어갈 수 있습니다. (두 자리 안됨)
# 2. 사칙연산(+.-.*./)만 가능합니다.
# 3. 0을 사용할 수 있습니다.

from pythonds.basic.stack import Stack

def calculator(str):
    expression = [] #list
    numbers = []
    operator = Stack() #stack
    ranking = {'+':1,'-':1,'*':2,'/':2 }
    middle_num = 0
    right_num = 0
    left_num = 0

    # 담기
        #숫자 : 배열에 넣기
        #기호(맨 위 연산자보다 우선순위가 낮거나 같을 때 ) : 기존 값들을 배열에, 본인은 스택에
        #기호(우선순위 높을 때) : 스택에 본인 값 저장
    for s in str:
        if s.isdigit():
            expression.append(s)
        elif s in ranking.keys():
            if len(operator) == 0:
                operator.append(s)
            elif ranking[s] <= ranking[operator.peek()] :
                while operator:
                    expression.append(operator.pop())
                operator.push(s)
            else:
                operator.push(s)
    
    # 남은 기호들 배열에 넣기
    while operator:
        expression.append(operator.pop())
    


    # 계산하기
    for e in expression:
        if e.isdigit():
            numbers.push(e)
        else:
            right_num = int(numbers.pop())
            left_num = int(numbers.pop())
            if e == '+':
                middle_num = left_num+right_num
            elif e == '-':
                middle_num = left_num-right_num
            elif e == '*':
                middle_num = left_num*right_num
            elif e == '/':
                middle_num = left_num/right_num

            numbers.push(middle_num)

    return numbers.pop()
  

if __name__ == '__main__':
    s = 3+5*2 #input("Enter the arithmetic expression : ")
    result = calculator(s)
    print('Calculation result : {} = {}'.format(s, result))


''' 이전 연산 코드
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
'''
''' example = [
        '1+1',
        ' 2 - 5',
        '5 * 2',
        '8/ 2',
        '3*4-2',
        '4-1/3',
        '1-1-1'
    ]
    for e in example:
        result = calculator(e)
        print('calculation result : {} = {}'.format(e, result))
    ''' 