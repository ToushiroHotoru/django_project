from django.contrib import admin

# Register your models here.
from .models import Service, User, Animal, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ("title", "status")
    list_filter = ("user", "animal")
    search_fields = ("title", "user")
    list_editable = ("status",)


admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Service)
admin.site.register(Order, OrderAdmin)


