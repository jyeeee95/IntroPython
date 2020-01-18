import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class Character:
    def __init__(self, charname):
        # default setting
        self.charname = charname
        self.charlevel = 1
        self.charexp = 0
        self.classchoice = "초보자"
        self.weapon = "주먹"
        self.skill = '휘두르기'
        self.exp = 5

        self.skillset = []

    def create_char(self):
        print("\n{} 님, 당신의 레벨은 {}, 클래스는 {} 입니다.".format(self.charname, self.charlevel, self.classchoice))

    def levelup(self):
        self.charlevel += 1
        print("\n{} 님, {} 레벨이 되었습니다.".format(self.charname, self.charlevel))

        return self.charlevel

    def skillup(self, skill, exp):
         self.skill = skill
         self.exp = exp

         return skill, exp



class Warrior(Character):
    def __init__(self,Character):
        super().__init__(Character.charname)
        self.skill = "강하게 내려찍기"
        self.weapon = "대검"
        self.exp = 10
        self.classchoice = Character.classchoice
        self.charlevel = Character.charlevel

class knight(Character):
    def __init__(self,Character):
        super().__init__(Character.charname)
        self.skill = "정권찌르기"
        self.weapon = "한손검"
        self.exp = 10
        self.classchoice = Character.classchoice
        self.charlevel = Character.charlevel

class magician(Character):
    def __init__(self,Character):
        super().__init__(Character.charname)
        self.skill = "벼락치기"
        self.weapon = "스태프"
        self.exp = 10
        self.classchoice = Character.classchoice
        self.charlevel = Character.charlevel

class axler(Character):
    def __init__(self,Character):
        super().__init__(Character.charname)
        self.skill = "도끼날리기"
        self.weapon = "도끼"
        self.exp = 10
        self.classchoice = Character.classchoice
        self.charlevel = Character.charlevel




class Attack(Character):
    def __init__(self, Character, monster):
        self.charname = Character.charname
        self.weapon = Character.weapon
        self.monstername = monster
        print("\n{} 이(가) {} 를 마주쳤습니다. Σ(꒪ȏ꒪)".format(self.charname, self.monstername))

    def monsterAttack(self, Character):
        self.skill = Character.skill
        self.exp = Character.exp
        print("{} 이(가) {} 에게 {} 를 시전하였습니다. 경험치 {} 를 획득합니다.".format(self.charname, self.monstername, self.skill, self.exp))

        return self.exp



class Jump(Character):
    def __init__(self, Character):
        self.charname = Character.charname
        print("{} 이(가) 점프합니당 (ノ^o^)ノ".format(self.charname))




class setButton():
    def __init__(self):
        self.buttonset = {
        }
        self.setting = ""

    def buttonPrint(self):
        for key in self.buttonset.keys():
            print(key, " : ", self.buttonset[key])

    def buttonChoice(self, setlist):
        self.setlist = setlist
        myFunction = input("원하는 {} 의 번호를 입력하세요: ".format(self.setting))

        if int(myFunction) > 0 and int(myFunction) <= len(self.setlist):
            print("\n{} 을(를) 선택하셨습니다.".format(self.setlist[int(myFunction)]))
            pass
        else:
            raise MyError()

        return myFunction


class setFunction(setButton):
    def __init__(self):
        self.buttonset = {
              1: '전직'
            , 2: '레벨업'
            , 3: '공격'
            , 4: '점프'
            , 5: '게임종료'
        }

        self.setting = '기능'

class setClass(setButton):
    def __init__(self):
        self.buttonset = {
              1: '전사'
            , 2: '나이트'
            , 3: '매지션'
            , 4: '액슬러'
        }

        self.setting = '직업'



class MyError(Exception):
    def __str__(self):
        return "다시 입력해주세요."








if __name__ == "__main__":

    def emptyCheck(myString):
        if len(myString) > 0:
            pass
        else:
            raise MyError()


    ######

    print("\n===== G A M E   S T A R T ======\n")

    # Character Setting
    while True:
        try:
            # input Charname
            charname = input("캐릭터 명을 입력하세요: ")

            # Check Empty Value
            emptyCheck(charname)

        except MyError as e:
            print(e)
            continue

        myChar = Character(charname)
        myChar.create_char()

        print("이블린 서버에 입장했습니다.\n")
        break


    # Game Start
    while True:
        try:
            button1 = setFunction()
            button1.buttonPrint()

            try:
                myFunction = button1.buttonChoice(button1.buttonset)

                # 1. 전직하기
                if myFunction == '1':
                    button2 = setClass()
                    button2.buttonPrint()

                    try:
                        myClass = button2.buttonChoice(button2.buttonset)

                    except MyError as e:
                        print(e)
                        continue

                    myChar.classchoice = button2.buttonset[int(myClass)]
                    print("{} 님이 {} 로 전직하였습니다.".format(myChar.charname, myChar.classchoice))

                    if myClass == '1':
                        myChar = Warrior(myChar)
                        myChar.create_char()

                    elif myClass == '2':
                        myChar = knight(myChar)
                        myChar.create_char()

                    elif myClass == '3':
                        myChar = magician(myChar)
                        myChar.create_char()

                    elif myClass == '4':
                        myChar = axler(myChar)
                        myChar.create_char()

                    else:
                        print("잘못된 입력입니다.")

                # 2. 레벨업하기
                elif myFunction == '2':
                    myChar.charlevel = myChar.levelup()

                # 3. 공격하기
                elif myFunction == '3':
                    myAttack = Attack(myChar, "크로우")
                    myChar.charexp += myAttack.monsterAttack(myChar)
                    print("현재 {} 님의 경험치는 {} 입니다.".format(myChar.charname, myChar.charexp))

                # 4. 점프하기
                elif myFunction == '4':
                    myJumb = Jump(myChar)

                # 4. 종료하기
                elif myFunction == '5':
                    print("===== G A M E  E N D =====")
                    break

            except MyError as e:
                print(e)
                continue

        except:
            break
