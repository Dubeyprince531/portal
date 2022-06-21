from django.db import models

# Create your models here.

class UserMaster(models.Model):
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=30)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    
    
class candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to="app/imp/candidate")
    
    
class company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    logo_pic = models.ImageField(upload_to="app/imp/company")
    

class JobDetail(models.Model):
    company_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    companyaddress = models.CharField(max_length=250)
    jobndescription = models.TextField(max_length=500)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    joblocation = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    companyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=20)
    salarypackage = models.CharField(max_length=250)
    experience = models.IntegerField(blank=True, null=True, default=None)
