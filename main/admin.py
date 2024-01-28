from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_date']
    search_fields = ['name', ]
    date_hierarchy = 'created_date'
    readonly_fields = ['created_date', ]
