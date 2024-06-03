from matplotlib import pyplot as plt
from requester import API_Request
import random
import numpy as np
import pandas as pd
from matplotlib.ticker import MaxNLocator, FuncFormatter
import json
color = ["red", "blue", "green", "purple", "black"]
# API_Request().saveAll() # > API 데이터 갱신
k=0
for i in API_Request.country_code:
    for j in API_Request.indicator_code:
        k+=1
        api_data = pd.json_normalize(API_Request().getData(i,j))
        x = api_data["date"]
        y = api_data["value"]
        axes = plt.subplot(4,len(API_Request.indicator_code),k)
        plt.title(f"{i}.{j}", fontsize=10)
        axes.xaxis.set_major_locator(MaxNLocator(5))
        plt.grid()
        plt.plot(x,y, linewidth=1.5)
plt.subplots_adjust(hspace=0.7, wspace=0.5)

plt.figure(figsize=(15,3))
k=0
for i in API_Request.indicator_code:
    k+=1
    plt.subplot(1, len(API_Request.indicator_code), k)
    plt.title(i, fontsize=10)
    plt.grid()
    for j in API_Request.country_code:
        api_data = pd.json_normalize(API_Request().getData(j,i))
        x = api_data["date"]
        y = api_data["value"]
        plt.xlabel("Years")
        plt.ylabel("value", loc="top", rotation=360, fontsize=11)
        plt.plot(x,y,color=color[list(API_Request.country_code).index(j)], label=API_Request.country_code[j])
    plt.legend()
plt.subplots_adjust(wspace=0.5)
plt.tight_layout()
plt.show()
# 각 지표 별 그래프 통합