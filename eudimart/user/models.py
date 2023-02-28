from django.db import models


# Create your models here.
class Userdata(models.Model):
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=32)
    Middle_Name = models.CharField(max_length=32)
    Last_Name = models.CharField(max_length=32)
    User_id = models.CharField(max_length=25, )
    Gender = models.CharField(max_length=6, choices=(("M", "Male"), ("F", "Female"), ("O", "Others")))
    Age = models.IntegerField(max_length=3)
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)

    def __str__(self):
        return self.User_id


class Tweet(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    tweet = models.TextField()
    User_id = models.ForeignKey(Userdata, on_delete=models.CASCADE)
