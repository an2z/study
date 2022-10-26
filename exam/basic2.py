# 파이썬 연산자 ( 산술 | 비교 | 할당 | 논리 | 비트 )

# 산술연산자 : +, -, *, /, **, //, %
a = 1
b = 2

c = a + b      # 덧셈
d = a - b      # 뺄셈
e = a * b      # 곱셈
f = a / b      # 나누기
g = a // b     # 몫을 구한다
h = a % b      # 나머지를 구한다


# 비교연산자 : ==, !=, <, >, <=, >=
a = 2
b = 2
c = 3
d = 1

if a == b :                       
    print('a는 b와 같습니다.')

if a != c :
    print('a는 c는 같지않습니다.')  

if a < c : 
    print('a는 c보다 작다.')

if a > d :
    print('a는 d보다 크다.')

if a <= b :
    print('a는 b보다 작거나 같다.')

if a >= b :
    print('a는 b보다 크거나 같다.')


# 할당연산자 :  +=, -=, *=, %=, //=
a = 3
a += 3         # a = a + 3

b = 5
b -= 2         # b = b - 2

print(a)
print(b)


# 논리연산자 : and, or, not
a = 3
b = 2
c = 3

if a > b and a == c :                # 조건이 '모두' 참이여야 출력
    print('조건이 모두 참이다.')

if a > b or a == b :                 # 조건이 둘 중 하나만 참이여도 출력
    print('조건 둘중 하나가 참이다')

if not a < b :                       # 조건이 참이 아닐경우 출력
    print('조건이 참이 아니다')


# 비트연산자 : &(AND), |(OR), ^(XOR), ~(보수), <<, >>
# 16bit / 2진수 표현
a = 0x03 #0000 0011
b = 0x04 #0000 0100
c = 0x01 #0000 0001

d = a & b         # 각 비트가 모두 1일때만 1 ➡ 0000 0000
print(d)

e = a | b         # 각 비트가 하나만 1이여도 1 ➡ 0000 0111
print(e)

f = a ^ b         # 각 비트가 다를때만 1 ➡ 0000 0111
print(f)

g = ~a            # 2의 보수를 구한다
print(g)

h = a << 1        # 비트를 왼쪽으로 1칸씩 shift ➡ 0000 0110
print(h)

i = a >> 1        # 비트를 오른쪽으로 1칸씩 shift ➡ 0000 0001
print(i)