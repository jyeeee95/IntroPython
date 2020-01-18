## 클래스와 상속 이해하기

- 클래스(Class) : 반복되는 불필요한 소스코드를 최소화 하면서 현실 세계의 사물을 컴퓨터 프로그래밍 상에서 쉽게 표현할 수 있도록 해주는 프로그래밍 기술
- 인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이요할 수 있게 만든 변수
- 클래스의 멤버 : 클래스 내부에 포함되는 변수
- 클래스의 함수 : 크래스 내부에 포함되는 함수, 메소드



~~~python
class Car:
  # 클래스의 생성자
	def __init__(self, name, color):
		self.name = name # 클래스의 멤버
		self.color = color #클래스의 멤버
  
  # 클래스의 소멸자
  def __del__(self):
    print("인스턴스를 소멸시킵니다.")
  
  #클래스의 메소드
  def show_info(self):
    print("이름:", self.name, "/ 색상:", self.color)
    
    
  # Setter 메소드: 이름을 바꾸기 위해 사용
  def set_name(self, name):
    self.name = name # 매개변수를 바꿈
    

# 인스턴스 할당
car1 = Car("소나타", "빨간색")

# 메소드 불러오기
car1.show_info()

# 이름만 출력하고 싶다면?
print(car1.name, "을(를) 구매했습니다!")
# 출력; 소나타 을(를) 구매했습니다!

# 매개변수 바꾸려면
car1.set_name("아반떼")
print(car1.name, "을(를) 구매했습니다!")
# 출력; 아반떼 을(를) 구매했습니다!

# 메모리 상에서 해당 인스턴스를 할당 해제
del car1
# 이후로는 car1에 접근 불가능

~~~





- 상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
  - 불필요한 소스코드의 작성을 줄일 수 있다!
  - 부모와 자식 관계가 존재
  - 자식 클래스 : 부모 클래스를 상속 받은 클래스



~~~python
class Unit:
	def __init__(self, name, power):
		self.name = name
		self.power = power
	
	def attack(self):
		print(self.name, "이(가) 공격을 수행합니다 [전투력:", self.power, "]")
		

class Monster(Unit):
  # Unit class의 def를 모두 받아서 사용 가능
  def __init__(self, name, power, type):
    self.name = name
    self.power = power
    self.type = type
    
  def show_info(self):
    print("몬스터 이름:", self.name, "/ 몬스터 종류:", self.type)
    
    
unit = Unit("홍길동", 375)
unit.attack()
# 출력; 홍길동 이(가) 공격을 수행합니다 [전투력: 375]

monster = Monster("슬라임", "10", "초급")
monster.attack()
# 출력; 슬라임 이(가) 공격을 수행합니다 [전투력: 10]
# 부모 클래스에 생성된 함수를 재작성하지 않아도 사용 가능

monster.show_info()
# 출력; 몬스터 이름: 슬라임 / 몬스터 종류: 초급

~~~



