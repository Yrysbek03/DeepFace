from django.contrib import admin

from main.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'coffee_type', 'file', 'age', 'gender', 'ethnicity', 'created']
    list_display_links = ['client_id']


admin.site.register(Document, DocumentAdmin)
