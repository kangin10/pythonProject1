'''
파일복사
'''
buffer_size = 1024
with open('hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size) # 1024bit 단위로 읽기
            if not buffer:
                break
