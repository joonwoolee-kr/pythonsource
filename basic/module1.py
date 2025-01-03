# 패키지: 모듈 모음

# 모듈: 함수, 변수, 클래스를 모아 놓은 파이썬 파일
# .py로 작성된 파일은 모듈

# 파이썬에서 제공되는 기본 모듈 사용하기
# 모듈 불러오기
# import 모듈명

# add 함수만 삽입
from mod1 import add

# mod1 모듈 안에 있는 모든 요소
from mod1 import *

print(add(13, 9))
print(sub(13, 9))


from mod2 import prt1, prt2

prt1()
prt2()

import mod3

print(mod3.add(17, 5))

n = mod3.Math()
print(n.solv(6))

print(mod3.PI)
