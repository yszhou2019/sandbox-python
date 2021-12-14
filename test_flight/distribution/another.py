import matplotlib.pyplot as plt
import numpy as np# 生成随机数
d1 = np.random.randn(5000)
d2 = np.random.randn(4000)
'''bins：直方图条目数alpha：透明度label：图例名'''
plt.hist(d1, bins=50, label = 'label1', density=True, stacked=True)
plt.hist(d2, bins=50, label = 'label2', density=True, stacked=True)
plt.grid(alpha=0.3)
plt.title('title')
plt.xlabel('x ')
plt.ylabel('y ')# 显示图例
plt.legend()
plt.show()
