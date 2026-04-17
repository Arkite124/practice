import numpy as np
import matplot as mpl
import matplotlib.pyplot as plt

# plt.title('y=x')
# plt.ylabel('y label')
# plt.xlabel('x label')
# plt.plot(list(range(0,12)))
# plt.show()

plt.title('y=x^2')
x=np.arange(-20,21)
y1=2*x
y2=(1/3)*x**2+5
y3=-x**2-5
plt.plot(x,y1,'g--',x,y2,'r^-',x,y3,'b*:')
# axis , 범위 결정
plt.axis([-30,30,-30,30])
plt.show()