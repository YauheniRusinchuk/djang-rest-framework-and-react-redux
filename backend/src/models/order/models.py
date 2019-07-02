from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    owner       = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE, null=True)
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    create_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
