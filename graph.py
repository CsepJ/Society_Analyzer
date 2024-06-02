from matplotlib import pyplot as plt
import numpy as np
plt.figure(figsize=(8,8))
plt.plot(range(1,101), np.power(range(1,101), 2))
plt.bar()
plt.show()