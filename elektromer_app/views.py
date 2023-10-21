from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Svj
from .models import Customer
from .models import Gsm_modul
from .models import Flat
from .models import Main_electrometer
from .models import Sub_electrometer
from .models import Solar_electrometer
from .forms import CustomerForm
from .forms import Gsm_modulForm
from .forms import Main_electrometerForm
from .forms import Sub_electrometerForm
from .forms import Solar_electrometerForm

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
	
	form = CustomerForm()
	
	return render (request, 'elektromer_app/customers.html', {'all_customers': all_customers, 'form': form, })



def customer_add(request):
	
	submitted=False
	
	if request.method == 'POST':
		form=CustomerForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Zákazník byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("customers")

	else:
	
		form = CustomerForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/gsm_moduls.html', {'form': form, 'submitted': submitted,})

	


def customer_update(request, pk):
	
	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form=CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('/customers')

	return render(request, 'elektromer_app/customer.html', {'form': form,})



def customer_delete(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()
	messages.success(request("Zákazník byl úspěšně smazán."))
	return redirect('/customers')






"""

def chairman(request):
	return render (request, 'elektromer_app/chairman.html', {})


def sub_chairman(request):
	return render (request, 'elektromer_app/sub_chairman.html', {})

"""




def gsm_modul(request, pk):

	gsm_modul = Gsm_modul.objects.get(id=pk)

	return render (request, 'elektromer_app/gsm_modul.html', {'gsm_modul':gsm_modul})


def gsm_moduls(request):

	all_gsm_moduls = Gsm_modul.objects.all()
	form = Gsm_modulForm()

	return render (request, 'elektromer_app/gsm_moduls.html', {'all_gsm_moduls': all_gsm_moduls, 'form': form})


def gsm_modul_add(request):
	
	
	submitted=False
	
	if request.method == 'POST':
		form=Gsm_modulForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Gsm modul byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("gsm_moduls")

	else:
	
		form = Gsm_modulForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/gsm_moduls.html', {'form': form, 'submitted': submitted,})

	

def gsm_modul_update(request, pk):

	gsm_modul = Gsm_modul.objects.get(id=pk)
	form = Gsm_modulForm(instance=gsm_modul)

	if request.method == 'POST':
		form=Gsm_modulForm(request.POST, instance=gsm_modul)
		if form.is_valid():
			form.save()
			return redirect('/gsm_modul')

	return render(request, 'elektromer_app/gsm_modul_form.html', {'form': form,})


def gsm_modul_delete(request, pk):

	gsm_modul = Gsm_modul.objects.get(id=pk)
	gsm_modul.delete()
	messages.success(request("Gsm modul byl úspěšně smazán."))
	return redirect('/gsm_moduls')





def flat(request):

	all_flats = Flat.objects.all()

	return render (request, 'elektromer_app/flat.html', {'all_flats': all_flats})




def main_electrometer(request, pk):

	main_electrometer = Main_electrometer.objects.get(id=pk)

	return render (request, 'elektromer_app/main_electrometer.html', {'main_electrometer': main_electrometer})


def main_electrometers(request):

	all_main_electrometers = Main_electrometer.objects.all()
	form = Main_electrometerForm()

	return render (request, 'elektromer_app/main_electrometers.html', {'all_main_electrometers': all_main_electrometers, 'form': form, })


def main_electrometer_add(request):

	submitted=False
	
	if request.method == 'POST':
		form=Main_electrometerForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Hlavní elektroměr byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("main_electrometers")

	else:
	
		form = Main_electrometerForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/main_electrometers.html', {'form': form, 'submitted': submitted,})


def main_electrometer_update(request, pk):

	
	main_electrometer = Main_electrometer.objects.get(id=pk)
	form = Main_electrometerForm(instance=main_electrometer)

	if request.method == 'POST':
		form=Main_electrometerForm(request.POST, instance=main_electrometer)
		if form.is_valid():
			form.save()
			return redirect('/main_electrometers')

	return render(request, 'elektromer_app/main_electrometer_form.html', {'form': form,})




def main_electrometer_delete(request, pk):
	
	main_electrometer = Main_electrometer.objects.get(id=pk)
	main_electrometer.delete()
	messages.success(request("Hlavní elektroměr byl úspěšně smazán."))
	return redirect('/main_electrometers')





def sub_electrometer(request, pk):

	sub_electrometer = Sub_electrometer.objects.get(id=pk)

	return render (request, 'elektromer_app/sub_electrometer.html', {'sub_electrometer': sub_electrometer})



def sub_electrometers(request):

	all_sub_electrometers = Sub_electrometer.objects.all()

	form = Sub_electrometerForm()

	return render (request, 'elektromer_app/sub_electrometers.html', {'all_sub_electrometers': all_sub_electrometers, 'form': form})



def sub_electrometer_add(request):

	submitted=False
	
	if request.method == 'POST':
		form=Sub_electrometerForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Podružný elektroměr byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("sub_electrometers")

	else:
	
		form = Sub_electrometerForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/sub_electrometers.html', {'form': form, 'submitted': submitted})


def sub_electrometer_update(request, pk):

	
	sub_electrometer = Sub_electrometer.objects.get(id=pk)
	form = Sub_electrometerForm(instance=sub_electrometer)

	if request.method == 'POST':
		form=Sub_electrometerForm(request.POST, instance=sub_electrometer)
		if form.is_valid():
			form.save()
			return redirect('/sub_electrometers')

	return render(request, 'elektromer_app/sub_electrometer_form.html', {'form': form,})


def sub_electrometer_delete(request, pk):
	
	sub_electrometer = Sub_electrometer.objects.get(id=pk)
	sub_electrometer.delete()
	messages.success(request("Podružný elektroměr byl úspěšně smazán."))
	return redirect('/sub_electrometers')





def solar_electrometer(request, pk):

	solar_electrometer = Solar_electrometer.objects.get(id=pk)

	return render (request, 'elektromer_app/solar_electrometer.html', {'solar_electrometer': solar_electrometer})



def solar_electrometers(request):

	all_solar_electrometers = Solar_electrometer.objects.all()

	form = Solar_electrometerForm()

	return render (request, 'elektromer_app/solar_electrometers.html', {'all_solar_electrometers': all_solar_electrometers, 'form': form, })


def solar_electrometer_add(request):

	
	submitted=False
	
	if request.method == 'POST':
		form=Solar_electrometerForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Solární elektroměr byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("solar_electrometers")

	else:
	
		form = Solar_electrometerForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/solar_electrometers.html', {'form': form, 'submitted': submitted})


def solar_electrometer_update(request, pk):

	solar_electrometer = Solar_electrometer.objects.get(id=pk)
	form = Solar_electrometerForm(instance=solar_electrometer)

	if request.method == 'POST':
		form=Solar_electrometerForm(request.POST, instance=solar_electrometer)
		if form.is_valid():
			form.save()
			return redirect('solar_electrometers')



def solar_electrometer_delete(request, pk):

	solar_electrometer = Solar_electrometer.objects.get(id=pk)
	solar_electrometer.delete()
	messages.success(request,("Solární elektroměr byl úspěšně smazán."))

	return redirect('solar_electrometers')

	


"""

def balance_main(request):
	return render (request, 'elektromer_app/balance_main.html', {})


def balance_sub(request):
	return render (request, 'elektromer_app/balance_sub.html', {})


def balance_solar(request):
	return render (request, 'elektromer_app/balance_solar.html', {})
"""
