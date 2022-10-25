f1 = open('input.json', 'r', encoding="utf8")
f2 = open('output.yml', 'w', encoding="utf8")
buffer = ""
s = ''
for line in f1:
    s = line
    for i in range(1, len(s)):
        if s[i] != '"' and s[i] != '{' and s[i] != '}' and '},' not in s :
            buffer = buffer + s[i]
f2.write(buffer)
f1.close()
f2.close()