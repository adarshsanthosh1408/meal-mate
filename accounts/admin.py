from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentImage)
admin.site.register(MenuItem)
admin.site.register(Transaction)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Feedback)