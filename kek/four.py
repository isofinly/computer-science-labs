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
    s2 = input("Do you want to ignore them? (y/n): ")
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