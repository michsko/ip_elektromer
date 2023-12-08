from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Svj
from .models import Customer
from .models import Gsm_modul
from .models import Flat
from .models import Main_electrometer
from .models import Sub_electrometer
from .models import Solar_electrometer
from .models import Balance_main
from .models import Balance_sub
from .models import Balance_solar




class Balance_mainForm(ModelForm):
	class Meta:
		model = Balance_main
		fields = '__all__'



		labels = {'balance': 'stav',
				  'from_date':'datum založení',
				  'to_date' : 'datum odpojení',

					}


		widgets = {
		
		'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'e.g. 1234567.123',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 

		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}


class Balance_subForm(ModelForm):
	class Meta:
		model = Balance_sub
		fields = '__all__'



		labels = {'balance': 'stav',
				  'from_date':'datum založení',
				  'to_date' : 'datum odpojení',

					}


		widgets = {
		
		'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'e.g. 1234567.123',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 

		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}


class Balance_solarForm(ModelForm):
	class Meta:
		model = Balance_solar
		
		fields = '__all__'



		labels = {'balance': 'stav',
				  'from_date':'datum založení',
				  'to_date' : 'datum odpojení',

					}


		widgets = {
		
		'balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'e.g. 1234567.123',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 

		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

		labels = {
		'name': 'Jméno', 
		'surname': 'Příjmení', 
		'phone': 'Telefon',
		'address_street': 'Bydliště - ulice', 
		'address_orientation_number': 'Bydliště - číslo orientační', 
		'address_number_subscription': 'Bydliště - číslo popisné', 
		'address_city': 'Bydliště - město',
		'address_postal_code': 'Bydliště - PSČ',
		'contract_number': 'Číslo smlouvy', 
		

		}

		widgets = {'klub': forms.Select(attrs={'class': 'form-control'}), 
		'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jméno:',}), 
		'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Příjmení:',}), 
		'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Telefonní číslo:'}),
		'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email:',}), 
		'datum_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum narození: (RRRR-MM-DD)',}), 
		'address_street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa:',}),
		'address_orientation_number': forms.NumberInput(attrs={'class': 'form-control', }),
		'address_number_subscription': forms.NumberInput(attrs={'class': 'form-control', }),
		'address_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa:',}), 
		'address_postal_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10200:',}),
		}





class FlatForm(ModelForm):
	class Meta:
		model = Flat
		fields = '__all__'


		labels = {'flat':'byt číslo',
				  'from_date':'datum založení',
				  'to_date' : 'datum odpojení',
				  'owner' : 'majitel',
				  'owner_from_date': 'majitel od',
				  'owner_to_date': 'majitel do',

					}


		widgets = {
		
		'flat_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g. solar_x',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 
		
		'gsm_modul': forms.Select(attrs={'class': 'form-control'}),
		'owner': forms.Select(attrs={'class': 'form-control'}),
		'owner_from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Majitel od: (DD.MM.RRRR)',}),
		'owner_to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Majitel do: (DD.MM.RRRR)',}),
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}




class Gsm_modulForm(ModelForm):
	class Meta:
		model = Gsm_modul
		fields = '__all__'

		labels = {'identification_number': 'Identifikátor',
				  'from_date':'datum založení',
				  'to_date' : 'datum odpojení',
				  
					}


		widgets = {
		
		'identification_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g. solar_x',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 
		
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}





class Main_electrometerForm(ModelForm):
	class Meta:
		model = Main_electrometer
		fields = '__all__'


		labels = {'from_date':'datum založení',
				  'to_date' : 'datum odpojení',
				  

					}


		widgets = {
		
		'identification_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g. solar_x',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 
		
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}



class Sub_electrometerForm(ModelForm):
	class Meta:
		model = Sub_electrometer
		fields = '__all__'
		
		labels = {'from_date':'datum založení',
				  'to_date' : 'datum odpojení',
				  'flat' : 'byt',

					}


		widgets = {
		
		'identification_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g. solar_x',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 
		
		'flat': forms.Select(attrs={'class': 'form-control'}),
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}
		

 

class Solar_electrometerForm(ModelForm):
	class Meta:
		model = Solar_electrometer
		fields = '__all__'


		labels = {'from_date':'datum založení',
				  'to_date' : 'datum odpojení',

					}


		widgets = {
		
		'identification_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g. solar_x',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}
		


class SvjForm(ModelForm):
	class Meta:
		model = Svj
		fields = '__all__'


		labels = {'identification_number': 'Identifikátor',
				  'from_date':'Datum založení',
				  'to_date' : 'Datum ukončení',
				  'name' : 'Název',
				  'address_street': 'Ulice', 
				  'address_orientation_number': 'číslo orientační', 
				  'address_number_subscription': 'číslo popisné',
				  'address_city': 'Město',
				  'address_postal_code': 'PSČ', 
				  'account_number': 'Číslo účtu',
				  'energy_supply' : 'Dodavatel',
				  'number_of_flats': 'Počet bytů',

					}

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']