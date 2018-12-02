from django.contrib import admin

# Register your models here.
from .models import Actor, Producer, Movie

admin.site.register(Actor)
admin.site.register(Producer)
admin.site.register(Movie)