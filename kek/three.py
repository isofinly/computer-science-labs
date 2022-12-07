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
            s2 = input("Do you want to ignore them? (y/n): ")
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