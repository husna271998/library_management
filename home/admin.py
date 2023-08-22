from django.contrib import admin
from . models import Books,LoginRecord,SignupRecord,MembersRecord
# Register your models here.
admin.site.register(LoginRecord)
admin.site.register(Books)
admin.site.register(SignupRecord)
admin.site.register(MembersRecord)
