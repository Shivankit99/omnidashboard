from django.contrib import admin
from . models import employee,rem,leave

admin.site.register(employee)
admin.site.register(leave)
admin.site.register(rem)