from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=30)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name_kor = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    temperature = models.CharField(max_length=10, null=True)
    is_new = models.BooleanField(null=True)
    is_best = models.BooleanField(null=True)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=2000)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'sizes'

class Nutrient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Size, on_delete=models.PROTECT, null=True)
    kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugar = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fat = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    serve = models.IntegerField(null=True)
    serve_type = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'nutrients'
        unique_together = (('product', 'size'),)

class AllergyCauses(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'allergy_causes'

class ProductAllergyCauses(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    allergy_causes = models.ForeignKey(AllergyCauses, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product_allergy_causes'
        unique_together = (('product', 'allergy_causes'),)

class Milk(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'milks'

class MilkSelection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    milk = models.ForeignKey(Milk, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'milk_selections'
        unique_together = (('product', 'milk'),)
