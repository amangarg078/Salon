from __future__ import unicode_literals
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.conf import settings
import os
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #return '/salon_{0}/{1}'.format(instance.salon_id.id, filename)
    folder = instance.salon_id and instance.salon_id.id or 'default'
    return 'salon_{0}/{1}'.format(folder, filename)
# Create your models here.
class SalonStore(models.Model):
	
    #id=models.AutoField(primary_key=True,default=1)
    CHOICES= (('Karnataka', 'Karnataka'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Kerala', 'Kerala'), ('Tamil Nadu', 'Tamil Nadu'), ('Maharashtra', 'Maharashtra'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Rajasthan', 'Rajasthan'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Telangana', 'Telangana'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chattisgarh', 'Chattisgarh'), ('Haryana', 'Haryana'), ('Jharkhand', 'Jharkhand'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Orissa', 'Orissa'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar', 'Andaman and Nicobar'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Delhi', 'Delhi'), ('Lakshadweep', 'Lakshadweep'), ('Pondicherry', 'Pondicherry'))
    name = models.CharField(max_length=256)
    
    address_1 = models.CharField(max_length=128 )
    address_2 = models.CharField(max_length=128 ,null=True)
    address_3 = models.CharField(max_length=128 )
    state=models.CharField(choices=CHOICES,default='Delhi',max_length=128)
    country= models.CharField(max_length=128, default='India')
    contact_number= models.CharField(max_length=12)
    email= models.EmailField()
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(default=timezone.now)
    def __unicode__(self):
        return self.name
class Photo(models.Model):
    #dest=settings.MEDIA_ROOT + '/photo/'
    salon_id = models.ForeignKey(SalonStore,null=True)
    title = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to=user_directory_path)
    
    is_cover_photo = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title
    class Meta:
        ordering=["-date_created"]
