from django.db import models

# Create your models here.

class MyProfile(models.Model):
    profile_image=models.ImageField(upload_to='media/profileimage/',blank=True)
    contact_info=models.ForeignKey()
    basic_info=models.ForeignKey()
    
class ContactInfo(models.Model):
    email=models.EmailField()
    phone=models.PositiveIntegerField(max_length=15,null=False)
    address=models.TextField()

class BasicInfo(models.Model):
    name=models.CharField(max_length=50) 
    birth_date=models.DateField()
    gender=models.TextChoices()
    military_service=models.TextChoices()
    nationality=models.CharField(max_length=20)
    languages=models.ForeignKey()
    
class WorkHistory(models.Model):
    company_name=models.CharField(max_length=30)
    from_date=models.DateField()
    to_date=models.DateField()
    work_details=models.TextField()
    
class Education(models.Model):
    universty=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    department=models.CharField(max_length=100)

class projects(models.Model):
    project_name=models.CharField(max_length=60)
    project_details=models.TextField()
    project_link=models.URLField()
    technologies_used=models.ForeignKey()
    
class Technologies(models.Model):
    technology=models.CharField(max_length=30)
    
class  Skills(models.Model):
    skill=models.CharField(max_length=40)
    skill_detail=models.TextField()
    
class certificates(models.Model):
    certificate_name = models.CharField(max_length=150)
    certificate_detail=models.TextField()
    certificate_link=models.URLField()
    

    

    
