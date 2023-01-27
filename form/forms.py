from django.forms import ModelForm
from form.models import BookInspection


class BookInspectionForm(ModelForm):
    class Meta:
        model = BookInspection
        fields = "__all__"


form = BookInspectionForm()


bookinspection = BookInspection.objects.get(pk=1)
form = BookInspectionForm(instance=bookinspection)

