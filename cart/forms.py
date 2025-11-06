from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        label='Кількість',
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'style': 'width: 75px; text-align: center;'
        })
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        self.cart = kwargs.pop('cart', None)
        super().__init__(*args, **kwargs)

        if self.product:
            self.fields['quantity'].widget.attrs.update({
                'max': self.product.stock,
            })

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        current_quantity_in_cart = 0
        if self.cart and str(self.product.id) in self.cart.cart:
            if not self.cleaned_data.get('update'):
                current_quantity_in_cart = self.cart.cart[str(self.product.id)]['quantity']

        total_quantity = quantity + current_quantity_in_cart

        if self.product and total_quantity > self.product.stock:
            raise forms.ValidationError(
                f'На складе осталось только {self.product.stock} шт.'
            )
        return quantity