from django.contrib import admin
from .models import Category, Ticket


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Ticket, TicketAdmin)
