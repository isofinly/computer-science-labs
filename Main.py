import re
import random as r

eyes = {
    0 : ":",
    1 : ";",
    2 : "X",
    3 : "8",
    4 : "="
 }
nose = {
    0 : "-",
    1 : "<",
    2 : "-{",
    3 : "<{"
}
mouth = {
    0 : "(",
    1 : ")",
    2 : "O",
    3 : "|",
    4 : "\\",
    5 : "/",
    6 : "P"
}
results = {
    0 : '1, 0',
    1 : '0, 2',
    2 : '1, 0',
    3 : '2, 1',
    4 : '1, 0'
}

isu = 368823
alphabet = "\\<>{|:;8=-()OP"
smile = f"{isu%5}{isu%4}{isu%7}" # 330
smile_mask = (eyes[3] + nose[3] + mouth[0])


string_set = [
    f"Between a Rock and a Hard Place {smile_mask}",
    f"Foaming {smile} At The Mouth {smile}",
    f"It's Not {smile_mask} Brain Surgery",
    f"Curiosity Killed {smile_mask} The {smile} Cat {smile_mask}",
    f"Man of {smile_mask} Few Words"
]
rand_string_set = [
   f'',
   f'',
   f'',
   f'',
   f''
]

def fun_1(rand_string_set):
    for i in range(5):
        a = 30
        while a > 0:
            a -= 1
            rand_string_set[i] += str(alphabet[r.randint(0,len(alphabet)-1)])
    return rand_string_set

def fun_2(string_set):
    for ss in range(len(string_set)):
        print(string_set[ss])
        if (len(re.findall(re.escape(smile_mask), string_set[ss]))):
            print("• Total " + str(smile_mask) + " in string set:", len(re.findall(re.escape(smile_mask), string_set[ss])))
        if len(re.findall(re.escape(smile), string_set[ss])):
            print("• Total " + str(smile) + " in string set:", len(re.findall(re.escape(smile), string_set[ss])))
        print('• Your resuts to compare with: ' + results[ss])
        print()

def fun_3(rand_string_set):
   fun_1(rand_string_set)
   for ss in range(5):
      print(rand_string_set[ss])
      print("• Total " + str(smile_mask) + " in string set:", len(re.findall(re.escape(smile_mask), rand_string_set[ss])))
      print()

if __name__ == '__main__':
    try:
        print(fun_2(string_set))
        print()
        print(fun_3(rand_string_set))
    except ValueError or SyntaxError:
        print('You are doing something wrong :)')