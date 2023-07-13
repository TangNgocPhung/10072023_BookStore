from django.db import models

# Create your models here.
class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    decenttralization = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{self.id}";
    
class UserID(models.Model):
    gmail = models.EmailField(primary_key=True, max_length=300)
    username = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=300)
    IDpermission = models.ForeignKey(Permission, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.gmail}, {self.username}, {self.password}, {self.IDpermission}"