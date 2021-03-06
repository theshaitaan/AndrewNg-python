import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

f = open(r'C:\Users\Hp\Desktop\Mlclass\machine-learning-ex1\ex1\ex1data1.txt','r')
x,y =zip(*[ i.split(',') for i in f.readlines()])

y = list(map( str.strip , y ))
x = [ float(i) for i in x]
y = [float(i) for i in y ]

x = np.asarray(x)
y = np.asarray(y)
x = x.reshape(len(x),1)
y = y.reshape(len(x),1)

plt.scatter(x , y , marker = 'x', label='Training data' )
plt.legend()

theta = np.array([[0],[0]])

x=np.insert( x , [0],[1],1)
iterations=1500
alpha=0.01

def computeCost(x , y , theta ):
    m = len(y)
    pred = np.dot( x , theta )
    diff = np.square( pred - y)
    cost = 1/(2*m) * (diff.sum())
    return cost

J = computeCost(x, y ,theta)
print('With theta[0,0] the value of cost is =',J)

J = computeCost(x, y ,np.array([[-1],[2]]))
print('With theta[-1,2] the value of cost is =',J)

def gradientDescent( x , y , theta , alpha , num_iters):
    import numpy as np
    m = len(y)
    J_history = np.zeros([num_iters,1])
    theta_history = np.zeros([num_iters , 2])
    
    for i in range(num_iters):
        
       x1 = x[:,1]
       x1 = x1.reshape(len(x),1)
       
       h = theta[0] + theta[1]*x1
       
       theta_0 = theta[0] - alpha * (1/m) * ((h-y).sum())
       theta_1 = theta[1] - alpha * (1/m) * (((h-y)*x1).sum())
           
       theta_history[i] = [theta_0 , theta_1]
       theta = theta_history[i]
       theta = theta.reshape(len(theta),1)
       
       J_history[i] = computeCost( x , y ,theta)
    
    minVal = J_history.min()
    
    for j in range(len(J_history)):
        if J_history[j]==minVal:
            index=j
            break
    
    return theta_history[index]
    
theta = gradientDescent( x , y , theta , alpha , iterations)
print(" Value of theta found by gradient descent is : \n" ,theta)

plt.plot( x[:,1] , np.dot(x, theta), color = 'r' , label = 'Linear Regression')
plt.legend()
plt.xlabel("Population of cities in 10k's")
plt.ylabel("Porfit in $10k's")
plt.title("Linear reg fit sample")

predict1 = np.dot([[1, 3.5]] , theta)
print("For population of 35,000, we predict a profit of " ,predict1*10000)

predict2 = np.dot([[1, 7]] , theta)
print("For population of 70,000, we predict a profit of " ,predict2*10000)

#surface plot 
#Grid over which we will calculate J
theta0_vals = np.linspace( -10 ,10 ,100)
theta1_vals = np.linspace(-1 , 4, 100)

J_vals = np.zeros([len(theta0_vals), len(theta1_vals)])

#fillin J
for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        t= np.array([[theta0_vals[i]] ,[ theta1_vals[j]]])
        J_vals[i , j] = computeCost(x , y , t)
        
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
theta0_vals , theta1_vals = np.meshgrid(theta0_vals , theta1_vals)
ax.plot_surface(theta0_vals,theta1_vals, np.transpose(J_vals) )

ax.set_xlabel("theta0")
ax.set_ylabel("theta1")

#contour plot
fig  = plt.figure()
ax   = fig.add_subplot(1,1,1)
ax.contour(theta0_vals, theta1_vals ,np.transpose(J_vals) , np.logspace( -2, 3, 20) )
plt.plot(theta[0], theta[1], marker = 'x')


'''
#Program for linear regression using sklearn

regr = linear_model.LinearRegression()
regr.fit(x,y)

plt.scatter(x , y,  marker="x")
plt.plot(x , regr.predict(x) , c='r')

print(regr.coef_)
print(regr.intercept_)
print()
'''
