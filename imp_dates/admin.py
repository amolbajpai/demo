from django.contrib import admin
from .models import ImpDatesModel

# Register your models here.
@admin.register(ImpDatesModel)
class ImpDatesAdmin(admin.ModelAdmin):
    list_display = ['name','occasion','date','remarks']
