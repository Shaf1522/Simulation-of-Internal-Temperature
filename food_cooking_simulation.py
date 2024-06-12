import os
import numpy as np
import matplotlib.pyplot as plt
import pdb
L=0.15
H=0.025
k=0.418
rho = 840
cp = 3810

Tcooking = 100
Tinitial=23.1
Nx=30
Ny=30

deltax=L/Nx
deltay=H/Ny

Ntime = 1000

alpha = k/(rho*cp)


tfinal = 1800
deltat=tfinal/Ntime

T_old=Tinitial*np.ones((Nx,Ny))

for i in range(0,Nx):
  T_old[i,0] = Tcooking
  T_old[i,-1] = Tcooking

for j in range(0,Ny):
  T_old[0,j] = Tcooking
  T_old[-1,j] = Tcooking

T_new=np.copy(T_old)
time_array = np.arange(0.,tfinal,deltat)
x_array=np.linspace(0,L,num=Nx)
y_array=np.linspace(0,H,num=Ny)

print("The thermal diffusivity is {} m^2/s.".format(alpha))
print("The final time is {} seconds.".format(tfinal))
print("The step size is {} seconds.".format(deltat))
print("The simulation will loop through {} time steps.".format(len(time_array)))

for n,time in enumerate(time_array):
    for i in range(1,Nx-1):
      for j in range (1,Ny-1):
        T_new[i,j] = T_old[i,j] + alpha*deltat*((T_old[i-1,j] - 2*T_old[i,j] + T_old[i+1,j])/deltax**2 + (T_old[i,j-1] - 2*T_old[i,j] + T_old[i,j+1])/deltay**2)

    if n%(Ntime/10)==0:
      X,Y=np.meshgrid(x_array,y_array)
      plt.contourf(Y,X,T_new,cmap=plt.cm.jet)

      plt.colorbar()
      time_min = time/60
      plt.xlabel('x[m]')
      plt.ylabel('y[m]')

      n_string = str(n).zfill(3)
      plt.savefig('plot'+n_string+'.png')
      plt.close()

    T_old = np.copy(T_new)

print('THe final time is {:.2f} minutes'.format(tfinal/60))
