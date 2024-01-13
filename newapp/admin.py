from django.contrib import admin
from .models import Member

#đăng ký mô hình member trong trang admin
class MemberAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country","email","age","salary"

admin.site.register(Member,MemberAdmin)