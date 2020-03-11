
# 파이썬에서 변수에 대해 name을 정의
# namespace는 names를 담을 수 있는 공간
# module은 파이썬 코드를 담은 파일
# 각 모듈은 자신만의 namespace 가지고, 보통은 모듈 이름과 동일

import sys
sys.path

# sys 모듈을 import 하였을때, sys는 모듈 이름, path는 sys 모듈의 namespace에 담겨있는 name 중 하나

# import 하지 않고 인터프리터에 의해 해당 파이썬 파일(모듈)이 실행되는 경우에는 다음 조건 사용
# if __name__ == '__main__' 
# 파이썬 인터프리터가 소스 파일을 읽고 그 안의 모든 코드를 실핼하기 전에 __name__이라는 변수를 __main__으로 세팅하기 때문


# using_name.py 파일 생성
# import 했을 때랑 자체 실행했을때 결과 다름
'''
if __name__ == '__main__':
	print ('This program is being run by itself')
else:
	print ('I am being imported from another module')
'''
import using_name