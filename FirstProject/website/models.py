from django.db import models

#Student Name
#Student Roll
#Student Class

class student_info(models.Model):
    std_name = models.CharField(max_length=50)
    std_roll = models.IntegerField()
    std_class = models.CharField(max_length=20)

class employee_info(models.Model):

    emp_name = models.CharField(max_length=20)
    emp_email = models.EmailField()
    emp_pic = models.ImageField(upload_to='employee/',blank=True,null=True)
    is_delete = models.BooleanField(default=False)
