from django.contrib import admin
from .import models

admin.site.register(models.Course)
admin.site.register(models.Paper)
admin.site.register(models.Questions)
admin.site.register(models.Answer)
