


i=0
num=0
ch = input()
num = len(ch)
while i<num:
    if ch[i] != "G" and ch[i] !="C" and ch[i] !="T" and ch[i] !="A":
        print("Invalid Input")
        num=1
        break
    if ch[i] == "G" and num==1:
        print('C', end = '')
    elif ch[i] =="C" and num==1:
        print('G', end = '')
    elif ch[i] =="T" and num==1:
        print('A', end = '')
    elif ch[i] =="A" and num==1:
        print('U', end = '')   
    i+=1