from dal import autocomplete

from django.conf.urls import url

from .models import TModel


class LinkedDataView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = super(LinkedDataView, self).get_queryset()
        print(self.forwarded.get('checkbox', None))
        possessor = self.forwarded.get('possessor', None)
        secret = self.forwarded.get('secret', None)

        if secret != 42:
            return qs.none()

        if possessor:
            return qs.filter(owner_id=possessor)

        return qs


urlpatterns = [
    url(
        '^linked_data/$',
        LinkedDataView.as_view(model=TModel),
        name='linked_data_rf'
    ),
]
