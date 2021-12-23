from django.contrib import admin
from django.contrib.auth import admin as u_admin
from accounts.models import User
# Register your models here.

admin.site.register(User, u_admin.UserAdmin)



