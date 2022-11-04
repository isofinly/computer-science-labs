f1 = open('input.json', 'r', encoding="utf8")
f2 = open('output1.yml', 'w', encoding="utf8")

f1test = f1.read()
f1 = open('input.json', 'r', encoding="utf8")

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