from django import forms
from django.forms import ModelForm
from .models import Svj
from .models import Customer
from .models import Gsm_modul
from .models import Flat
from .models import Main_electrometer
from .models import Sub_electrometer
from .models import Solar_electrometer



class SvjForm(ModelForm):
	class Meta:
		model = Svj
		fields = '__all__'


		labels = {'from_date':'datum založení',
				  'to_date' : 'datum ukončení',
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
		 
		
		'address_street': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Adresa:',}),
		'address_orientation_number': forms.NumberInput(attrs={'class': 'form-control', }),
		'address_number_subscription': forms.NumberInput(attrs={'class': 'form-control', }),
		'address_city': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Adresa:',}), 
		'address_postal_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 10200:',}),

		'rodne_cislo': forms.NumberInput(attrs={'class': 'form-control',}),
		
		'zdravotni_prohlidka': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Zdravotní prohlídka DO: (RRRR-MM-DD)',}), 
		'registr_csar': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}), 
		'registr_zavodni_csar': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'registr_wrrc': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'tanecnik': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}), 
		'trener': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'porotce': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'}),
		'odborny_dozor': forms.CheckboxInput(attrs={'class': 'form-check form-check-inline'})
		}



class Gsm_modulForm(ModelForm):
	class Meta:
		model = Gsm_modul
		fields = '__all__'

		labels = {'from_date':'datum založení',
				  'to_date' : 'datum odpojení',
				  
					}


		widgets = {
		
		'identification_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'e.g. solar_x',}), 
		'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum založení: (DD.MM.RRRR)',}),
		'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Datum odpojení: (DD.MM.RRRR)',}), 
		'status': forms.Select(attrs={'class': 'form-control'}),
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}





class Flat(ModelForm):
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
		'status': forms.Select(attrs={'class': 'form-control'}),
		'gsm_modul': forms.Select(attrs={'class': 'form-control'}),
		'owner': forms.Select(attrs={'class': 'form-control'}),
		'owner_from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Majitel od: (DD.MM.RRRR)',}),
		'owner_to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Majitel do: (DD.MM.RRRR)',}),
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
		'status': forms.Select(attrs={'class': 'form-control'}),
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
		'status': forms.Select(attrs={'class': 'form-control'}),
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
		'status': forms.Select(attrs={'class': 'form-control'}),
		'svj': forms.Select(attrs={'class': 'form-control'}), 
		
		}
		