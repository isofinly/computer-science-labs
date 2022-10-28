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
string_set = [
   f'',
   f'',
   f'',
   f'',
   f''
]

isu = 368823
alphabet = "\\<>{|:;8=-()OP"
# alphabet = "8<{("
smile = f"{isu%5}{isu%4}{isu%7}"
smile_mask = (eyes[3] + nose[3] + mouth[0])

# smile_mask = '8<{('
# string_set[2] += '(8<{()()'

def fun_1(string_set):
   for i in range(5):
      a = 30
      while a > 0:
         a -= 1
         string_set[i] += str(alphabet[r.randint(0,len(alphabet)-1)])
   return string_set
         
def fun_2(string_set):
   fun_1(string_set)
   for ss in range(5):
      print(string_set[ss])
      print(len(re.findall(re.escape(smile_mask), string_set[ss])))

print(fun_2(string_set))
   # print(re.escape(smile_mask), type(smile_mask))