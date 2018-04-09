from django import forms

MENU_ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class AddMenuItemForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=MENU_ITEM_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
                                