import re

s = 'Студент Вася вспомнил, что на своей лекции Балакшин П.В. упоминал про старшекурсников, которые будут ему помогать: Анищенко А.А. и Машина Е.А.'
# Дан текст. Требуется найти в тексте все фамилии, отсортировав их по алфавиту.
# Фамилией для простоты будем считать слово с заглавной буквой, после которого идут инициалы.

new_s = s.split(' ')

def match(string):

	pattern_1 = '[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬ]+[йцукенгшщзфывапрболдячсмитью]+$'
	pattern_2 = '[ЙЦУКЕНГШЩЗФЫВАПРБОЛДЯЧСМИТЬЮ]'

	if re.search(pattern_1, string):
		return('pattern_1_flag')
	elif (re.search(pattern_2, string)) and (len(string) == 4):
		return('pattern_2_flag')
	else:
		return(0)

def fun_1(new_s):
	str_dict = {}
	for i in range(len(new_s)-1):
		if (match(new_s[i]) == 'pattern_1_flag') and (match(new_s[i+1]) == 'pattern_2_flag'):
			str_dict[new_s[i]] = new_s[i+1]

	for ls in range(len(list(str_dict.keys()))):
		print(list(str_dict.keys())[ls])

if __name__ == '__main__':
    try:
        print(fun_1(new_s))
    except ValueError or SyntaxError:
        print('You are doing something completely wrong :)')
