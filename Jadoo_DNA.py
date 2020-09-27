i=0
temp = 0
ch = input()
num = len(ch)
if ch[i] != "G" and ch[i] !="C" and ch[i] !="T" and ch[i] !="A":
    print("Invalid Input")
    temp = 1
    quit()
    
else:       
    while i<num:
        
        if ch[i] == "G" and temp == 0:
            print('C', end = '')
        elif ch[i] =="C" and temp == 0:
            print('G', end = '')
        elif ch[i] =="T" and temp == 0:
            print('A', end = '')
        elif ch[i] =="A" and temp == 0:
            print('U', end = '')  
        i+=1