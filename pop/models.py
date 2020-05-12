from django.db import models
from PIL import Image
from django.utils import timezone
from users.models import User
from django.contrib import messages
from django.urls import reverse
# Create your models here.
class Case(models.Model):
    pet_name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30,null=True)
    pet_breed = models.CharField(max_length=30,null=True,blank=True)
    lost_date = models.DateTimeField(null=True)
    lost_location = models.CharField(max_length=30)
    pet_image = models.ImageField(default='default.jpg',upload_to='images_pets') #requires pillow
    filed_date = models.DateField(default=timezone.now)
    reward = models.IntegerField(null=True,blank=True)
    user_contact_no = models.IntegerField(null=True)
    user_address = models.CharField(max_length=40,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    founder_id = models.IntegerField(null=True)
    founder_username = models.CharField(max_length=30,null=True)
    citizen_name = models.CharField(max_length=30,null=True)
    citizen_phone = models.IntegerField(null=True)
    found_location = models.CharField(max_length=60,null=True)
    found_date = models.DateTimeField(null=True)
    found_pet_image = models.ImageField(default='default.jpg',upload_to='images_pets')
    found_status = models.BooleanField(default=False)
    confirmed_status = models.BooleanField(default=False)
    def __str__(self):
        return self.pet_name
    #def save(self):
    #    super().save()

    #    img = Image.open(self.pet_image.path)

    #    if img.height > 300 or img.width > 300:
    #        output_size = (300,300)
    #        img.thumbnail(output_size)
    #        img.save(self.pet_image.path)
    def get_absolute_url(self):
        if self.user != None:
         return reverse('case_detail',kwargs={'pk':self.pk})
        else:
            return reverse('case_finder_list')


