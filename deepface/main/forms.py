from django import forms

from main.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['age', 'ethnicity', 'gender', 'pixels']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'type': "file", 'class': "form-control", 'id': "inputGroupFile04",
                                                 'aria-describedby': "inputGroupFileAddon04", 'aria-label': "Upload"})
