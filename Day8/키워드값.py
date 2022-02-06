# def profile(name,age ,main_lang):
#     print(name,age,main_lang)
    
# profile(name="정상수", main_lang='python',age=20)
# profile(main_lang='자바',age=25,name='정상수')


# # 가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0} \t 나이:{1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name,age,*language):
    print("이름: {0} \t 나이:{1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang,end=" ")
    print()


profile('유재석',20,'python','java','C','C++','C#','자위')
profile('정상수',25,'백발백중','백발백중','','','')

