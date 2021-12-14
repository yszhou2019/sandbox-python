# import matplotlib.pyplot as plt
# from datetime import datetime
# import pandas as pd
# import numpy as np
#
# # 从已经写好的csv文件中读取数据
# mydata = pd.read_csv("data.csv")
# print(data) # 查看数据
#
# # 将数据提取出作为坐标，将数值转化为int型，datetime类型转化为string类型
# count = np.array(mydata['Count'].astype(str).astype(int))
# date = np.array(mydata['Time'].astype(str))
#
# # X坐标，将str类型的数据转换为datetime.date类型的数据，作为x坐标
# xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in date]
#
# # 图表格式
# # 设置图形格式
#
# plt.title('地铁人数', fontsize=25)  # 字体大小设置为25
# plt.xlabel('日期', fontsize=10)  # x轴显示“日期”，字体大小设置为10
# plt.ylabel('人数', fontsize=10)  # y轴显示“人数”，字体大小设置为10
# plt.plot(xs, count, 'o-', label='客流量')
# plt.tick_params(axis='both', which='both', labelsize=10)
#
# # 显示折线图
# plt.gcf().autofmt_xdate()  # 自动旋转日期标记
# plt.show()


# https://www.coder.work/article/4908151
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm
#
# n = 11 # change this value for the number of iterations/percentiles
# colormap = cm.Blues # change this for the colormap of choice
# percentiles = np.linspace(0,100,n)
#
# SampleData=(375-367)*np.random.random_sample((365, 50))+367
# SDist=np.zeros((365,n))
# for i in range(n):
#     for t in range(365):
#       SDist[t,i]=np.percentile(SampleData[t,:],percentiles[i])
#
# half = int((n-1)/2)
#
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, sharex=True, figsize=(8,4))
# ax1.plot(np.arange(0,365,1), SDist[:,half],color='k')
# for i in range(half):
#     ax1.fill_between(np.arange(0,365,1), SDist[:,i],SDist[:,-(i+1)],color=colormap(i/half))
#
# ax1.set_title("SampleData", fontsize=15)
# ax1.tick_params(labelsize=11.5)
# ax1.set_xlabel('Day', fontsize=14)
# ax1.set_ylabel('SampleData', fontsize=14)
# fig.tight_layout()
# plt.show()


# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

date = pd.date_range('2018-09-03', '2018-09-06')
y1 = [0.9143, 0.9293, 0.9348, 0.9327]
y2 = [0.9143, 0.9294, 0.9348, 0.9327]

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_major_formatter(mdate.DateFormatter('%Y%m%d'))  # 设置时间标签显示格式
ax.xaxis.set_major_locator(mdate.DayLocator())
ax.set_title("y plot")
ax.plot(date, y1, 'go-', label=u'this is y1')
ax.plot(date, y2, 'yo-', label=u'this is y2')
plt.xticks(rotation=45)  # 旋转45度显示
legend = ax.legend(loc='lower center', shadow=False)
plt.show()
