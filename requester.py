from bs4 import BeautifulSoup
import requests
import json
from matplotlib import pyplot as plt
import os
class API_Request: # API 요청, 값 저장.
    api_urls = {
        "BTN" : {
            "GDP" : "https://api.worldbank.org/v2/country/BTN/indicator/NY.GDP.MKTP.CD?format=json",
            "Population" : "https://api.worldbank.org/v2/country/BTN/indicator/SP.POP.TOTL?format=json"
        },
        "CR" : {
            "GDP" : "https://api.worldbank.org/v2/country/CR/indicator/NY.GDP.MKTP.CD?format=json",
            "Population" : "https://api.worldbank.org/v2/country/CR/indicator/SP.POP.TOTL?format=json"
        },
        "KR" : {
            "GDP" : "https://api.worldbank.org/v2/country/KR/indicator/NY.GDP.MKTP.CD?format=json",
            "Population" : "https://api.worldbank.org/v2/country/KR/indicator/SP.POP.TOTL?format=json"
        },
        "US" : {
            "GDP" : "https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.CD?format=json",
            "Population" : "https://api.worldbank.org/v2/country/US/indicator/SP.POP.TOTL?format=json"
        }
    } # API 링크
    def request_data(self, url:str) -> str:
        res = requests.get(url)
        return res.text
    def save(self, country="BTN", type="GDP", folder="data"):
        if not os.path.exists("./"+folder+"/"):
            os.makedirs("./"+folder+"/")  # 폴더 생성
        with open("./"+folder+"/"+country+"_"+type+".json", mode="w") as file: #데이터 저장
            data = self.request_data(self.api_urls[country][type])
            file.write(data)
        return True
    def saveAll(self, folder="data"):
        for i in self.api_urls:
            for j in self.api_urls[i]: # 반복 > 모든 API값 저장
                self.save(i,j, folder)
        return True
    def load(self, country="BTN", type="GDP"):
        with open(country+"_"+type+".json", mode="r") as file: # 파일 읽기
            return file