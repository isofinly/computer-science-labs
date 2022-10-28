import re

studs = {
    'P0000': ['Петров П.П.','Примеров Е.В.','Иванов И.И.','Бамбуб К.К.'],
    'P33113': ['Анищенко А.А.'],
    'P8888': ['Абобов В.Г.']
}
pattern = (r'[A-ZА-Я]\w+\s+(?:[A-ZА-Я]\.?\s*){2}')
pattern_2 = (r'P0000')

# regex function to get certain pattern from array of strings
# def get_pattern(pattern, arr):
#     result = []
#     for i in range(len(arr)):
#         result += re.findall(pattern, arr[i])
#     return result

print(list(studs.keys()))



# regesx function to get certain pattern from dictionary of strings
# def get_pattern_dict(dict):
#     result = {}
#     for i in range(len(dict)):
#         result[dict[i]] = re.findall(pattern_2, dict[i])
#     return result

# print(get_pattern_dict(studs))



# def get_pattern_dict(pattern, studs):
#     pattern = re.compile(r'')
#     result = []
#     for key in studs:
#         for name in studs[key]:
#             result += re.findall(pattern, name)
#     return result


# print(get_names(studs))