from django.db import models


class Member(models.Model):
    pro_pic = models.ImageField(default='profile.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    GENDER =(
        ('male','male'),
        ('female', 'female')
    )
    gender = models.CharField(max_length=50, choices=GENDER, default='male')
    MARITAL_STATUS = (
        ('single','single'),
        ('married','married'),
        ('other','other')
    )
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS, default='single')
    home_address = models.CharField(max_length=100)
    res_address = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    CUR_LEVEL = (
        ('high_school','high_school'),
        ('vocation','vocation'),
        ('tetiary','tetiary'),
    )
    cur_level = models.CharField(max_length=50, choices=CUR_LEVEL, default='100')
    institution = models.CharField(max_length=100)
    BAPTISM = (
        ('yes','yes'),
        ('no', 'no')
    )
    baptism = models.CharField(max_length=50, choices=BAPTISM, default='yes')
    confirmation = models.CharField(max_length=50, choices=BAPTISM, default='yes')
    position = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    list = models.JSONField()
    def __str__(self):
        return f"{self.date}'s Attendance"