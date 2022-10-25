import re

findByGroup_indexList = []
personArray = []
studs = {
    'P0000': ['Петров П. П.','Примеров Е.В.','Иванов И.И.','Бамбуб К.К.'],
    'P33113': ['Анищенко А.А.','Господибоже А.А.','Гдеденьги Д. Б.'],
    'P8888': ['Абобов В.Г.','Почему Б.А.','Кекус ОЧ',]

    # "P0000" : ['Петров П.П.', 'Примеров Е.В.', 'Иванов И.И.'],
    # "P33113": ["Анищенко А.А."]
}
group_pattern = r'[A-ZА-Я]\.?.[A-ZА-Я]\.'
group_pattern_3 = r'([А-Я].)\1{1}'
# group_pattern_2 = r'[а-яА-Я]*.([А-Я].).\1{1}'
pattern_2 = r'P0000' # edit this regex to choose a group


keyslist  = list(studs.keys())
for i in range(len(keyslist)):
    keyslist[i] = re.findall(pattern_2, keyslist[i])
    if keyslist[i]:
        findByGroup = (list(studs[keyslist[i][0]]))

for i in range(len(findByGroup)):
    findByGroup[i] = findByGroup[i].replace(' ','&',1).replace(' ','',1)
    if not(re.findall(group_pattern_3, list(findByGroup)[i])) and re.findall(group_pattern, list(findByGroup)[i]):
        findByGroup_indexList.append(i)
    findByGroup[i] = findByGroup[i].replace('&',' ',1)

for i in range(len(studs)-1):
    if (re.findall(pattern_2, list(studs.keys())[i])):
        studs.pop(list(studs.keys())[i])

for i in range(len(findByGroup_indexList)):
    personArray.append(findByGroup[findByGroup_indexList[i]])
    studs.update({str(pattern_2) : personArray})

print(studs)
