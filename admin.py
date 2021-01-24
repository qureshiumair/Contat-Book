from django.contrib import admin
from .models import contact
# Register your models here.
class userAdminSite(admin.ModelAdmin):
    model=contact
    fields=['name','relationship','email','phone','address']
    list_display=('name','relationship','email','phone','address')

admin.site.register(contact,userAdminSite)