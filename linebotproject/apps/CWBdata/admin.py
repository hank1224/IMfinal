from django.contrib import admin
from CWBdata.models import hazards, rain

class hazardsMain(admin.ModelAdmin):
    list_display = ('sLocationName', 'sPhenomena', 'sStartTime', 'sEndTime')
    list_filter = ('sPhenomena',)
    search_fields = ('sLocationName',)
    ordering = ('sStartTime',)

class rainMain(admin.ModelAdmin):
    list_display = ('sCity', 'sRAIN', 'sMIN_10', 'sHOUR_3', 'sHOUR_6', 'sHOUR_12', 'sHOUR_24', 'sNOW')
    search_fields = ('sCity',)
    ordering = ('sNOW',)

admin.site.register(hazards, hazardsMain)
admin.site.register(rain, rainMain)
# Register your models here.
