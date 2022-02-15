from django.contrib import admin
from . import models

@admin.register(models.SubPlan)
class SubPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']

@admin.register(models.SubPlanFeature)
class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display = ['feature']

