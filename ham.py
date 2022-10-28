import random

def fun_0_5(s):
    if (len(s)!=7 and s.count('1')+s.count('0')!=7):
        print('Партия не понимать, что ты сказать')
        return False
    return True
    
def fun_1(s):
    new_s = ''
    fun_0_5(s)
    s1 = 0
    for i in range(0,len(s),2):
        s1+=int(s[i])
        
    s1 = s1%2
    s2 = sum(map(int, [s[1],s[2],s[5],s[6]]))%2
    s3 = sum(map(int, [s[3],s[4],s[5],s[6]]))%2
    
    k = int(str(s3)+str(s2)+str(s1),2)

    if k == 0:
        print('Партия гордиться тебе, ошибок не найдено')
    else:
        print('Вы разочаровать партия в месте '+str(k))
    print('Партия сообщить, что надо было: ', end='')
        
    if k!=3:
        print(s[2],end='')
    else:
        print(int(not(bool(s[2]))),end='')
    
    for i in range(5,8):
        if k != i:
            new_s += str(s[i-1])
            
        else: 
            new_s += str(int(not(bool(s[i-1]))))
    print(new_s)



s = input('Партия требует 7 бит кода:\n')
if __name__ == '__main__':
    try:
        fun_0_5(s)
        fun_1(s)
    except ValueError or IndexError:
        socialCredits = random.randint(100,1000)
        print(f'Ну и ну вы окончательно разочаровать партия -{socialCredits} social credits')
