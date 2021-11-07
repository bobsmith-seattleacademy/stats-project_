f = open("my.txt", "r")
h = f.read().split()
f.close()

mydict = {}

for line in h:
    (x,y) = line.split(",")
    if y not in mydict:
        mydict.update({y:(0,0)})
    if x == '1':
        i = mydict[y]
        mydict.update({y:(i[0]+1,i[1]+1)})
    else:
        i = mydict[y]
        mydict.update({y:(i[0],i[1]+1)})


for key in mydict:
    i = mydict[key]
    mydict.update({key:(i[0]/i[1])})
print(mydict)

f = open("new.txt","w")
for key in mydict:
    f.write("{},{}\n".format(key,mydict[key]))
    
    
