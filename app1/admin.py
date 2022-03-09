from django.contrib import admin
from .models import new_users
from .models import Event
from .models import details,contact
# Register your models here.
admin.site.register(new_users)
admin.site.register(Event)
admin.site.register(details)
admin.site.register(contact)