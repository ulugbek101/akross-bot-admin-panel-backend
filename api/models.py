from django.db import models


class TelegramUser(models.Model):
    LANGUAGE_CODE_CHOICES = (
        ('uz', 'uz'),
        ('ru', 'ru'),
        ('en', 'en'),
    )

    STATUS_CHOICES = (
        ('bronze', '🥉 Bronze'),
        ('silver', '🥈 Silver'),
        ('gold', '🥇 Gold'),
        ('platinum', '🌟 Platinum'),
    )

    fullname = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    telegram_id = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    language_code = models.CharField(max_length=2, choices=LANGUAGE_CODE_CHOICES, default='uz', db_default='uz')
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='bronze', db_default='bronze')
    order_count = models.IntegerField(default=0)
    last_visited_place = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'users'


class Category(models.Model):
    BELONGS_TO_CHOICES = (
        ('foods', 'Foods'),
        ('others', 'Others'),
    )

    name_uz = models.CharField(max_length=200, unique=True)
    name_ru = models.CharField(max_length=200, unique=True)
    name_en = models.CharField(max_length=200, unique=True)
    photo = models.CharField(max_length=200)
    has_subcategory = models.BooleanField(default=False)
    category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories', verbose_name='Subcategory of')
    belongs_to = models.CharField(max_length=200, choices=BELONGS_TO_CHOICES, default=BELONGS_TO_CHOICES,
                                  db_default='foods')

    def __str__(self):
        return self.name_en

    class Meta:
        db_table = 'categories'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    subcategory = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='sub_categories')
    name_uz = models.CharField(max_length=200, unique=True)
    name_ru = models.CharField(max_length=200, unique=True)
    name_en = models.CharField(max_length=200, unique=True)
    desc_uz = models.CharField(max_length=200, blank=True, null=True)
    desc_ru = models.CharField(max_length=200, blank=True, null=True)
    desc_en = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    photo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name_en

    class Meta:
        db_table = 'products'


class Location(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='locations')
    coordinates = models.CharField(max_length=200)
    full_address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('user', 'full_address')
        db_table = 'locations'

    def __str__(self):
        return self.full_address


class Cart(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ('user', 'product')
        db_table = 'cart'


class Order(models.Model):
    order_id = models.IntegerField()
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=5)
    created_date = models.DateField()
    created_time = models.TimeField()

    def __str__(self):
        return f"Order {self.order_id} by {self.user}"

    class Meta:
        db_table = 'orders'


class UserOrder(models.Model):
    user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='user_orders')
    deliver_type = models.CharField(max_length=50)
    deliver_time = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=50, default="not_accepted")
    created_date = models.DateField()
    created_time = models.TimeField()
    payment_method = models.CharField(max_length=20)

    def __str__(self):
        return f"User Order {self.id} by {self.user}"

    class Meta:
        db_table = 'user_orders'
