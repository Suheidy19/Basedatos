from django.contrib import admin
from .models import Client, Doctor, Vendor,Provider,Service,Mascot,Product,Office,Cite,Sale
# Register your models here.
admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Vendor)
admin.site.register(Provider)
admin.site.register(Service)
admin.site.register(Mascot)
admin.site.register(Product)
admin.site.register(Office)
admin.site.register(Cite)
admin.site.register(Sale)


