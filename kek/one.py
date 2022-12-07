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
# print("Does your JSON file have balanced parentheses:",checkBalance(str1))  

# symbols in line of file
# def a_a():
#     try:
#         f2 = open('./kek/out/output1.yml', 'w', encoding="utf8")
#         # newF1test = f1test.replace('\t', '').replace('\n', '').replace('\r','').replace('      ', '').replace('    ', '').replace('  ', '')        
#         f2.write(newF1test)
#         f2.close()
#         f1.close()
#     except (SyntaxError):
#         print("Your JSON file is not valid")
#         exit()
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
    # s1 = input("Do you want to check your JSON more precisely? (y/n): ")
    # if s1 == "y":
    #     if '\\' in f1test  and not('\\\\' in f1test):
    #         print("Your JSON file has issues with backslashes.")
    #         s2 = input("Do you want to ignore them? (y/n): ")
    #         if s2 == "y":             
    #             # a_a()
    #             a()
    #         else:
    #             a()
    #             exit()
    #     # a_a()
    #     a()
    # else:
    #     a()