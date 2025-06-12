from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    

class Group(models.Model):
    """
    Group model representing available groups for users to join.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    group_icon = models.ImageField(upload_to='group_icons/', blank=True, null=True)
    group_icon_url = models.URLField(max_length=255, blank=True, null=True)
    member_count = models.IntegerField(default=0)

    #  ManyToManyField to link users to groups
    users = models.ManyToManyField(User, through='BasketItem')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Update the member count before saving
        self.member_count = self.users.count()
        super().save(*args, **kwargs)
    
class BasketItem(models.Model):
    """
    Model representing the association between a user and a group.
    """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.group.name}"
    
class PurchasedItem(models.Model):
    """
    Model representing a purchased item in the basket.
    """
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.item_name
















        