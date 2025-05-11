from django import forms
from django.core.exceptions import ValidationError

from .models import Product, Category
from .constants import FORBIDDEN_WORDS

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control-lg text-primary text-center',
            'placeholder': 'Введите наименование'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите стоимость'
        })



    def clean_name(self):
        name = self.cleaned_data['name']
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(f"Название содержит запрещённое слово: '{word}'")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(f"Описание содержит запрещённое слово: '{word}'")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            valid_mime_types = ['image/jpeg', 'image/png']
            if image.content_type not in valid_mime_types:
                raise forms.ValidationError('Изображение должно быть в формате JPEG или PNG.')

            max_size = 5 * 1024 * 1024
            if image.size > max_size:
                raise forms.ValidationError('Размер изображения не должен превышать 5 МБ.')

        return image