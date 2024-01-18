from django.contrib import admin
from web_app.models import signup

class SignupAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 
        'phone_number', 
        'Gender',
        'Email', 
        'user_id', 
        'username', 
        'Reg_date'
    )

admin.site.register(signup, SignupAdmin)


# Register your models here.
