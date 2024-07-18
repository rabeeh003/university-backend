from django.contrib import admin
from .models import Course, Department, Semester, Subject, Silabus
from django.utils.html import format_html

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_preview', 'description', 'qualification', 'duration', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description', 'qualification')

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.icon.url))
        return ''
    icon_preview.allow_tags = True
    icon_preview.short_description = 'Icon'

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course', 'is_active')
    list_filter = ('is_active', 'course')
    search_fields = ('name', 'description')

class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'department')
    list_filter = ('course__name', 'department__name',)
    search_fields = ('name',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    search_fields = ('name', 'author')

class SilabusAdmin(admin.ModelAdmin):
    list_display = ('semester', 'department', 'course', 'subject', 'silabus')
    list_filter = ('department__name', 'course__name', 'subject__name')
    # search_fields = ('semester','department','course',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Silabus, SilabusAdmin)