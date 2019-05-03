import matplotlib.pyplot as plt

x = []
y = []

dataset = open('dataset.csv','r')

for line in dataset:
    line = line.strip()
    #separaçao da string quando detectada virgula ','
    X,Y = line.split(',')
    x.append(X)
    y.append(Y)

dataset.close()

plt.plot(x,y)

plt.title('Example')
plt.xlabel('x label')
plt.ylabel('y label')

plt.show()
