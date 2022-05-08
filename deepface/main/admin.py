from django.contrib import admin

from main.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'age', 'gender', 'ethnicity']
    list_display_links = ['id']


admin.site.register(Document, DocumentAdmin)
