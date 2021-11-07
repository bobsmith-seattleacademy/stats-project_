f = open("my.txt", "r")
h = f.read().split()
f.close()

def myround(x, base=20):
    return base * round(x/base)

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

newdict = {}
highest = None
lowest = None
for key in mydict:
    if lowest == None:
        lowest = int(key)
    if highest == None:
        highest = int(key)
    if int(key) > highest:
        highest = int(key)
    if int(key) < lowest:
        lowest = int(key)

for i in range(myround(lowest)-20,myround(highest)+20+1,20):
    newdict.update({i:(0,0)})



for key in mydict:

    i = newdict[int(myround(float(key),20))]
    newdict.update({myround(float(key),20):(i[0]+mydict[key][0],i[1]+mydict[key][1])})
print(newdict)
input()

for key in newdict:
    i = newdict[key]
    try:
        newdict.update({key:(i[0]/i[1])})
    except ZeroDivisionError:
        newdict.update({key:0})
    
print(newdict)

f = open("new.txt","w")
for key in newdict:
    f.write("{},{}\n".format(key,newdict[key]))
    
    
