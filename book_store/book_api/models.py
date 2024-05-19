from django.db import models
from uuid import uuid4

# Create your models here.
class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid4())
    name = models.TextField(unique=True, null=False, max_length=100)
    author = models.TextField(max_length=100)
    order_link = models.TextField(max_length=2000)
    image_link = models.TextField(max_length=2000)
    