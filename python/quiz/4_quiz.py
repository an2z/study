# >> 초보자를 위한 파이썬 300제 (31 ~ 40) <<

# 031
# 아래 코드의 실행 결과를 예상해보세요.
a = "3"
b = "4"
print(a + b)  # 34가 출력

# 두 문자열에 대해 덧셈기호는 문자열의 연결을 의미


# 032
# 아래 코드의 실행 결과를 예상해보세요.
print("Hi" * 3)  # HiHiHi 출력

# 문자열에 대한 곱셈은 문자열의 반복을 의미


# 033
# 화면에 '-'를 80개 출력하세요. 
print('-' * 80)


# 034
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예: python java python java python java python java
t1 = 'python'
t2 = 'java'
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)


#⭐035
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))

# print 포맷팅에서 %s는 문자열, %d는 정수형 데이터 값의 출력을 의미


#⭐036
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("이름: {} 나이: {}.format(name1, age1)")
print("이름: {} 나이: {}.format(name2, age2)")

# 문자열 포맷 메서드는 타입과 관계없이 값이 출력될 위치에 {}를 적어주면 됨


#⭐037
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# f-string은 문자열 앞에 f가 붙은 형태
# f-string을 사용하면 {변수}와 같은 형태로, 문자열 사이에 타입과 관계없이 값을 출력할 수 있음


# 038
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
result_replace = 상장주식수.replace("," , "")
result_int = int(result_replace)
print(result_int, type(result_int))


# 039
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
분기 = "2020/03(E) (IFRS연결)"

print(분기[:7])


# 040
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
data = "   삼성전자    "

print(data.strip())

# strip()은 좌우 공백을 제거해주는 함수이다