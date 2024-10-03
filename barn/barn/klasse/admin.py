from django.contrib import admin
from .models import Barn, Klasse, Personale

# Register your models here.
admin.site.register(Barn)
admin.site.register(Personale)
admin.site.register(Klasse)