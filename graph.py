from matplotlib import pyplot as plt
from requester import API_Request
import random
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator, FuncFormatter
import json

color = ["red", "blue", "green", "purple", "black"]

API_Request().saveAll() # > API 데이터 갱신
# plt.figure(figsize=(16,9))
# k=0
# for i in API_Request.country_code:
#     for j in API_Request.indicator_code:
#         k+=1
#         api_data = pd.json_normalize(API_Request().getData(i,j))
#         x = api_data["date"]
#         y = api_data["value"]
#         axes = plt.subplot(4,len(API_Request.indicator_code),k)
#         plt.title(f"{i}.{j}", fontsize=10)
#         axes.xaxis.set_major_locator(MaxNLocator(5))
#         plt.grid()
#         plt.plot(x,y, linewidth=1.5)
# plt.subplots_adjust(hspace=1, wspace=1)
# plt.show()
# k=0
# for i in API_Request.indicator_code:
#     for j in API_Request.country_code:
#         k+=1
#         api_data = pd.json_normalize(API_Request().getData(j,i))
#         x = api_data["date"]
#         y = api_data["value"]
#         plt.subplot(len(API_Request.indicator_code), 4, k)
#         plt.title(f"{j}.{i}", fontsize=10)
#         plt.grid()
#         plt.plot(x,y)
# plt.show()
# plt.figure(figsize=(15,3))
# k=0
# for i in API_Request.indicator_code:
#     k+=1
#     plt.subplot(3, 3, k)
#     plt.grid()
#     for j in API_Request.country_code:
#         api_data = pd.json_normalize(API_Request().getData(j,i))
#         x = api_data["date"]
#         y = api_data["value"]
#         plt.xlabel("Years")
#         plt.ylabel(i, loc="top", rotation=360, fontsize=9)
#         plt.plot(x,y,color=color[list(API_Request.country_code).index(j)], label=API_Request.country_code[j])
#     plt.legend()
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
# plt.show()
# 각 지표 별 그래프 통합
for i in API_Request.country_code:
    for j in API_Request.indicator_code:
        api_data = pd.json_normalize(API_Request().getData(i,j))
        x = api_data["date"]
        y = api_data["value"]
        plt.figure(figsize=(5,5))
        plt.title(f"{i}.{j}")
        plt.grid()
        plt.plot(x,y)
        plt.show()