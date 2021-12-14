
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

data = np.random.randn(1000)
#最基本的频次直方图命令
plt.hist(data)
plt.show()
# print(data)