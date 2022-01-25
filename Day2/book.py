class BookReader():
    name ='정상수'
    def read_book(self):
        print(self.name,'는 책을 읽는다')

reader =BookReader()
reader.name = '정상수'
print(reader.read_book())

reader =BookReader()
reader.name='정상수'
print(reader.read_book())

class BookReader():
    
    def __init__(self,name):
        self.name =name
    
    def read_book(self):
        print(self.name,'님은 책을 읽는다')
        reader =BookReader('박찬우')
        print(reader.read_book())
        
