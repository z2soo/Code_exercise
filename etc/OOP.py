###############################################################################

class robot:
    # 변수 : 속성
    name = 'robot'
    age = 0

    # 함수 : 메소드
    # 메소드의 첫번째 인자로 self를 전달

    # 생성자 init 는 객체가 만들어질 때 호출되는 함수
    def __init__(self, name, age):
        print('robot 생성자 호출')
        self.name = name
        self.age = age
    
    # 소멸자 del은 객체가 사라질 때 호출되는 함수
    def __del__(self):
        print('robot 소멸자 호출')
    
    def info(self):
        print('나의 이름은', self.name, '입니다')
        print('나이는', self.age,'입니다')

# 실행
r = robot('Bill',7)
r.info()
del r

###############################################################################

# 상속받고싶은 클래스 이름을 괄호 안에 작성
# 부모 클래스 모든 내용이 자식에게 전달됨
# 부모 클래스 메소드 사용시 super() 사용
# 부모 클래스 메소드를 자식이 재정의 가능, 오버라이딩
# 파이썬 다중상속 가능

class strong_robot(robot): 
    weapon = 'gun'

    def __init__(self, name, age, weapon):
        print('strong_robot 생성자 호출')
        super().__init__(name, age)
        self.weapon = weapon

    def info(self):
        super().info()
        print(self.weapon, '무기로 싸웁니다')

# 실행
s = strong_robot('hulk',3,'sword')

###############################################################################

# 속성 이름 앞에 언더바 2개 쓰면 외부에서 접근 불가
# get, set 메소드를 사용하여 속성 다루기

class test:
    __data = 10
    def getData(self):
        return self.__data
    def setData(self,data):
        self.__data = data 

# 실행
t = test()
print(t.getData())
t.setData(20)
print(t.getData())
#t.__data

###############################################################################
#<변수>

# 클래스 변수는 클래스에 하나만 존재하는 반면, 인스턴스 변수는 각 객체 인스턴스 마다 별도로 존재

# 클래스 변수 외부 엑세스 : 클래스명.변수명

# 인스턴스 변수 내부 엑세스 : self.변수명
# 인스턴스 변수 외부 엑세스 : 객체변수.인스턴스변수

# 변수나 메서드를 private 하게 만드려면 __ 사용

###############################################################################<메서드>

# 인스턴스 메서드 : 객체의 인스턴스 필드를 self를 통해 엑세스

# 정적 메서드
# self 파라미터를 갖지 않고, 인스턴스 변수에 엑세스 불가
# 객체와 독립적이지만 로직상 클래스내에 포함되는 메서드에 사용
# 메서드 앞에 @staticmethod 라는 Decorator 표시

# 클래스 메서드
# 메서드 앞에 @classmethod 라는 Decorator 표시
# 정적 메서드와 비슷하지만, 객체 인스턴스 self 받는 대신 cls 라는 클래스 파라미터 받음, 클래스 변수 엑세스 가능

###############################################################################
# 클래스 상속

class country:
    name = '국가명'
    population = '인구'
    capital = '수도'
    def show(self):
        print('국가 클래스의 메소드')

class world(country):
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print('국가 이름은 ', self.name)

var1 = world('korea')
var1.show() #인스턴스 변수 존재
var1.show_name()
print(var1.capital) #인스턴스 변수 존재 안함, 입력 안했을때는 () 불필요