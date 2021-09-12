import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,50)
plt.ylim(0,50)
plt.plot(n,n,label="n")
plt.plot(n,np.square(n),label="n^2")
plt.plot(n,np.power(2,n),label="2^n")
plt.plot(n,np.sqrt(n),label="sqrt(n)")
plt.plot(n,np.log(n),label="logn")
plt.plot(n,(n*(np.log(n))),label="nlog(n)")
plt.plot(n,np.square(np.log(n)),label="(log(n))^2")
plt.legend(loc="upper right")
plt.xlabel('n')
plt.title('Graphs')
plt.show()


