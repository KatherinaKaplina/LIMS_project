from django.contrib import admin

from main.models import Reagent, Batch, Tracking


admin.site.register(Reagent)
admin.site.register(Tracking)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('reagent', 'batch_number', 'quantity', 'units')
    ordering = ('reagent',)