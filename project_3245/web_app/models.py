from django.db import models

# Create your models here.
class signup (models.Model):
    fullname = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    Gender = models.IntegerField
    Email = models.CharField(max_length=50,unique = True)
    new_password = models.CharField(max_length=200)
    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    Reg_date = models.CharField(max_length=40)

    def __str__(self):
        return self.fullname + "--" + self.user_id + "--" + self.username