ch = input()
for j in ch:
    if j != "G" and j != "C" and j != "T" and j != "A":
        print("Invalid Input")  
        exit()
for i in ch:
    if i == "G": 
        print("C", end = '')
    elif i =="C": 
        print("G", end = '')
    elif i=="T": 
        print("A", end = '')
    else: 
        print("U", end = '')  
  