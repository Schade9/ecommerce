from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='categories')

    def __str__(self):
        return self.category

    # image output size
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
            img.save(self.image.path)
        # elif img.height < 800 or img.width < 800:
        #     output_size = (800, 800)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skuNumber = models.CharField(max_length=100)
    #store = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    description = models.TextField()
    condition = models.CharField(max_length=50)
    warranty = models.CharField(max_length=50)
    image = models.ImageField(default='product_default.jpg', upload_to='products')

    def __str__(self):
        return self.productName

    # image output size
    # def save(self, *args, **kwargs):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 800 or img.width > 800:
    #         output_size = (800, 800)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    