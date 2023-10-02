import django_filters
from .models import DonneeECG

class DonneeECGFilter(django_filters.FilterSet):
    # ... Your other filters ...

    # Define a custom filter for frequence_cardiaque
    frequence_cardiaque = django_filters.NumberFilter(
        method='filter_frequence_cardiaque',
        label='Frequence Cardiaque'
    )

    def filter_frequence_cardiaque(self, queryset, name, value):
        # Calculate frequence_cardiaque for filtering
        queryset = queryset.annotate(
            computed_frequence_cardiaque=60000 / django.db.models.F('rr_interval')
        )
        return queryset.filter(computed_frequence_cardiaque=value)

    class Meta:
        model = DonneeECG
        fields = {
            'sante_patient': ['exact', 'contains'],
            'interval_pr': ['exact', 'gte', 'lte'],
            #'frequence_cardiaque': ['exact', 'gte', 'lte']
            # Add other fields here...
        }
