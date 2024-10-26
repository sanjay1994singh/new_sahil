from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    desc = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='category_img', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
