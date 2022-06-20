from operator import mod
from django.db import models
opt=(
    ('Manager','Manager'),
    ('Employee', 'Employee'),
    ('Semi-Manager', 'Semi-Manager'),
    ('Accounts','Accounts')
)
stat=(
    ('Offline','Offline'),
    ('Online','Online'),
)
class employee(models.Model):
    name=models.CharField(max_length=50)
    reportingmanager=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    Mail=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    role=models.CharField(max_length=20,choices=opt, default='manager')
    status=models.CharField(max_length=20,choices=stat,default='Offline')
    def __str__(self):
        return self.username

class leave(models.Model):
    username=models.ForeignKey(employee,on_delete=models.CASCADE)
    dfrom=models.DateField()
    dto=models.DateField()
    reason=models.CharField(max_length=250)
    reportingmanager=models.CharField(max_length=50)
    approve=models.BooleanField('Approve',default=False)
    reject=models.BooleanField('Reject',default=False)    
    def __str__(self):
        return str(self.username)

class rem(models.Model):
    username=models.ForeignKey(employee,on_delete=models.CASCADE)
    reportingmanager=models.CharField(max_length=50)
    dadded=models.DateField()
    loc=models.CharField(max_length=100)
    dis=models.CharField(max_length=150)
    cat=models.CharField(max_length=20)
    pname=models.CharField(max_length=50)
    value=models.IntegerField()
    adv=models.IntegerField()
    mof=models.CharField(max_length=20)
    file=models.FileField()
    approve=models.BooleanField('Approve',default=False)
    reject=models.BooleanField('Reject',default=False)
    pay=models.BooleanField('Payment-Status',default=False)
    def __str__(self):
        return str(self.username)

class att(models.Model):
        username=models.ForeignKey(employee,on_delete=models.CASCADE) 
        dadded=models.DateField(auto_now_add=True)
        d1=models.CharField(max_length=15)
        d2=models.CharField(max_length=15)
        reportingmanager=models.CharField(max_length=50)
        def __str__(self):
            return self.username        
