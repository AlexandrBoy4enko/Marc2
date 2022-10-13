from django.contrib import admin
from .models import Person, Material, Services, Order, CategoryPerson

admin.site.register(Person)
admin.site.register(Material)
admin.site.register(Services)
admin.site.register(Order)
admin.site.register(CategoryPerson)
