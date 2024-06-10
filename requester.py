import requests
import os
import json
class API_Request:  # API 요청, 값 저장.
    folderName = "data"  # API 파일 폴더 이름
    dataFormat = "json"  # API 자료 형식 (XML/JSON)
    country_code = {
        "Korea": "KR",
        "United_States": "US"
    }
    indicator_code = {  # 지표 코드 (언더바 X - 파일 이름)
        "GDP": "NY.GDP.MKTP.CD",
        "Personal_GDP": "NY.GDP.PCAP.CD",
        "Population": "SP.POP.TOTL",
        "Unemployment": "SL.UEM.TOTL.ZS",
        "Labor_Participation": "SL.TLF.CACT.ZS",
        "Gini": "SI.POV.GINI",
        "Airplane_Infra": "IS.AIR.PSGR",
        "Train_Infra": "IS.RRS.TOTL.KM",
        "Electricity_Infra": "EG.ELC.ACCS.ZS",
        "Internet_Infra": "IT.NET.USER.ZS",
        "Health_Infra": "SH.XPD.CHEX.GD.ZS"
    }
    def request_api(self, country="Bhutan", indicator="GDP"):  # API 기본 요청
        url = f"https://api.worldbank.org/v2/country/{self.country_code[country]}/indicator/{self.indicator_code[indicator]}?format={self.dataFormat}"
        response = requests.get(url)
        return response.text
    
    def getPath(self, country="Bhutan", indicator="GDP"):  # API 저장 파일 경로
        return f"./{self.folderName}/{self.country_code[country]}_{indicator}.json"
    
    def saveData(self, country="Bhutan", indicator="GDP"):  # API 결과을 파일로 저장
        if not os.path.exists(f"./{self.folderName}/"):
            os.makedirs(f"./{self.folderName}/")  # 폴더 생성
        with open(self.getPath(country, indicator), mode="w") as file:
            data = self.request_api(country,indicator)
            file.write(data)

    def saveAll(self):
        for i in self.country_code:
            for j in self.indicator_code:  # 반복 > 모든 API값 저장
                self.saveData(i,j)

    def getData(self, country="Bhutan", indicator="GDP"):
        result:list[dict] = []  # 리턴 결과
        with open(self.getPath(country,indicator), mode="r") as file:
            for i in json.loads(file.read())[1]:
                result.append({"date": int(i["date"]), "value": i["value"]})  # 연도와 값만 가져와서 새 딕셔너리로 재배열
        return sorted(result, key=lambda x: x["date"])  # 연도별 오름차순 정렬