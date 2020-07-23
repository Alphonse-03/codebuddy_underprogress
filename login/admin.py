from django.contrib import admin

# Register your models here.
from .models import Java,Cpp,Python,Django,C,Javascript

admin.site.register(Java)
admin.site.register(Cpp)
admin.site.register(Python)
admin.site.register(Javascript)
admin.site.register(C)
admin.site.register(Django)