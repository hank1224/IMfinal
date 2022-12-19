from django.db import models

class hazards(models.Model):
    sLocationName=models.CharField(max_length=3, null=False, primary_key=True)
    sPhenomena=models.CharField(max_length=15, null=True)
    sStartTime=models.DateTimeField(blank=False, null=True)
    sEndTime=models.DateTimeField(blank=False, null=True)
    
    #def __str__(self):
        #return self.sLocationName
    #讓object預設回傳

class rain(models.Model):
    sCity = models.CharField(max_length=3, null=False, primary_key=True) #所在縣市
    sRAIN = models.FloatField(null=False, blank=False) #60分鐘累積雨量，單位 毫米
    sMIN_10 = models.FloatField(null=False, blank=False) #10分鐘累積雨量，單位 毫米
    sHOUR_3 = models.FloatField(null=False, blank=False) #3小時累積雨量，單位 毫米
    sHOUR_6 = models.FloatField(null=False, blank=False) #6小時累積雨量，單位 毫米
    sHOUR_12 = models.FloatField(null=False, blank=False) #12小時累積雨量，單位 毫米
    sHOUR_24 = models.FloatField(null=False, blank=False) #24小時累積雨量，單位 毫米
    sNOW = models.FloatField(null=False, blank=False) #本日累積雨量
    #雨量值為 -998.00 表示 RAIN = MIN_10 = HOUR_3 = HOUR_6 = 0.00

# Create your models here.
