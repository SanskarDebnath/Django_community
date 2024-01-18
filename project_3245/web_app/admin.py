from django.contrib import admin
from web_app.models import signup


class Signup_admin (admin.ModelAdmin):
    list_display = (
        'fullname', 
        'phone_number', 
        'Gender',
        'Email', 
        'user_id', 
        'username', 
        'Reg_date'
        )

adminl.site.register(signup, Signup_admin)

# Register your models here.
