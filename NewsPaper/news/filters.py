from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Category
import django.forms


class PostFilter(FilterSet):
    category = ModelChoiceFilter(
            field_name='categories',
            queryset=Category.objects.all(),
            label='Категория',
            empty_label='---------'
        )

    class Meta:

        model = Post

        fields = {

            'author': ['exact'],

            'categories': ['exact'],
        }