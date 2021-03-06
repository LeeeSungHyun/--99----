# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 예제 입력 1 
# 24 18
# 예제 출력 1 
# 6
# 72

#유클리드 호제법 = 두수 비교 후 큰수%작은수 = 나머지   -> 작은수 % 나머지 = 0 일때 나머지가 최대공약수
#최소공배수는 최대공약수로 두수를 나눈 몫을 다 곱하면 됌

n, t = map(int,input().split())                #두개의 자연수 입력
n1, t1 = n, t

if n > t:                       #ex) 2304, 1440   num = 864 n=2304 t = 1440  나누고 난 뒤 n = t , t = num 
    num = n%t                       
    while num !=0:                  
        n=t
        t = num
        num = n%t
    print(t)
    bae = t * (n1//t) * (t1//t)                         #최소공배수는 최대공약수 * (n//최대공약수) * (t//최대공약수)
    print(bae)

elif n < t:
    num = t%n 
    while num !=0:
        t=n
        n = num
        num = t%n
    print(n)
    bae = n * (n1//n) * (t1//n)
    print(bae)

else:                              # n = t 인 경우
    print(n)
    print(t)

    

