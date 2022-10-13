from django.db import models


class Person(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    mail = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    sex = models.CharField(max_length=255, verbose_name='Пол')
    id_category = models.ForeignKey('CategoryPerson', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"Person {self.name} id={self.uuid} {self.id_category}"


class CategoryPerson(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"CategoryPerson {self.name} id={self.uuid}"


class Material(models.Model):
    """Модель материалов"""
    uuid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Materials {self.name} id={self.uuid}"


class Services(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Services {self.name} id={self.uuid}"


class Order(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    uuid_person = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="orders")
    uuid_services = models.ForeignKey('Services', on_delete=models.CASCADE, related_name="orders")
    date_time = models.DateField()
    profit = models.IntegerField()
