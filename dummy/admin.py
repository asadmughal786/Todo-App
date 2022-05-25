from django.contrib import admin
from .models import TODOS, Contact
# Register your models here.
# admin.site.register(Contact)

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone']
    list_display_links = ['id', 'email', 'phone']
    readonly_fields = ('email',)
@admin.register(TODOS)
class AdminTODOS(admin.ModelAdmin):
    list_display = ['title','contnt']
    list_disply_links = ['title','contnt']
