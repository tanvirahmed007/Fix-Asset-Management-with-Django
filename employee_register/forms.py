from django import forms
from django.forms import widgets
from.models import Assets



class AssetForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ('year_of_purchase', 'historical_cost', 'purchase_order', 'user', 
                 'location', 'specification', 'rate', 'accumulated_balance', 'book_value', 'position',
                 'bookValue', 'service', 'fromYear', 'result')
        
        widgets = {
            'bookValue': forms.TextInput(attrs={'class': 'form-control', 'id': 'bookvalue', 'onblur':"depreciation()"}),
            'service': forms.TextInput(attrs={'class': 'form-control', 'id': 'years', 'onblur':"depreciation()"}),
            'fromYear': forms.TextInput(attrs={'class': 'form-control', 'id': 'fromyear', 'onblur':"depreciation()"}),
            'result': forms.TextInput(attrs={'class': 'form-control', 'id': 'hgf'}),
        }
        
        labels = {
            'year_of_purchase': 'Year of purchase',
            'historical_cost': 'Historical Cost',
            'purchase_order': 'Purchase Order',
            'user': 'User',
            'location': 'Location',
            'specification': 'Specification',
            'rate': 'Rate',
            'accumulated_balance': 'Accumulated Balance',
            'book_value': 'Book Value',
            'bookValue': 'Book Value',
            'service': 'Service of years',
            'fromYear': 'From Year',
            'result': 'Result',
            
            
            

        }

    def __init__(self, *args, **kwargs):
        super(AssetForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        

        