# import pandas as pd

# f1 = open('./kek/input.json', 'r', encoding="utf8")
# # f2 = open('./kek/out/output4.tsv', 'w+', encoding="utf8")
# f1test = f1.read()
# newF1test = f1test.replace('\t', '').replace('\n', '').replace('\r','').replace('      ', '').replace('    ', '').replace('  ', '')

# def checkBalance(str1):  
#         count= 0  
#         ans=False  
#         for i in str1:  
#             if i == "(" or i == "{" or i == "[":  
#                 count += 1  
#             elif i == ")" or i == "}" or i == "]":  
#                 count-= 1  
#             if count < 0:  
#                 return ans  
#         if count==0:  
#             return not ans  
#         return ans  
# str1=f1test   
# # print("Does your JSON file have balanced parentheses:",checkBalance(str1))  

# def d():
#     if '\\' in f1test  and not('\\\\' in f1test):
#         print("Your JSON file has issues with backslashes.")
#     s2 = input("Do you want to ignore them? (y/n): ")
#     if s2 == "y":             
#         try:
#             df = pd.read_json(newF1test)
#             df.to_csv('./kek/out/output4.tsv', encoding='utf-16', sep='\t', index=False)
#             # f2.close()
#         except (ValueError, SyntaxError, pd.errors.ParserError):
#             print("Your tsv file completely is not valid")
#     else:
#         exit()

# if checkBalance(str1) == False:  
#     print("Your JSON file has unbalanced parentheses")
#     exit()
    
# else:
#     d()
#     # f2.close()

# import json, csv
# import pandas as pd
# try:
#     f2 = open('./kek/out/output4_4.tsv', 'w', encoding="utf16")
#     with open('./kek/input.json', encoding='utf-8') as inputfile:
#         inputfile.read()
#         df = json.dumps(inputfile)
#         print(df)

#     df.to_csv('./kek/out/csvfile.csv', encoding='utf-16', index=False, sep='\t')
#     with open('./kek/out/csvfile.csv', encoding='utf-16') as file: 
#         file = file.read()
#         newFile = file.replace('[','').replace(']','')
#         f2.write(newFile)
#         f2.close()
        
 
# except (json.decoder.JSONDecodeError, SyntaxError, ValueError, KeyError):
#     print("Your JSON file is not valid")

import json, csv
js = json.loads(open('./kek/input.json',encoding='utf8').read())
wr = csv.writer(open('./kek/out/csvfile.csv','w+',encoding='utf16'),delimiter=',',skipinitialspace=False,lineterminator='\n')
headers = []
for x in js:
    headers.append(x)
columns = ['']+list(js[headers[0]].keys())
wr.writerow(columns)
for i in range(len(headers)):
    t = [headers[i]]
    for j in range(1,len(columns)):
        t.append(js[headers[i]][columns[j]])
    wr.writerow(t)
