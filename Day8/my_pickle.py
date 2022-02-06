import pickle
# profile_file =open("profile.pickle.txt",'wb')
# profile ={"이름": '정상수','나이':30,'취미':['백발백중','명사수','자위']}
# print(profile)
# pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 저장
# profile_file.close()

profile_file =open('profile.pickle.txt','rb')
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile) 
profile_file.close()