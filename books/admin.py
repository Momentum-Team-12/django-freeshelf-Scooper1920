from django.contrib import admin
from .models import Book
from .models import User


admin.site.register(User)
admin.site.register(Book)
