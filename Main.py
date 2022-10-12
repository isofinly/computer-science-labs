import re

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
# string_set = [
#    f'',
#    f'',
#    f'',
#    f'',
#    f''
# ]

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


def fun_2(string_set):
   for ss in range(len(string_set)):
      print(string_set[ss])
      print("Total " + str(smile_mask) + " in string set:", len(re.findall(re.escape(smile_mask), string_set[ss])))
      print("Total " + str(smile) + " in string set", len(re.findall(re.escape(smile), string_set[ss])))

print(fun_2(string_set))