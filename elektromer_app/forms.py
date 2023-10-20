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



class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'



class Gsm_modulForm(ModelForm):
	class Meta:
		model = Gsm_modul
		fields = '__all__'



class Flat(ModelForm):
	class Meta:
		model = Flat
		fields = '__all__'



class Main_electrometerForm(ModelForm):
	class Meta:
		model = Main_electrometer
		fields = '__all__'



class Sub_electrometerForm(ModelForm):
	class Meta:
		model = Sub_electrometer
		fields = '__all__'


 

class Solar_electrometerForm(ModelForm):
	class Meta:
		model = Main_electrometer
		fields = '__all__'