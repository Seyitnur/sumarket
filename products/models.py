from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=255)
    article = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    tags = models.ManyToManyField("products.Tag",related_name="products" ,null=True, blank=True)
    phone = models.CharField(max_length=12)
    seller = models.ForeignKey("profiles.User", on_delete=models.CASCADE)

    def related_products(self):
        products = []
        for i in Product.objects.filter(category=self.category):
            if (i not in products) and (i.id != self.id):
                products.append(i)
        return products

    def __str__(self):
        return self.name

class Image(BaseModel):
    image = models.ImageField(upload_to='products')
    product = models.ForeignKey("products.Product", related_name='images', on_delete=models.CASCADE)
    order = models.IntegerField(default=1)
