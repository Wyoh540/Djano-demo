from django.contrib import admin
from staff.models import Staff


# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ('cn', 'ori_hp', 'ori_atk', 'ori_def', 'ori_res', 'ori_dt', 'ori_dc', 'ori_block', 'ori_cd', 'feature')


admin.site.register(Staff, StaffAdmin)