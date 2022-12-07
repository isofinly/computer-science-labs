import re
jsonFile = (open('input.json', 'r', encoding="utf8").read())
outputYml = open('output3.yml', 'w', encoding="utf8")


f1 = open('input.json', 'r', encoding="utf8")
f1test = f1.read()

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

if checkBalance(str1) == False:  
    print("Your JSON file has unbalanced parentheses")
    exit()
    
else:
    print("Your JSON file has balanced parentheses")
    jsonMatch = r'{|},|\[|\],|]|}|\"'
    jsonFile_new = re.sub(jsonMatch, '', str(jsonFile))
    outputYml.write(jsonFile_new)
    outputYml.close()