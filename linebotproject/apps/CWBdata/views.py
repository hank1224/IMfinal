#from django.shortcuts import render
import requests

from django.db import IntegrityError
from django.http import HttpResponse
from django.conf import settings

from CWBdata.models import hazards, rain

def refresh_hazards():
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/W-C0033-001"
    res = requests.get(url, {"Authorization": settings.CWB_AUTH})
    resJson = res.json()

    locations = resJson["records"]["location"]
    for locationss in locations:
        cLocationName = locationss["locationName"]
        try:
            cPhenomena = locationss["hazardConditions"]["hazards"][0]["info"]["phenomena"]
            cStartTime = locationss["hazardConditions"]["hazards"][0]["validTime"]["startTime"]
            cEndtime = locationss["hazardConditions"]["hazards"][0]["validTime"]["endTime"]
        except:
            cPhenomena = None
            cStartTime = None
            cEndtime = None

        try:
            hazards.objects.create(sLocationName = cLocationName, sPhenomena = cPhenomena, sStartTime = cStartTime, sEndTime = cEndtime)
        except IntegrityError:
            hazards.objects.filter(sLocationName = cLocationName).update(sPhenomena = cPhenomena, sStartTime = cStartTime, sEndTime = cEndtime)

def refresh_rain():
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0002-001?parameterName=CITY&stationId=C0ACA0,C0AC70,C0B010,C0C700,"+\
        "C0D660,C0E750,C0F9U0,C0G650,C0H890,C0K400,C0M770,C0X110,C0V700,C0R170,C0U900,C0T960,C0SA60,C0W130,C0W150"
    res = requests.get(url, {"Authorization": settings.CWB_AUTH})
    resJson = res.json()
    """
        新北市 新莊 C0ACA0
        臺北市 信義 C0AC70
        基隆市 七堵 C0B010
        桃園市 中壢 C0C700
        新竹縣 新豐 C0D660
        苗栗縣 苗栗 C0E750 
        臺中市 南屯 C0F9U0
        彰化縣 員林 C0G650
        南投縣 埔里 C0H890
        雲林縣 斗六 C0K400 
        嘉義縣 民雄 C0M770
        台南市 南區 C0X110
        高雄市 三民 C0V700
        屏東縣 屏東 C0R170
        宜蘭縣 內城 C0U900
        花蓮縣 光復 C0T960
        臺東縣 知本 C0SA60
        澎湖縣 花嶼 C0W130
        金門縣 金寧 C0W150
    """
    locations = resJson["records"]["location"]
    for locationss in locations:
        City = locationss['parameter'][0]['parameterValue']
        RAIN = locationss['weatherElement'][1]['elementValue']
        MIN_10 = locationss['weatherElement'][2]['elementValue']
        HOUR_3 = locationss['weatherElement'][3]['elementValue']
        HOUR_6 = locationss['weatherElement'][4]['elementValue'] 
        HOUR_12 = locationss['weatherElement'][5]['elementValue']
        HOUR_24 = locationss['weatherElement'][6]['elementValue']
        NOW = locationss['weatherElement'][7]['elementValue']

        if RAIN == "-998.00": #氣象局格式問題
            RAIN = MIN_10 = HOUR_3 = HOUR_6 = 0

        try:
            rain.objects.create(sCity= City, sRAIN= RAIN, sMIN_10= MIN_10, sHOUR_3= HOUR_3, \
                sHOUR_6= HOUR_6, sHOUR_12= HOUR_12, sHOUR_24= HOUR_24, sNOW= NOW)
        except IntegrityError:
            rain.objects.filter(sCity= City).update(sRAIN= RAIN, sMIN_10= MIN_10, sHOUR_3= HOUR_3, \
                sHOUR_6= HOUR_6, sHOUR_12= HOUR_12, sHOUR_24= HOUR_24, sNOW= NOW)

def run_CWBapp(requset):
    refresh_hazards()
    refresh_rain()
    return HttpResponse(str("510yyds"))