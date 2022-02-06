# # 마린
# name ='마린'
# hp =40
# damage =5

# print("{} 유닛이 생성되었습니다".format(name))
# print("체력 {0}, 공격력{1} \n".format(hp,damage))

# tank_name ='땅크'
# tank_hp =150
# tank_damage =35

# print("{0} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력{1}\n ".format(tank_hp,tank_damage))


# tank2_name ='땅크2'
# tank2_hp =150
# tank2_damage =35

# print("{0} 유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0}, 공격력{1}\n ".format(tank2_hp,tank2_damage))


# def attack(name,location,damage):
#     print("{0} :{1} 방향으로 적군을 공격합니다.[공격력{2}]".format ( \
#         name,location,damage))
    
    
# attack(name,"1시",damage)
# attack(tank_name,'1시',tank_damage)
# attack(tank2_name,'1시',tank2_damage)

# 일반유닛 
# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name= name
#         self.hp =hp
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0} ,공격력{1}".format(self.hp,self.damage))
        
# marin1 = Unit('마린',40 ,5)
# # marin2 = Unit('마린',40 ,5)
# # tank =Unit('탱크',150,35)


# # 맴버 변수
# # 클래스 내에서 정의된 변수 

# # 레이스
# wraith1 =Unit("레이스",80,5)
# print("유닛 이름 :{0},공격력:{1}".format(wraith1.name,wraith1.damage))
# wraith1.clocking =True

# wraith2 = Unit('레이스',80,5)
# wraith2.clocking =True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))
    
# 메소드
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 상속받을 때 '클래스명(상속받을 클래스명)'
# 공격 유닛


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)  # 부모에게 값을 넘겨주어 초기화하는 작업.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]".format(
            self.name, location, self.damage
        ))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날수 있는 기능을 가진 클래스


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]"
              .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)


# 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 7, 6)
valkyrie.fly(valkyrie.name, '3시')


# 메딕 : 의무병 (공격력 : 0 / 없음)

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("정상수뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# # 다중상속
