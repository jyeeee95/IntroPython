import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Character :
    def __init__(self,charname):
        #인스턴스 변수에 값 할당
        self.level = 1
        self.charname = charname
        self.classchoice = "초보자"
        self.weapon="주먹"
    def create_char(self):
        print("{} {} 캐릭터가 생성되었습니다. 레벨은 {} , 클래스는 {} 입니다.".format(self.classchoice,self.charname,self.level,self.classchoice))
    def levelup(self) :
        self.level += 1
        print("{} {} 캐릭터가 {}레벨이 되었습니다.".format(self.classchoice,self.charname,self.level))
    def attack(self):
        print("{} {} 캐릭터가 {} 으로 공격합니다!!!".format(self.classchoice,self.charname,self.weapon))
    def jump(self):
        print("{} {} 캐릭터가 점프합니당 ~ ".format(self.classchoice,self.charname))

class Warrior(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "전사"
        self.skill = "강하게 내려찍기"
        self.weapon = "대검"
        self.level = character.level
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
    def attack(self):
        print("{} {} 캐릭터가 {} 으로 {} 스킬을 시전합니다!!!".format(self.classchoice,self.charname,self.weapon,self.skill))

class knight(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "나이트"
        self.skill = "정권찌르기"
        self.weapon = "한손검"
        self.level = character.level
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
    def attack(self):
        print("{} {} 캐릭터가 {} 으로 {} 스킬을 시전합니다!!!".format(self.classchoice,self.charname,self.weapon,self.skill))

class magician(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "매지션"
        self.skill = "벼락치기"
        self.weapon = "스태프"
        self.level = character.level
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
    def attack(self):
        print("{} {} 캐릭터가 {} 으로 {} 스킬을 시전합니다!!!".format(self.classchoice,self.charname,self.weapon,self.skill))

class axler(Character):
    def __init__(self,character):
        super().__init__(character.charname)
        self.classchoice = "액슬러"
        self.skill = "도끼날리기"
        self.weapon = "도까"
        self.level = character.level
        print("{} 캐릭터가 {} 로 전직하였습니다!!".format(self.charname,self.classchoice))
    def attack(self):
        print("{} {} 캐릭터가 {} 으로 {} 스킬을 시전합니다!!!".format(self.classchoice,self.charname,self.weapon,self.skill))


print("======게임 시작!======")
charname = str(input("캐릭터명을 입력하세요: "))
char = Character(charname)
char.create_char()

while True:
    print("1. 전직하기")
    print("2. 레벨업")
    print("3. 공격하기")
    print("4. 점프하기")
    print("Z : 게임 종료 ")
    a=str(input("원하는 기능을 선택하세요: "))
    if a=='1':
        print("1. 전사")
        print("2. 나이트")
        print("3. 매지션")
        print("4. 액슬러")
        b=str(input("원하는 클래스를 선택하세요: "))
        if b=='1':
            char=Warrior(char)
            char.create_char()
        elif b=='2':
            char = knight(char)
            char.create_char()
        elif b=='3':
            char = magician(char)
            char.create_char()
        elif b=='4':
            char = Warrior(char)
            char.create_char()
    elif a=='2':
        char.levelup()
    elif a=='3':
        char.attack()
    elif a=='4':
        char.jump()
    elif a=='Z' or a=='z':
        print("======게임종료======")
        break
