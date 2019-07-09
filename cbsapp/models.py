from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='wewe',primary_key=True)
    company_owner = models.CharField(max_length=50,null= True)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=12)
    about_company = models.CharField(max_length=200)
    company_type = models.CharField(max_length=200,null=True,)
    linkedin = models.CharField(max_length = 60,null=True, verbose_name=u'link to linkedin profile')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.wewe.save()

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

class ExampleModel(models.Model):
    field = models.CharField(max_length=50)
