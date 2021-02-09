from django.db import models


class Service(models.Model):
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", blank=True, null=True)
    price = models.PositiveSmallIntegerField("Цена", default=100)
    image = models.ImageField("Изображение", upload_to="services/")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Animal(models.Model):
    name = models.CharField("Кличка", max_length=50)
    type = models.CharField("Вид питомца", max_length=100)
    image = models.ImageField("Фото питомца", upload_to="pets/")
    services = models.ManyToManyField(Service, verbose_name="услуга", related_name="service")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"


class User(models.Model):
    name = models.CharField("ФИО", max_length=50)
    tel_number = models.PositiveSmallIntegerField("Номер телефона", default=0, help_text="начинать с семерки")
    animals = models.ManyToManyField(Animal, verbose_name="питомец", related_name="animal")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Order(models.Model):
    title = models.CharField("Название заказа", max_length=100)
    user = models.CharField("ФИО", max_length=50)
    animal = models.CharField("Кличка", max_length=50)
    status = models.BooleanField("Статус заказа", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"