import re

# isu = 368823
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

isu = 368823
smile = f"{isu%5}{isu%4}{isu%7}"

smile_mask = "8<{("

string_set = [
    f"Between a Rock and a Hard Place {smile}",
    f"Foaming {smile} At The Mouth {smile}",
    f"It's Not {smile} Brain Surgery",
    f"Curiosity Killed {smile} The {smile} Cat {smile}"
    f"Man of {smile} Few Words"
]


# for i in string_set:
#     print(len(re.findall(string_set[i], smile)))
for i in range(len(string_set)):
    print(string_set[i])
    print(len(re.findall(smile, string_set[i])))
    print(smile, type(smile_mask))
# def function_2():



# def function_1(string: str) -> int:
#     return (len(re.findall({smile}, string_set)))




        