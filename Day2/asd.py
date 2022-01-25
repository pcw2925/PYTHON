def hello():
    name =input("이름이 무엇인가요?")
    print(hello)
    hello()
    
def hello(name):
    print(name,'님 반갑습니다')
    hello("정상수")
    
def hello(name,gretting):
    print(name, '님',gretting)
    hello("정상수,"'반갑다')
    
def add_suffix(name):
    return name +'님'
print(add_suffix('정상수'))

name_with_suffix =add_suffix('정상수')
print(name_with_suffix)


def sum(a,b):
    return a +b
print(sum(3,5))
print(sum(115,43))
