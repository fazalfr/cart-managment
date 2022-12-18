from django.contrib import admin
from .models import users
from .models import Item


admin.site.register(users)
admin.site.register(Item)