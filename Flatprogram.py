list=[[1,2],[2,3],[3,4]]
flat=[]
for i in list:
    for j in i:
        flat.append(j)

print("The flatted list",flat)