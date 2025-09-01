import time

def myfunc():
    start = time.time()
    print('함수가 실행됩니다.')
    end = time.time()
    print(f"함수 수행시간: {end-start}초")

myfunc()
