from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
    ('Ariana', 'Ariana'),
    ('Béja', 'Béja'),
    ('Bizerte', 'Bizerte'),
    ('Ben Arous', 'Ben Arous'),
    ('Gabès', 'Gabès'),
    ('Jendouba', 'Jendouba'),
    ('Jendouba', 'Jendouba'),
    ('	Kasserine', '	Kasserine'),
    ('Kebili', 'Kebili'),
    ('	Mahdia', '	Mahdia'),
    ('Medenine', 'Medenine'),
    ('Monastir', 'Monastir'),
    ('	Nabeul', '	Nabeul'),
    ('Sfax', 'Sfax'),
    ('	Siliana', '	Siliana'),
    ('		Sousse', '	Sousse'),
    ('Tataouine', 'Tataouine'),
    ('	Tozeur', '	Tozeur'),
    ('Tunis', 'Tunis'),
    ('Zaghouan', 'Zaghouan'),
)

CATEGORY_CHOICES=(
    ('TU','Tunisia'),
    ('TUR','Turkiye'),
    ('DO','Dubai'),
    ('QA','Qatar'),
    ('FR','France'),
    ('GR','Germany'),
    ('IT','Italy'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    composition = models.TextField(default='')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    prodapp = models.TextField(default='')
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField( max_length=200)
    city = models.CharField( max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATE_CHOICES, default='Pending')
    ordered_data = models.DateTimeField(auto_now_add=True)
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
        