import sys, os, timeit
sys.path.append(os.path.abspath("/Users/isofinly/VSC-Projects/CS-lab-4"))

# from lab4L1T import firstParser
# from lab4LET2 import lab4LET2 
# from lab4LET3 import lab4LET3 
# from lab4LET4_1 import lab4LET4_1

print('================= TEST 1 =================')

start1 = timeit.default_timer()
for i in range(100):
    
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
    
stop1 = timeit.default_timer()
print('Test one successful')
print('Time: ', stop1 - start1)  


print('================= TEST 2 =================')

start2 = timeit.default_timer()
for i in range(100):
    
    import json
    import yaml
    with open('input.json', 'r', encoding="utf8") as f:
        data = json.load(f)
        with open('output2.yml', 'w', encoding="utf8") as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
            
stop2 = timeit.default_timer()
print('Test two successful')
print('Time: ', stop2 - start2)


print('================= TEST 3 =================')

start3 = timeit.default_timer()
for i in range(100):
    
    import re
    jsonFile = (open('input.json', 'r', encoding="utf8").read())
    outputYml = open('output3.yml', 'w', encoding="utf8")

    jsonMatch = r'{|},|\[|\],|]|}|\"'
    jsonFile_new = re.sub(jsonMatch, '', str(jsonFile))
    outputYml.write(jsonFile_new)
    outputYml.close()
    
stop3 = timeit.default_timer()
print('Test three successful')
print('Time: ', stop3 - start3)

print('================= TEST 4 =================')

start4 = timeit.default_timer()
for i in range(100):
    
    import pandas as pd
    with open('input.json', encoding='utf-8-sig') as f_input:
        df = pd.read_json(f_input)
    df.to_csv('output4.csv', encoding='utf-16', sep='\t', index=False)
    
stop4 = timeit.default_timer()
print('Test four successful')
print('Time: ', stop4 - start4)