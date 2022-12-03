#welcome() 함수 정의
def welcom():
    print('Hello Python')
    print('Nice to meet you')

welcom() # 함수 호출

# 매개변수 0, 리턴 X
def introduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

introduce('james', 25)

# 가변 매개변수 함수
def show(*args):
    for item in args:
        print(item)

show('python')
show('python', 'happy', 'birthday')

# 반환(return)값이 있는 변수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)

# 매개변수 0 리턴 0
def plus(num1, num2):
    return num1 + num2

print(plus(1,3))
print(plus(2,5))

area = 0
def move():
    global area
    area += 1
    return area

result = move()
print('유닛이 오른쪽으로 {}칸 이동했습니다.'.format(result))