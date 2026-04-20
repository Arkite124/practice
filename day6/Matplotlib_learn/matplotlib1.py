import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# ax221=plt.subplot(2,2,1)
# ax222=plt.subplot(2,2,2)
# ax212=plt.subplot(2,1,2)

# ax221.scatter([1,2,3],[1,2,3])
# ax222.bar([1,2,3],[1,2,3])
# ax222.plot([1,2,3,4,5])

# plt.tight_layout()
# plt.show()

# _,ax=plt.subplots(2,3)
# for i in range(0,2):
#     for j in range(0,3):
#         ax[i,j].text(0.3,0.5,str((i,j)),fontsize=11)
# plt.show()

# # fig,ax=plt.subplots(2,3)
# grid=plt.GridSpec(2,3)
# X=np.random.randn(100)
# Y=np.random.randn(100)
# plt.subplot(grid[0,0]).scatter(X,Y)

# X=np.arange(10)
# Y=np.random.uniform(1,10,10)
# plt.subplot(grid[0,1:]).bar(X,Y)

# X=np.linspace(0,10,100)
# Y=np.cos(X)
# plt.subplot(grid[1,:2]).plot(X,Y)

# Z=np.random.uniform(0,1,(5,5))
# plt.subplot(grid[1,2]).imshow(Z)
# plt.show()

# grid=plt.GridSpec(3,3)
# X=np.random.randn(100)
# Y=np.random.randn(100)
# plt.subplot(grid[0,:3]).scatter(X,Y)

# X=[1,2,3,4,5]
# Y=[2,4,6,8,10]
# plt.subplot(grid[1,:2]).plot(X,Y)

# X=np.arange(10)
# Y=np.random.uniform(1,10,10)
# plt.subplot(grid[2,1]).bar(X,Y)

# X=np.linspace(0,10,100)
# Y=np.cos(X)
# plt.subplot(grid[2,0]).plot(X,Y)

# Z=np.random.uniform(1,9,(10,5))
# plt.subplot(grid[1:,2]).imshow(Z)
# plt.show()

# y=np.arange(3)
# years=['2010','2011','2012']
# domestic=[6801,7695,8010]
# foreign=[777,1046,1681]
# plt.barh(y,domestic,height=0.25)
# plt.barh(y-0.3,foreign,height=0.25)
# plt.yticks(y,years)
# plt.show()

# heights = np.array([
#     175, 165, 164, 164, 171, 165, 160, 169, 164, 159, 163,
#     167, 163, 172, 159, 160, 156, 162, 166, 162, 158, 167,
#     160, 161, 156, 172, 168, 165, 165, 177
# ])
# plt.hist(heights, bins=12,width=1,align='mid',cumulative=True) # 히스토그램 bins는 구간의 수
# plt.xlabel("height")
# plt.ylabel("frequency")
# plt.show()
# f1=np.random.normal(loc=0,scale=1,size=10000)
# f2=np.random.normal(loc=3,scale=0.5,size=10000)
# plt.hist(f1,bins=200,color='red',alpha=.7,label='loc=0, scale=1')
# plt.hist(f2,bins=200,color='blue',alpha=.5,label='loc=3, scale=.5')
# plt.show()

# data=norm.rvs(10.0, 3, size=1000)
# plt.hist(data,bins=20,density=True,alpha=0.6,color='b')
# mu,std=norm.fit(data)
# xmin,xmax=plt.xlim()
# x=np.linspace(xmin,xmax,100)
# p=norm.pdf(x,mu,std)
# plt.plot(x,p,'r',linewidth=2)
# plt.show()

np.random.seed(85)
data1=np.random.normal(100,10,200)
data2=np.random.normal(100,40,200)
data3=np.random.normal(80,40,200)
data4=np.random.normal(80,60,200)
plt.boxplot([data1,data2,data3,data4])
plt.show()