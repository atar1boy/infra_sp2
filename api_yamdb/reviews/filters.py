from django_filters import rest_framework as filters

from .models import Title


class TitleFilters(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name'
    )
    category = filters.CharFilter(
        field_name='category__slug'
    )
    genre = filters.CharFilter(
        field_name='genre__slug'
    )

    class Meta:
        model = Title
        fields = ['name', 'year', 'genre', 'category']
