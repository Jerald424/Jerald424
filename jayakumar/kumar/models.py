from django.db import models

# Create your models here.


class flipkart(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)

    class Meta:
        verbose_name = ("flipkart")
        verbose_name_plural = ("flipkarts")

    def __str__(self):
        return self.name


class items(models.Model):
    name = models.CharField(("Item Name"), max_length=50)

    class Meta:
        verbose_name = ("items")
        verbose_name_plural = ("items")

    def __str__(self):
        return self.name


class morning(models.Model):

    morning_item = models.ForeignKey(items, verbose_name=(
        "Morning Item"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("morning")
        verbose_name_plural = ("mornings")

    def __str__(self):
        return self.name


class admin(models.Model):

    adminname = models.CharField(max_length=50, null=True)
    adminpassword = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("admin")
        verbose_name_plural = ("admins")

    def __str__(self):
        return self.name


class morningitems(models.Model):

    idly = models.CharField(max_length=50, null=True)
    dosa = models.CharField(max_length=50, null=True)
    tea = models.CharField(max_length=50, null=True)
    pongal = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = ("morningitems")
        verbose_name_plural = ("morningitemss")

    def __str__(self):
        return self.name


class morningfood(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(max_length=50, null=True)
    count = models.IntegerField(max_length=50, null=True)
    img = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = ("morningitems")
        verbose_name_plural = ("morningitemss")

    def __str__(self):
        return self.name


class morningfoodcart(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(max_length=50, null=True)
    count = models.IntegerField(max_length=50, null=True)
    img = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = ("morningfoodcart")
        verbose_name_plural = ("morningfoodcarts")

    def __str__(self):
        return self.name


class coffee(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(max_length=50, null=True)
    count = models.IntegerField(max_length=50, null=True)
    img = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = ("coffee")
        verbose_name_plural = ("coffees")

    def __str__(self):
        return self.name


class coffeecart(models.Model):

    name = models.CharField(max_length=50, null=True)
    price = models.IntegerField(max_length=50, null=True)
    count = models.IntegerField(max_length=50, null=True)
    img = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = ("coffeecart")
        verbose_name_plural = ("coffeecarts")

    def __str__(self):
        return self.name
