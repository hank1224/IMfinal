from django.contrib import admin
from chatGPT.models import lineUser

class lineUserMain(admin.ModelAdmin):
    list_display = ('sLineID', 'sName', 'sCity')
    list_filter = ('sCity',)
    search_fields = ('sName',)
    ordering = ('sCity',)

admin.site.register(lineUser, lineUserMain)
# Register your models here.
