from django.contrib import admin
from .models import Articles
# Register your models here.


@admin.register(Articles)
class ArticlesADM(admin.ModelAdmin):
    pass

