from django.contrib import admin
from website.models import *

class StdAdmin(admin.ModelAdmin):
    list_display = ('std_name','std_roll','std_class')

admin.site.register(student_info,StdAdmin)
