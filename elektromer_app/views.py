from django.shortcuts import render
from django.http import HttpResponse
from .models import Svj
from .models import Customer
from .models import Gsm_modul
from .models import Flat
from .models import Main_electrometer
from .models import Sub_electrometer
from .models import Solar_electrometer


# Create your views here.



def home (request):
	return render (request, 'elektromer_app/home.html', {})



def svj (request):


	all_svj = Svj.objects.all()

	return render (request, 'elektromer_app/svj.html', {'all_svj': all_svj,})


def customer(request, pk):

	customer = Customer.objects.get(id=pk)

	customer_flats = customer.flat_set.all()

	flat_count = customer_flats.count()


	return render (request, 'elektromer_app/customer.html', {'customer' : customer, 
		'customer_flats': customer_flats,
		'flat_count': flat_count,})





def customers(request):

	all_customers = Customer.objects.all()
	
	
	return render (request, 'elektromer_app/customers.html', {'all_customers': all_customers, 'custormer_count': customers_count})

"""

def chairman(request):
	return render (request, 'elektromer_app/chairman.html', {})


def sub_chairman(request):
	return render (request, 'elektromer_app/sub_chairman.html', {})

"""


def gsm_modul(request):

	all_gsm_moduls = Gsm_modul.objects.all()

	return render (request, 'elektromer_app/gsm_modul.html', {'all_gsm_moduls': all_gsm_moduls})


def flat(request):

	all_flats = Flat.objects.all()

	return render (request, 'elektromer_app/flat.html', {'all_flats': all_flats})


def main_electrometer(request):

	all_main_electrometers = Main_electrometer.objects.all()

	return render (request, 'elektromer_app/main_electrometer.html', {'all_main_electrometers': all_main_electrometers})


def sub_electrometer(request):

	all_sub_electrometers = Sub_electrometer.objects.all()

	return render (request, 'elektromer_app/sub_electrometer.html', {'all_sub_electrometers': all_sub_electrometers})


def solar_electrometer(request):

	all_solar_electrometers = Solar_electrometer.objects.all()

	return render (request, 'elektromer_app/solar_electrometer.html', {'all_solar_electrometers': all_solar_electrometers})

"""

def balance_main(request):
	return render (request, 'elektromer_app/balance_main.html', {})


def balance_sub(request):
	return render (request, 'elektromer_app/balance_sub.html', {})


def balance_solar(request):
	return render (request, 'elektromer_app/balance_solar.html', {})
"""
