# # 1번
# import matplotlib.pyplot as plt
# import numpy as np
# x=list(range(1,7))
# y=[55,62,70,75,80,88]
# plt.plot(x,y)
# plt.xlabel("Week")
# plt.ylabel("Score")
# plt.title("Weekly Learning Score")
# plt.show()
# # 2번
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(8)
# y=x*3
# plt.plot(x,y,'r.-')
# plt.xlabel("Period")
# plt.ylabel("Count")
# plt.show()
# # 3번
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(8)
# y=x**2
# plt.plot(x,y)
# plt.axis([0,10,0,50])
# plt.title("y=x^2")
# plt.show()
# # 4번
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(0,8)
# y=x**2
# # print(x,y)
# plt.scatter(x,y,c="green")
# plt.title("y=x^2 scatter")
# plt.show()
# # 5번
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(0,6)
# y1=x*2
# y2=x**2
# plt.plot(x,y1,'b',label='y=2x')
# plt.plot(x,y2,'r--',label='y=x^2')
# plt.legend(loc='upper left')
# plt.title("Two Functions")
# plt.show()
# # 6번
# import matplotlib.pyplot as plt
# import numpy as np
# t=np.arange(0,6)
# y1=t
# y2=t**2
# y3=t**3
# plt.plot(t,y1,'b',label='y=t')
# plt.plot(t,y2,'m',label='y=t^2')
# plt.plot(t,y3,'g',label='y=t^3')
# plt.grid()
# plt.legend(loc='upper left')
# plt.title("Two Functions")
# plt.show()
# # 7번
# import matplotlib.pyplot as plt
# import numpy as np
# t=np.arange(0,6)
# y1=t
# y2=t**2
# y3=t**3
# plt.plot(t,y1,'b',label='y=t')
# plt.plot(t,y2,'m',label='y=t^2')
# plt.plot(t,y3,'g',label='y=t^3')
# plt.grid()
# plt.legend(loc='upper left')
# plt.title("Two Functions")
# plt.show()
# # 8번
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.linspace(0,2*np.pi)
# y2=np.cos(x)
# y1=np.sin(x)
# plt.plot(x,y1,'r',label='sin')
# plt.plot(x,y2,'b:',label='cos')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend(loc='upper right')
# plt.title("Sin & Cos Graph")
# plt.show()
# # 9번 
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(0,6)
# y1=x**2
# y2=x*3
# fig,ax=plt.subplots(2,2)
# ax[0]=plt.subplot(1,2,1).scatter(x,y1,c='b')
# ax[0]=plt.title("y=x^2")
# ax[1]=plt.subplot(1,2,2).plot(x,y2,'g')
# ax[1]=plt.title("y=3x")
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi)
y1=np.sin(x)
y2=np.cos(x)
fig,ax=plt.subplots(2,2)
ax[0]=plt.subplot(2,1,1).plot(x,y1,'r--',label='sin')
ax[0]=plt.title("Sin Function")
ax[0]=plt.legend(loc='upper right')
ax[0]=plt.grid()
ax[1]=plt.subplot(2,1,2).plot(x,y2,label='cos')
ax[1]=plt.title("Cos Function")
ax[1]=plt.legend(loc='lower left')
ax[1]=plt.grid()
plt.savefig("graph")
plt.tight_layout()
plt.show()