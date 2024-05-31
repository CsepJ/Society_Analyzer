from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt
class API_Request:
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
    }
    def request_data(self, url:str) -> str:
        res = requests.get(url)
        return res.text
    def save(self, country="BTN", type="GDP"):
        with open(country+"_"+type+".json", mode="w") as file:
            data = self.request_data(self.api_urls[country][type])
            file.write(data)
    def saveAll(self):
        for i in self.api_urls:
            for j in self.api_urls[i]:
                self.saveData(i,j)
    def load(self, country="BTN", type="GDP"):
        with open(country+"_"+type+".json", mode="r") as file:
            return file