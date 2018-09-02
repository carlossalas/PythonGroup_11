from django import forms


class FilterForm(forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }
        )
    )

    sort = forms.ChoiceField(
        choices=(('newest', 'Más Reciente'), ('latest', 'Más antiguo')),
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }
        )
    )
