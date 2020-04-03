from django.forms import ModelForm, HiddenInput, RadioSelect
from hospital.models import Hospital, Inventory, Stock


class InventoryForm(ModelForm):

    class Meta:
        model = Inventory
        fields = '__all__'
        widgets = {
            'hospital': HiddenInput(),
            'stock': HiddenInput(),
            'supplies_left': RadioSelect(),
        }
