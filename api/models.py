from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Department(models.Model):
    """This class represents the department model."""
    id = models.CharField(max_length=225, blank=False, unique=True, primary_key=True)
    description = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.description)

class Brand(models.Model):
    """This class represents the brand model."""
    id = models.CharField(max_length=225, blank=False, unique=True, primary_key=True)
    description = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.description)

class Product(models.Model):
    """  """
    id = models.CharField(max_length=225, blank=False, unique=True, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=False)
    last_price = models.FloatField(default=0.00, validators=[MinValueValidator(0)])
    max_price = models.FloatField(default=0.00, validators=[MinValueValidator(0)])
    min_price = models.FloatField(default=0.00, validators=[MinValueValidator(0)])
    avg_price = models.FloatField(default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return "{}".format(self.description)


class Product_Pss(models.Model):
    """ """
    class Meta(object):
        unique_together = [("product", "date")]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.product)


class Purchase(models.Model):
    """ """
    date = models.DateTimeField()
    value = models.FloatField(default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return "{}".format(self.date)


class Item(models.Model):
    """ """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    qtd = models.PositiveIntegerField(default=1)
    sub_total = models.FloatField(default=0.00, validators=[MinValueValidator(0)])

    def __str__(self):
        return "{}".format(self.product)

class Market(models.Model):
    """ """
    id = models.CharField(max_length=225, blank=False, unique=True, primary_key=True)
    description = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=257)

    def __str__(self):
        return "{}".format(self.description)