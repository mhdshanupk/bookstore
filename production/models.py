from django.db import models
from django.contrib.auth.models import User
# Create 
class Book(models.Model):
    TYPE=(
        ('Fiction','Fiction'),
        ('Science Fiction','Science Fiction'),
        ('Engineering','Engineering'),
        ('PSC','PSC'),
        ('Politics','Politics'),
        ('Finance','Finance')
    )
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    author=models.CharField(max_length=50)
    type=models.CharField(max_length=50,choices=TYPE)
    is_published=models.BooleanField(default=False)

class Reviews(models.Model):
    fk_user=models.ForeignKey(User,on_delete=models.CASCADE)
    fk_book= models.ForeignKey(Book, on_delete=models.CASCADE)
    reviews= models.TextField()

    