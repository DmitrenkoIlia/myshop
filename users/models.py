from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import Product

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    city = models.CharField(max_length=100, blank=True, verbose_name='Місто')
    address = models.CharField(max_length=100, blank=True, verbose_name='Вулиця')
    house = models.CharField(max_length=100, blank=True, verbose_name='Будинок')
    flat = models.CharField(max_length=100, blank=True, verbose_name='Квартира')

    wishlist = models.ManyToManyField(Product, related_name='wished_by', blank=True, verbose_name='Список бажань')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Профиль {self.user.username}"

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()