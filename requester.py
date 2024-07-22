import requests
import os
import json
class API_Request:  # API 요청, 값 저장.
    folderName = "data"  # API 파일 폴더 이름
    dataFormat = "json"  # API 자료 형식 (XML/JSON)
    country_code = {
        "Korea": "KR",
        "United_States": "US"
    } # 각 국가 코드
    indicator_code = {  # 지표 코드
        "GDP": "NY.GDP.MKTP.CD", # 국가별 GDP 지표 API 코드
        "Personal_GDP": "NY.GDP.PCAP.CD",  # 1인 GDP 지표 API 코드
        "Population": "SP.POP.TOTL", # 인구 지표 API 코드
        "Unemployment": "SL.UEM.TOTL.ZS", # 국가 실업률 API 코드
        "Labor_Participation": "SL.TLF.CACT.ZS", #국가 노동 참여율 API 코드
        "Gini": "SI.POV.GINI", # 국가별 지니 계수(소득 불평등 지표) API 코드
        "Airplane_Infra": "IS.AIR.PSGR", # 국가별 GDP 지표 API 코드
        "Train_Infra": "IS.RRS.TOTL.KM", # 국가 철도 지표 API 코드
        "Electricity_Infra": "EG.ELC.ACCS.ZS", # 국가 전기 인프라 수치 API 코드
        "Internet_Infra": "IT.NET.USER.ZS", # 국가 인터넷 인프라 수치 API 코드
        "Health_Infra": "SH.XPD.CHEX.GD.ZS" # 국민 건강 수치 API 코드
    }
    def request_api(self, country="Bhutan", indicator="GDP"):  # API 요청 함수
        url = f"https://api.worldbank.org/v2/country/{self.country_code[country]}/indicator/{self.indicator_code[indicator]}?format={self.dataFormat}" # API 요청 URL
        response = requests.get(url)
        return response.text
    
    def getPath(self, country="Bhutan", indicator="GDP"):  # API 저장 파일 경로
        return f"./{self.folderName}/{self.country_code[country]}_{indicator}.json" # 저장 파일명
    
    def saveData(self, country="Bhutan", indicator="GDP"):  # API 결과을 파일로 저장
        if not os.path.exists(f"./{self.folderName}/"):
            os.makedirs(f"./{self.folderName}/")  # 폴더가 없을 시 폴더 생성
        with open(self.getPath(country, indicator), mode="w") as file:
            data = self.request_api(country,indicator) # API 요청 함수
            file.write(data)

    def saveAll(self): # 모든 API 데이터 저장 함수
        for i in self.country_code:
            for j in self.indicator_code:  # 반복 > 모든 API값 저장
                self.saveData(i,j)

    def getData(self, country="Bhutan", indicator="GDP"): # API 값을 정렬하여 불러오는 함수
        result:list[dict] = []  # 리턴 결과
        with open(self.getPath(country,indicator), mode="r") as file:
            for i in json.loads(file.read())[1]:
                result.append({"date": int(i["date"]), "value": i["value"]})  # 연도와 값만 가져와서 새 딕셔너리로 재배열
        return sorted(result, key=lambda x: x["date"])  # 연도별 오름차순 정렬