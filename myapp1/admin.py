from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'original_price', 'discount_price', 'get_discount_percentage')
    search_fields = ('title', 'language')
    list_filter = ('language',)
