from django.contrib import admin
from django.contrib.auth.models import Group

from . import models

admin.site.unregister(Group)
admin.site.register(models.TelegramUser)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.UserOrder)
admin.site.register(models.Location)
