from django.db import models

# Create your models here.
class MenuType(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    
    class Meta:
        db_table = 'type'
        ordering = ['-id']


class Menu(models.Model):
    name = models.CharField(max_length = 80, blank = True, null = True)
    type = models.ForeignKey(MenuType, blank = True, null = True, on_delete = models.CASCADE)
    url = models.CharField(max_length = 80, blank = True, null = True)
    upper_menu = models.ForeignKey('self', blank = True, null = True, on_delete = models.CASCADE)


    class Meta:
        db_table = 'menu'
        ordering = ['-id']

