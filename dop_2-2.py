import re

studs = {
'Петров П.П.' : 'P0000',
'Анищенко А.А.' : 'P33113',
'Примеров Е.В.' : 'P0000',
'Иванов И.И.' : 'P0000',
'Абобов В.Г.' : 'P8888',
'Бамбуб К.К.' : 'P0000'
}

def fun_1(studs):

    pattern_4 = r'\w* [ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬЮЁ]\.[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬЮЁ]\.'
    pattern_5 = r'[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬЮЁ]\.[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬЮЁ]\.'
    pattern_6 = r'^\w*'
    pattern_7 = r'^\w[0]*$'
    # ^[QWERTYUIOPASDFGHJKLZXCVBNM]\d\d\d\d

    retain_arr = []
    emtpy_arr = []
    idk_what_to_call = []
    idk_what_to_call_2 = []
    idk_what_to_call_3 = []
    new_var_2 = []
    
    for ls in range(len(studs)):
        emtpy_arr += (re.findall(pattern_4, (list(studs.keys()))[ls]))

    for ls in range(len(emtpy_arr)):
        idk_what_to_call += (re.findall(pattern_5, (emtpy_arr[ls])))
        idk_what_to_call_2 += (re.findall(pattern_6, (emtpy_arr[ls])))

    for i1 in range(len(idk_what_to_call)):
        if (idk_what_to_call[i1][0] == idk_what_to_call[i1][2]):
            retain_arr.append((idk_what_to_call_2[i1] + ' ' + idk_what_to_call[i1]))
    # print('ra',retain_arr)
    
    for ls in range(len(studs)):
        idk_what_to_call_3.append(list(studs.values())[ls])

    newvar = str(re.findall(pattern_7, list(studs.values())[ls])[0])
    new_set = set(studs.values())
    new_new_list = list(new_set)

    for ls in range(len(new_set)):
        if new_new_list[ls] != newvar:
            new_var_2.append(new_new_list[ls])

    value = []
    for ls in range(len(new_var_2)):
        value += [i for i in studs if studs[i] == new_var_2[ls]]

    # print('value', value)
    # print('Retain: ', retain_arr)
    # print('before', studs)
    for ls in range(len(value)):
        if value[ls] in retain_arr:
            # print('yes', value[ls])
            retain_arr.remove(value[ls])
    for ls in range(len(retain_arr)):
        studs.pop(retain_arr[ls])
    print(studs)
    
if __name__ == '__main__':
    try:
        (fun_1(studs))

    except ValueError or SyntaxError:
        print('You are doing something completely wrong :)')
