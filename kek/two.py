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
    s1 = input('do you want to ignore this error? (y/n): ')
    if s1 == 'y':
        print("Your YAML file is not valid but it does not matter because you have chosen to ignore it")
        newf1 = f1test.replace('"', '').replace('{', '').replace('}', '').replace('},','}').replace('],',']').replace(',\n','\n')
        f2.write(newf1)
        f2.close()
        f1.close()
        # f3 = open('./kek/input.json', 'r', encoding="utf8").read()
        # newF3 = f3.replace('\t', '').replace('\n', '').replace('\r','').replace('      ', '').replace('    ', '').replace('  ', '')
        # f2 = open('./kek/out/output2.yml', 'w', encoding="utf8")
        # f2.write(newF3)
        # f2.close()
    else:
        exit()