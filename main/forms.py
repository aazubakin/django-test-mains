from django import forms


class FileForm(forms.Form):
    title = forms.CharField()
    file = forms.FileField()

    class Meta:
        abstract = True


class AddBill(FileForm):
    pass


class AddClients(FileForm):
    pass
