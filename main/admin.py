from django.contrib import admin
from main import models

# Register your models here.


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass
