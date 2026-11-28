from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("titre","description","date_debut",)
    list_filter = ("date_debut",)
    search_fields = ("title","description",)