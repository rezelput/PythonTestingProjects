import matplotlib.pyplot as plt

print("X1: ",end="")
x1 = int(input())

print("X2: ",end="")
x2 = int(input())

print("Y1: ",end="")
y1 = int(input())

print("Y2: ",end="")
y2 = int(input())

dx = x2-x1
dy = y2-y1

if abs(dx)>abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)

xincrmnt = dx/steps
yincrmnt = dy/steps
i = 0


xcordinate = []
ycordinate = []
print("|-----------------------------------|")
while i<steps:
    i+=1
    x1 = x1 + xincrmnt
    y1 = y1 + yincrmnt
    print("| X1: ",x1,"|","Y1: ",y1)
    print("|-----------------------------------|")
    xcordinate.append(x1)
    ycordinate.append(y1)

plt.plot(xcordinate,ycordinate)
plt.xlabel('X-Ось')
plt.ylabel('Y-Ось')

plt.title("DDA")
plt.show()
