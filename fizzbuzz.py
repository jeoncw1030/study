# 어떤 숫자를 받는 함수를 만듭니다
# 2. 그 숫자가 3의 배수이면 fizz 를 출력 합니다.
# 3. 그 숫자가 5의 배수이면 buzz 를 출력합니다.
# 4. 그 숫자가 3의 배수이면서 5의 배수이면 fizzbuzz 를 출력합니다.



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
    for n in range(31):
        hungry(n)