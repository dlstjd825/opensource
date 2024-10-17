"""
나온 단어 다시 안 나오게 / 틀리면 -5점 & 다음 라운드로 진행 / 추가점수 제도
점수제도 : 정답 10점, 오답 -5점, 7글자 이상 추가점수 5점, 5글자 이상 추가점수 3점, 총 점수 = 점수 - 걸린시간

"""

import random as r
import time as t

words=[
'숭실대학교','젠사이야','Samsung','사과','시계','맹구',
'컴퓨팅적사고와알고리즘','Python','computer', '내찜닭', '숭덕경상관', '벤처중소기업센터',
'Pizza',
]
n=1
score=0

name=input("이름을 입력하세요: ")

print("준비되면 Enter")
input()

start_time=t.time()

while n<=10:
    print(f"*******라운드 {n}*******")
    current_word=r.choice(words)
    words.remove(current_word)
    print(f"단어: {current_word}")

    user_input=input("단어를 입력하세요: ")

    if current_word == user_input:
        n+=1
        score+=10
        if len(current_word)>=7:
            print("정답입니다. 추가점수 5점")
            score+=5
        elif len(current_word)>=5:
            print("정답입니다. 추가점수 3점")
            score+=3
        else:
            print("정답입니다.")

    else:
        print("오답입니다.")
        n+=1
        score-=5

end_time=t.time()
es_time=end_time-start_time

print(f'{name}님의 타자 시간: {es_time:.2f}초 / 점수: {score-es_time:.2f}')
