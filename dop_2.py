# Вывесили списки стипендиатов текущего семестра, которые представляют из себя список людей ФИО и номер группы этого человека. Вы решили подшутить над некоторыми из своих одногруппников и удалить их из списка.
# С помощью регулярного выражения найдите всех студентов своей группы, у которых инициалы начинаются на одну и туже букву и исключите их из списка.
# Могут существовать двойные фамилии, которые тоже нужно учитывать (студенты с такими фамилиями тоже должны иметь право быть удаленными из списка стипендиатов текущего семестра).


# input
# Петров П.П. P0000 Анищенко А.А. P33113 Примеров Е.В. P0000 Иванов И.И. P0000

# output
# Анищенко А.А. P33113 Примеров Е.В. P0000
import re
group = 'P0000'
studs = {
'Петров П.П.' : 'P0000',
'Анищенко А.А.' : 'P33113',
'Примеров Е.В.' : 'P0000',
'Иванов И.И.' : 'P0000',
'Абобов В.Г.' : 'P8888',
'Бамбуб К.К.' : 'P0000'
}


# studs_string = 'Петров П.П. P0000 Анищенко А.А. P33113 Примеров Е.В. P0000 Иванов И.И. P0000'
# new_s = studs_string.split(' ')

def match(string):

    pattern_1 = '[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬ] + [йцукенгшщзфывапрболдячсмитью]+$'
    pattern_2 = '[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬЮ]'
    pattern_3 = '[QWERTYUIOPASDFGHJKLZXCVBNM] + [0987654321]'

    if re.search(pattern_1, string):
        return('pattern_1_flag')
    elif (re.search(pattern_2, string)) and (len(string) == 4):
        return('pattern_2_flag')
    elif (re.search(pattern_3, string)):
        return('pattern_3_flag')
    else:
        return(0)

def fun_1(studs):

    expell_arr = []
    retain_dict = {}

    for ls in range(len(studs)):
        new_arr_string = str(list(studs.keys())[ls]).split(' ')
        sub_arr_string = str(new_arr_string[1])

        if group != studs.get(list(studs.keys())[ls]):
            retain_dict[list(studs.keys())[ls]] = studs.get(list(studs.keys())[ls])

        if (sub_arr_string[0] != sub_arr_string[2]):
            retain_dict[list(studs.keys())[ls]] = studs.get(list(studs.keys())[ls])

        if (sub_arr_string[0] == sub_arr_string[2]) and (group == studs.get(list(studs.keys())[ls])):
            expell_arr.append(new_arr_string[0] + ' ' + new_arr_string[1])

    print('To expell:')
    for i in range(len(expell_arr)):
        print(expell_arr[i])
        
    print('To retain:')
    
    for i in range(len(retain_dict)):
        print(list(retain_dict.keys())[i], retain_dict.get(list(retain_dict.keys())[i]))
    

if __name__ == '__main__':
    try:
        print(fun_1(studs))

    except ValueError or SyntaxError:
        print('You are doing something completely wrong :)')
