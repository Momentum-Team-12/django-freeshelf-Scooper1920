from django.contrib import admin
from .models import Book
from .models import User
from .models import Category
from .models import Favorite


admin.site.register(User)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Favorite)
