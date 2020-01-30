from users.models import User
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


# Categories for Class.Items and Class.Boxes
CATEGORY_CHOICES_BOXES = (
    ('W', 'Weekly'),
    ('M', 'Monthly')
)

CATEGORY_CHOICES_ITEMS = (
    ('C1', 'Category 1'),
    ('C2', 'Category 2'),
    ('C3', 'Category 3'),
    ('C4', 'Category 4'),
    ('C5', 'Category 5')
)

# Labels for Class.Items and Class.Boxes
ITEM_LABELS = (
    ('D', 'Discount'),
    ('S', 'Sale')
)

BOX_LABELS = (
    ('X', 'Extra Box'),
    ('D', 'Discount'),
    ('S', 'Sale')
)


# Models for webshop, items and boxes
class Box(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    discount_price = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=1)
    frequency = models.DecimalField(max_digits=3, decimal_places=0)
    frequency_extension = models.CharField(choices=CATEGORY_CHOICES_BOXES, max_length=1)
    description = models.CharField(max_length=750)
    label = models.CharField(choices=BOX_LABELS, max_length=1, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    # Defines a function to return slug for ProductView
    def get_absolute_url(self):
        return reverse('webshop:shop-box', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('webshop:shop-add-cart', kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('webshop:shop-remove-cart', kwargs={
            'slug': self.slug
        })


class OrderBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    # Check how many with same title got added
    def __str__(self):
        return f'{self.quantity} of {self.box.title}'


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    discount_price = models.CharField(max_length=10, blank=True)
    category = models.CharField(max_length=2)
    description = models.CharField(max_length=750)
    label = models.CharField(choices=BOX_LABELS, max_length=1, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    box = models.ManyToManyField(OrderBox)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
