from django.contrib import admin
from beauty.api.core.models.models import Person, Material, Services, Order, CategoryPerson

admin.site.register(Person)
admin.site.register(Material)
admin.site.register(Services)
admin.site.register(Order)
admin.site.register(CategoryPerson)
