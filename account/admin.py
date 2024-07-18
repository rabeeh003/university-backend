from django.contrib import admin
from .models import College, Student, Teacher
from django.utils.html import format_html

class CollegeAdmin(admin.ModelAdmin):
    list_display = ('user','profile_image_tag','place', 'phone', 'district')
    search_fields = ('place', 'district', 'principal', 'user')
    list_filter = ('district',)
    def profile_image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 50px; max-height: 50px;" />'.format(obj.profile.url))
    profile_image_tag.short_description = 'Profile Image'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'batch', 'phone', 'parent_name', 'relation', 'place', 'district', 'college', 'status', 'profile_image_tag')
    search_fields = ('user__username', 'parent_name', 'place', 'district')
    list_filter = ('college', 'batch', 'district','status')
    def profile_image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 50px; max-height: 50px;" />'.format(obj.profile.url))
    profile_image_tag.short_description = 'Profile Image'

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'degree', 'college', 'exam_invigilator', 'profile_image_tag')
    search_fields = ('user__username', 'degree', 'college__place')
    list_filter = ('college','is_principal','is_active',)
    def profile_image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 50px; max-height: 50px;" />'.format(obj.profile.url))
    profile_image_tag.short_description = 'Profile Image'


admin.site.register(College, CollegeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
