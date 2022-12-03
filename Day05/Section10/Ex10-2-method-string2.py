#join() 메소드
s = '-'.join('python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

#split() 메소드
s = 'Life is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)

#replac()
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백제거
s = '       apple'
print(s)
result = s.lstrip()
print(result) # 왼쪽 공백 제거

s = 'apple     '
print(s)
result = s.lstrip()
print(result) # 오른쪽 공백 제거

s = '     apple      '
print(s) # 양쪽 공백 제거
print(result)

# 전체 공백제거
s = 'a p p l e '
print(s)
result = s.replace(' ', '')
print(result)