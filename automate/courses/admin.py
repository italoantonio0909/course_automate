from django.contrib import admin

from .models import Course
from .services import course_assistance


@admin.action(description='Marcar asistencia')
def assistance(modeladmin, request, queryset):
    # course_assistance(course_id=queryset[0].id)
    print('id del curso', queryset[0].id)
    # course_create()


class CourseAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title',)
    actions = [assistance]


admin.site.register(Course, CourseAdmin)
