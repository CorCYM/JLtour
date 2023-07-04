from django.db import models

# Create your models here.
from django.db.models.fields import CharField

class City(models.Model) :
    location = CharField(primary_key=True, max_length=40, null=False)
    citynumber = CharField(max_length=20, null=True)
    
    
    class Meta :
        db_table = "city"
        app_label = "tourapp"
        managed = False 
        

class Detail(models.Model) :
    location = CharField(max_length=100, null=False)
    address = CharField(primary_key=True, max_length=200, null=False)
    attraction = CharField(max_length=200, null=True)
    food = CharField(max_length=200, null=True)
    
    class Meta :
        db_table = "detail"
        app_label = "tourapp"
        managed = False 
    
    