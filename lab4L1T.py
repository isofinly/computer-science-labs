f1 = open('input.json', 'r', encoding="utf8")
f2 = open('output1.yml', 'w', encoding="utf8")
buffer = ""
s = ''
arr = []
for line in f1:
    s = line
    for i in range(1, len(s)):
        if '[' in s:
            while ']' in s:
                arr.append(s[i])
                break
        if s[i] != '"' and s[i] != '{' and s[i] != '}' and '},' not in s :
            buffer = buffer + s[i]
            buffer = buffer.replace('[', '').replace(']', '')
# newA = ' '.join(arr).replace(' ', '').replace('\n','*').split('*')
# newA = (str(newA[0])[10:-2]).replace(',', '')
# print(list(newA))
f2.write(buffer)
f1.close()
f2.close()