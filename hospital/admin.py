from django.contrib import admin

from hospital.models import Hospital, Stock, Inventory


class HospitalAdmin(admin.ModelAdmin):
    pass

class StockAdmin(admin.ModelAdmin):
    pass

class InventoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Inventory, InventoryAdmin)
