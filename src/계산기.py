#계산기

def add(x,y):
    print(f'{x} + {y} = {x+y}')

def sub(x,y):
    print(f'{x},{y}의 차 = {float(abs(x-y))}')

def mul(x,y):
    print(f'{x} * {y} = {x*y}')

def div(x,y):
    print(f'{x} / {y} = {x/y}')

while True:
    m=input("'+','-','*','/' 중 입력, 종료하려면 q>")

    if m not in ['+','-','*','/','q']:
        print('유효한 명령을 입력하세요.')
        
    elif m=='q':
        print("종료")
        break

    else:
        a=int(input('수 입력>'))
        b=int(input('수 입력>'))

        if m=='+':
            add(a,b)
        elif m=='-':
            sub(a,b)
        elif m=='/':
            div(a,b)
        elif m=='*':
            mul(a,b)

