import django_tables2 as tables

from django_tables2 import TemplateColumn
from .models import Rent
from django_tables2.utils import A


class RentTable(tables.Table):
    # detail = tables.LinkColumn('rent_detail', args=[A('pk')], text='Detail')
    # delete = tables.TemplateColumn(
    #     '<form action="{% url "rent_delete" record.pk %}" method="post">{% csrf_token %}<button type="submit" '
    #     'class="btn btn-danger">Delete</button></form>')
    detail = TemplateColumn('<a href="{% url "films:rent_detail" record.pk %}" class="btn btn-info btn-sm">Detail</a>')
    delete = TemplateColumn('<a href="{% url "films:rent_delete" record.pk %}" class="btn btn-danger btn-sm">Delete</a>')

    class Meta:
        model = Rent
        fields = ('user', 'item', 'date_rent', 'actual_return', 'detail', 'delete')
        #view = TemplateColumn(template_name='administrator/index.html')
        template_name = 'django_tables2/bootstrap.html'
        order_by = ('-date_rent',)
