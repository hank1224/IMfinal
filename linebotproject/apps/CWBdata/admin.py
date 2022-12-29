from django.contrib import admin
from CWBdata.models import hazards, rain, weather_forecast, rain_pop

class hazardsMain(admin.ModelAdmin):
    list_display = ('sLocationName', 'sPhenomena', 'sStartTime', 'sEndTime')
    list_filter = ('sPhenomena',)
    search_fields = ('sLocationName',)
    ordering = ('sStartTime',)

class rainMain(admin.ModelAdmin):
    list_display = ('sCity', 'sRAIN', 'sMIN_10', 'sHOUR_3', 'sHOUR_6', 'sHOUR_12', 'sHOUR_24', 'sNOW')
    search_fields = ('sCity',)
    ordering = ('sNOW',)
    

class weather_forecastMain(admin.ModelAdmin):
    list_display = ('sLocationName', 'sWx', 'sMinT', 'sMaxT', 'sCI')
    search_fields = ('sLocationName',)


class rain_popMain(admin.ModelAdmin):
    list_display = ('sLocationName', 'sPop')
    search_fields = ('sLocationName',)


admin.site.register(hazards, hazardsMain)
admin.site.register(rain, rainMain)
admin.site.register(weather_forecast, weather_forecastMain)
admin.site.register(rain_pop, rain_popMain)

# Register your models here.
