from django.db import models

# Create your models here.

class createuser(models.Model):
    username = models.CharField(max_length=100,null=True,unique=True)
    password = models.CharField(max_length=100,null=True)

   


    def __str__(self):
        return self.username

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100,null=True)
    recipe_description = models.TextField()
    recipe_price = models.CharField(max_length=100,null=True)
    recipe_image = models.ImageField(upload_to='recipe',null=True)

    # name = models.ForeignKey(createuser, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.recipe_name
    
