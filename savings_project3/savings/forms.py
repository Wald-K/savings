from django.forms import ModelForm, ModelChoiceField
from .models import Client, Deposit, Bank


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname']

class DepositForm(ModelForm):
    # these are sorted so they are distinguish
    client = ModelChoiceField(queryset = Client.objects.order_by('lastname', 'firstname'))
    bank = ModelChoiceField(queryset = Bank.objects.order_by('name'))
    
    class Meta:
        model = Deposit
        fields = '__all__'

