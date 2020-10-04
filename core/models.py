from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
class Services(models.Model):
    title = models.CharField(max_length=225)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"
        db_table = 'table_services'
        
class Subservices(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    subservices = models.CharField(max_length=225)
    
    def __str__(self):
        return self.subservices

    class Meta:
        verbose_name = "Sub Services"
        verbose_name_plural = "Sub Services"
        db_table = 'table_subservices'

class Hireus(models.Model):
    title = models.CharField(max_length=225)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Hire Us"
        verbose_name_plural = "Hire Us"
        db_table = 'table_hireus'
        
class Hireuseconn(models.Model):
    title = models.ForeignKey(Hireus, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Hire Us Content"
        verbose_name_plural = "Hire Us Content"
        db_table = 'table_hireuscontent'
