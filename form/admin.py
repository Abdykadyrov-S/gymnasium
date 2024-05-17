from os import path

from django.contrib import admin
from .models import *


# from .resources import BookResource

# Register your models here.
admin.site.site_header  =  '"ЫЙМАН" ГИМНАЗИЯСЫ'
admin.site.site_title  =  '"ЫЙМАН" ГИМНАЗИЯСЫ'
admin.site.index_title  =  '"ЫЙМАН" ГИМНАЗИЯСЫ'
class CommentAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('full_name', 'class_of_year', 'date_of_saving')
    # add filtering by date
    list_filter = ('full_name',)
    # add search field
    search_fields = ['full_name']
    readonly_fields = ['full_name', 'class_of_year', "birth_day", "class_of_year", "region", "phone_number_student",
                       "name_of_dud_mum", "phone_of_dud_mum", "name_guardian",
                       "phone_guardian", "whatsapp", "interesting_lesson", "success", "hobbies", "gender",
                       'date_of_saving']


class YourModelAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<uuid:carrier_id>/carrier-report.pdf', self.pdf_view),
        ]
        return custom_urls + urls


admin.site.register(Student, CommentAdmin)

