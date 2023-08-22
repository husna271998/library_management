from django.db import models


# Create your models here.
class LoginRecord(models.Model):
   username=models.CharField(max_length=100)
   password=models.CharField(max_length=100)

class SignupRecord(models.Model):
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    
    
   
    
class Books(models.Model):
    book_name=models.CharField(max_length=255)
    author_name=models.CharField(max_length=255)
    year_of_publishing=models.CharField(max_length=255)
    book_image=models.ImageField(upload_to='books')
    def __str__(self):
        return self.book_name
    
    
class MembersRecord(models.Model):
    member_name=models.CharField(max_length=255)
    membership_id=models.CharField(max_length=255)
    book_details=models.ForeignKey(Books,default="",on_delete=models.CASCADE)
    date_of_issue=models.DateField()
    date_ot_return=models.DateField()
 
   #there is an error in /admin/MembersRecord 
    