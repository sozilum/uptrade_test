from django.db import models
from django.urls import reverse


class Menu(models.Model):
    
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

class InnerMenu(models.Model):

    menu = models.ForeignKey(Menu,
                             on_delete = models.CASCADE,
                             related_name = 'item',
                             )
    innermenu = models.ForeignKey('self',
                                  on_delete = models.CASCADE,
                                  null = True,
                                  blank = True,
                                  related_name = 'child',
                                  )
    name = models.CharField(max_length = 100)
    url = models.CharField(max_length = 300, 
                           blank = True,
                           )
    innerurl = models.CharField(max_length = 300,
                                blank = True,
                                )
    
    def __str__(self):
        return self.name
    
    def get_url(self):
        if self.innerurl:
            return reverse(self.innerurl)
        return self.url