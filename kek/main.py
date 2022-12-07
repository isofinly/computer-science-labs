import sys, os, timeit
# sys.path.append(os.path.abspath("/Users/isofinly/VSC-Projects/CS-lab-4/kek"))
s1 = 'y'
s2 = 'y'

print('================= TEST 1 =================')

start1 = timeit.default_timer()


for i in range(100):
    f1 = open('./kek/input.json', 'r', encoding="utf8")
    f2 = open('./kek/out/output1.yml', 'w', encoding="utf8")

    f1test = f1.read()
    f1 = open('./kek/input.json', 'r', encoding="utf8")

    def checkBalance(str1):  
            count= 0  
            ans=False  
            for i in str1:  
                if i == "(" or i == "{" or i == "[":  
                    count += 1  
                elif i == ")" or i == "}" or i == "]":  
                    count-= 1  
                if count < 0:  
                    return ans  
            if count==0:  
                return not ans  
            return ans  
    str1=f1test   

    def a():
        try:
            newf1 = f1test.replace('"', '').replace('{', '').replace('}', '').replace('},','}').replace('],',']').replace(',\n','\n')
            f2.write(newf1)
            f2.close()
            f1.close()

        except (SyntaxError):
            print("Your JSON file is not valid")
            exit()

    if checkBalance(str1) == False:     
        print("Your JSON file has issues with parentheses or backslashes. Please fix them and try again.")
        exit()

    else:
        a()
stop1 = timeit.default_timer()
print('Test one successful')
print('Time: ', stop1 - start1)  

print('================= TEST 2 =================')

start2 = timeit.default_timer()

for i in range(100):
    import json
    import yaml

    f1 = open('./kek/input.json', 'r', encoding="utf8")
    f2 = open('./kek/out/output2.yml', 'w', encoding="utf8")

    f1test = f1.read()
    f1 = open('./kek/input.json', 'r', encoding="utf8")

    def checkBalance(str1):  
            count= 0  
            ans=False  
            for i in str1:  
                if i == "(" or i == "{" or i == "[":  
                    count += 1  
                elif i == ")" or i == "}" or i == "]":  
                    count-= 1  
                if count < 0:  
                    return ans  
            if count==0:  
                return not ans  
            return ans  
    str1=f1test   

    def b():
        yaml.dump(json.load(f1), f2, indent=2, allow_unicode=True)
        f1.close()
        f2.close()
        
    if checkBalance(str1) == False:  
        print("Your JSON file has unbalanced parentheses")
        exit()
        
    try:
        b()
        
    except (json.decoder.JSONDecodeError, ValueError, SyntaxError):
        print("Your JSON file is not valid")
        # s1 = input('do you want to ignore this error? (y/n): ')
        if s1 == 'y':
            print("Your JSON file is not valid but it does not matter because you have chosen to ignore it")
            newf1 = f1test.replace('"', '').replace('{', '').replace('}', '').replace('},','}').replace('],',']').replace(',\n','\n')
            f2.write(newf1)
            f2.close()
            f1.close()
        else:
            exit()
stop2 = timeit.default_timer()
print('Test two successful')
print('Time: ', stop2 - start2)

print('================= TEST 3 =================')

start3 = timeit.default_timer()
for i in range(100):
    import re
    jsonFile = (open('./kek/input.json', 'r', encoding="utf8").read())

    outputYml = open('./kek/out/output3.yml', 'w', encoding="utf8")



    def checkBalance(str1):  
            count= 0  
            ans=False  
            for i in str1:  
                if i == "(" or i == "{" or i == "[":  
                    count += 1  
                elif i == ")" or i == "}" or i == "]":  
                    count-= 1  
                if count < 0:  
                    return ans  
            if count==0:  
                return not ans  
            return ans  
    str1=jsonFile   
    # print("Does your JSON file have balanced parentheses:",checkBalance(str1))  

    if checkBalance(str1) == False:  
        print("Your JSON file has unbalanced parentheses")
        exit()
        
    else:
        try:
            if '\\' in jsonFile  and not('\\\\' in jsonFile):
                print("Your JSON file has issues with backslashes.")
                # s2 = input("Do you want to ignore them? (y/n): ")
                if s2 == "y":
                    newJsonFile = jsonFile.replace('\t', '').replace('\r','').replace('      ', '').replace('    ', '').replace('  ', '')             
                            # regex for json
                    jsonRegex = re.compile(r'\".*?\"|,|:|\{|\}|\[|\]|\s+')
                    # regex for yml
                    ymlRegex = re.compile(r'\".*?\"|,|:|\{|\}|\[|\]|\s+')

                    # match json and yml
                    jsonMatch = jsonRegex.findall(newJsonFile)
                    ymlMatch = ymlRegex.findall(newJsonFile)

                    # replace json with yml
                    for i in range(len(ymlMatch)):
                        newJsonFile = newJsonFile.replace(jsonMatch[i], ymlMatch[i], 1)

                    newNewJsonFile = jsonFile.replace('"', '').replace('{', '').replace('}', '').replace('},','}').replace('],',']').replace(',\n','\n')        
                    # write to output file
                    outputYml.write(newNewJsonFile)
                    outputYml.close()
                else:
                    exit()
            else:
                
                jsonRegex = re.compile(r'\".*?\"|,|:|\{|\}|\[|\]|\s+')
                # regex for yml
                ymlRegex = re.compile(r'\".*?\"|,|:|\{|\}|\[|\]|\s+')
                # match json and yml
                jsonMatch = jsonRegex.findall(jsonFile)
                ymlMatch = ymlRegex.findall(jsonFile)
                # replace json with yml
                for i in range(len(ymlMatch)):
                    jsonFile = jsonFile.replace(jsonMatch[i], ymlMatch[i], 1)
                # write to output file
                newJsonFile = jsonFile.replace('"', '').replace('{', '').replace('}', '').replace('},','}').replace('],',']').replace(',\n','\n')        
                outputYml.write(newJsonFile)
                outputYml.close()
        except (ValueError, SyntaxError):
            print("Your JSON file is not valid")
            exit()
stop3 = timeit.default_timer()
print('Test three successful')
print('Time: ', stop3 - start3)

print('================= TEST 4 =================')

start4 = timeit.default_timer()
for i in range(100):
    import pandas as pd

    f1 = open('./kek/input.json', 'r', encoding="utf8")
    f1test = f1.read()
    newF1test = f1test.replace('\t', '').replace('\n', '').replace('\r','').replace('      ', '').replace('    ', '').replace('  ', '')

    def checkBalance(str1):  
            count= 0  
            ans=False  
            for i in str1:  
                if i == "(" or i == "{" or i == "[":  
                    count += 1  
                elif i == ")" or i == "}" or i == "]":  
                    count-= 1  
                if count < 0:  
                    return ans  
            if count==0:  
                return not ans  
            return ans  
    str1=f1test   
    # print("Does your JSON file have balanced parentheses:",checkBalance(str1))  

    def d():
        if '\\' in f1test  and not('\\\\' in f1test):
            print("Your JSON file has issues with backslashes.")
        # s2 = input("Do you want to ignore them? (y/n): ")
        if s2 == "y":             
            try:
                df = pd.read_json(newF1test)
                df.to_csv('/Users/isofinly/VSC-Projects/CS-lab-4/kek/out/output4.tsv', encoding='utf-16', sep='\t', index=False)
            except (ValueError, SyntaxError, pd.errors.ParserError):
                print("Your JSON file completely is not valid")
        else:
            exit()

    if checkBalance(str1) == False:  
        print("Your JSON file has unbalanced parentheses")
        exit()
        
    else:
        d()
stop4 = timeit.default_timer()
print('Test four successful')
print('Time: ', stop4 - start4)