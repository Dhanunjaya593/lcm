m,n = input().split()
list_m = list(map(int,m.split("/")))
list_n = list(map(int,n.split("/"))) 

a= list_m[0]
b = list_n[0] 
c= list_m[1]
d=list_n[1] 

if(c>d):
    greater = c 
else:
    greater = d 

if(greater % c == 0 ) and (greater % d == 0):
    lcm = greater 
    numrator = int(a*(lcm/c) + (b*(lcm/d)))
    
else:
    lcm = (c*d)
    numrator = int(a*d + b*c)
    

if(numrator  /lcm)<1:
    print(str(numrator)+"/"+ str(lcm))
elif(numrator % lcm)==0:
    print(int(numrator/lcm))
elif(numrator / lcm)>1:
    remiander = numrator % lcm 
    fractor = int(numrator - remiander) 
    mixed = int(numrator/lcm) 
    pert= str(remiander)+"/"+str(lcm) 
    print(str(mixed)+" " + pert)