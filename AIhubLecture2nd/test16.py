import matplotlib.pyplot as plt

#plt.plot([1,2,3,4],[1,4,9,16],'ro')
#plt.axis([0,6,0,20])
#plt.show()

"""
listx = []
listy = []

for i in range(0,10):
    listx[i] = i
    listy[i] = i*i

plt.plot(listx,listy)

plt.show()
"""
"""
#dictionary data를 들고오기

dic = {'data_x' : [1,2,3,4,5], 'data_y':[2,3,5,10,8]}
plt.plot('data_x','data_y',data=dic, label = 'price($)')
plt.xlabel('X-axis', loc= "right", labelpad= 15)
plt.ylabel('Y-axis', loc= "top", labelpad= 20)
plt.legend()
plt.show()


"""

a1 = [1,2,3,4]
b1 = [2,3,5,10]

a2 = [1,2,3,4]
b2 = [3,5,9,7]

plt.plot(a1,b1, label = 'price($)')
plt.plot(a2,b2, label = 'demand($)')

plt.xlabel('X-axis', loc= "right", labelpad= 15)
plt.ylabel('Y-axis', loc= "top", labelpad= 20)
plt.legend(loc = 'best', ncol=2)
plt.show()
