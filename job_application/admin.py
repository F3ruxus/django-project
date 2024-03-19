from django.contrib import admin
from .models import Form 

class FormAdmin(admin.ModelAdmin): 
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("date", "occupation")
    # To see the in reverse, put a - in front of the first name.
    ordering = ("first_name",)
    readonly_fields = ("occupation",)

# Register your models here.
admin.site.register(Form, FormAdmin)