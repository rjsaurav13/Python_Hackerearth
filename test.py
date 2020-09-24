


i=0
num=0
ch = input()
num = len(ch)
while i<num:
     if ch[i] != "G" and ch[i] !="C" and ch[i] !="T" and ch[i] !="A":
        print("Invalid Input")
        num=1
        break
if num==1:    
    while i<num:
        if ch[i] == "G":
            print('C', end = '')
        elif ch[i] =="C":
            print('G', end = '')
        elif ch[i] =="T":
            print('A', end = '')
        elif ch[i] =="A":
            print('U', end = '')   
        i+=1
else:
    print("Invalid Input")        