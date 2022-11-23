print("bananas"+"frut")
a="banana".upper()
b="frut"
c=a+b
d=12
с=a+b+str(d)
c=f"banana {d}"
print(c)

val1=15.777777
print(round(val1,3))
val2=-2
val4=True
val5=False
val6=12>5
if val6:
    print("правда")
else:
    print("ложь")

val7=[1,6,2,3,]
for i in val7:
    print(i*2)

def samming(x,y):
    print(x+y)
samming(15,12)
text="Привет"
#with open("new.txt", "w") as file:
 #   file.write(text)

with open("new.txt", "r") as file:
    text=file.read()
    print(text)
