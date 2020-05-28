
from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.register(models.Biology)
admin.site.register(models.Entertainment)
admin.site.register(models.History)
admin.site.register(models.Literature)
admin.site.register(models.Science)
admin.site.register(models.Sport)
