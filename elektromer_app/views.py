from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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
from .forms import SvjForm
from .forms import CustomerForm
from .forms import Gsm_modulForm
from .forms import Main_electrometerForm
from .forms import Sub_electrometerForm
from .forms import Solar_electrometerForm
from .forms import Balance_mainForm
from .forms import Balance_subForm
from .forms import Balance_solarForm
from .forms import FlatForm
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users
# Create your views here.




@login_required(login_url='login')
def home (request):
	return render (request, 'elektromer_app/home.html', {})

	

@login_required(login_url='login')
def balance_main(request, pk):

	balance_main = Balance_main.objects.get(id=pk)

	
	form = Balance_mainForm(instance=balance_main)

	return render (request, 'elektromer_app/balance_main.html', {'balance_main': balance_main, 
		'form': form,})


@login_required(login_url='login')
def balances_main(request):

	all_balances_main = Balance_main.objects.all()

	form = Balance_mainForm()
	
	return render (request, 'elektromer_app/balances_main.html', {'all_balances_main': all_balances_main, 
		'form': form, })


@login_required(login_url='login')
def balance_main_add(request):	
	submitted=False
	if request.method == 'POST':
		form = Balance_mainForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Stav Hlavního elektroměru byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("balances_main")

	else:
	
		form = Balance_mainForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/balances_main.html', {'form': form, 
		'submitted': submitted,})



@login_required(login_url='login')
def balance_main_update(request, pk):

	balance_main = Balance_main.objects.get(id=pk)
	form = Balance_mainForm(request.POST, instance=balance_main)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o stavu Hlavního elektroměru byly změněny.'))

		return redirect('balances_main')

	return render(request, "web_app/balances_main.html", {'form': form, 
		'balance_main': balance_main,})



@login_required(login_url='login')
def balance_main_delete(request, pk):
	
	balance_main = Balance_main.objects.get(id=pk)
	balance_main.delete()
	messages.success(request,("Stav Hlavního elektroměru byl úspěšně smazán."))
	return redirect("balances_main")

	
@login_required(login_url='login')
def balance_sub(request, pk):

	balance_sub = Balance_sub.objects.get(id=pk)

	
	form = Balance_subForm(instance=balance_sub)

	return render (request, 'elektromer_app/balance_sub.html', {'balance_sub': balance_sub, 
		'form': form,})


@login_required(login_url='login')
def balances_sub(request):

	all_balances_sub = Balance_sub.objects.all()

	
	
	form = Balance_subForm()
	
	return render (request, 'elektromer_app/balances_sub.html', {'all_balances_sub': all_balances_sub, 
		'form': form, })


@login_required(login_url='login')
def balance_sub_add(request):	
	submitted=False
	if request.method == 'POST':
		form = Balance_subForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Stav Podružného elektroměru byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("balances_sub")

	else:
	
		form = Balance_subForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/balances_sub.html', {'form': form, 
		'submitted': submitted,})


@login_required(login_url='login')
def balance_sub_update(request, pk):

	balance_sub = Balance_sub.objects.get(id=pk)
	form = Balance_subForm(request.POST, instance=balance_sub)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o stavu Podružném elektroměru byly změněny.'))

		return redirect('balances_sub')

	return render(request, "web_app/balances_sub.html", {'form': form, 
		'balance_sub': balance_sub,})


@login_required(login_url='login')
def balance_sub_delete(request, pk):
	
	balance_sub = Balance_sub.objects.get(id=pk)
	balance_sub.delete()
	messages.success(request,("Stav Podružného elektroměru byl úspěšně smazán."))
	return redirect("balances_sub")




@login_required(login_url='login')
def balance_solar(request, pk):

	balance_solar = Balance_solar.objects.get(id=pk)

	
	form = Balance_solarForm(instance=balance_solar)

	return render (request, 'elektromer_app/balance_solar.html', {'balance_solar': balance_solar, 
		'form': form,})


@login_required(login_url='login')
def balances_solar(request):
	

	all_balances_solar = Balance_solar.objects.all()

		
	form = Balance_solarForm()
	
	return render (request, 'elektromer_app/balances_solar.html', {'all_balances_solar': all_balances_solar, 
		'form': form, })


@login_required(login_url='login')
def balance_solar_add(request):	
	submitted=False
	if request.method == 'POST':
		form = Balance_solarForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Stav Solárního elektroměru byl úspěšně přidán."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("balances_solar")

	else:
	
		form = Balance_solarForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/balances_solar.html', {'form': form, 
		'submitted': submitted,})



@login_required(login_url='login')
def balance_solar_update(request, pk):

	balance_solar = Balance_solar.objects.get(id=pk)
	form = Balance_solarForm(request.POST, instance=balance_solar)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o stavu Solárního elektroměru byly změněny.'))

		return redirect('balances_solar')

	return render(request, "elektromer_app/balances_solar.html", {'form': form, 
		'balance_solar': balance_solar,})


@login_required(login_url='login')
def balance_solar_delete(request, pk):
	
	balance_solar = Balance_solar.objects.get(id=pk)
	balance_solar.delete()
	messages.success(request,("Stav Solárního elektroměru byl úspěšně smazán."))
	return redirect("balances_solar")


@login_required(login_url='login')
def count(request):

	return render(request, "elektromer_app/count.html", {})



@login_required(login_url='login')
def customer(request, pk):

	customer = Customer.objects.get(id=pk)

	customer_flats = customer.flat_set.all()


	flat_count = customer_flats.count()


	return render (request, 'elektromer_app/customer.html', {'customer' : customer, 
		'customer_flats': customer_flats,
		'flat_count': flat_count,})


@login_required(login_url='login')

def customers(request):

	all_customers = Customer.objects.all()


	form = CustomerForm()
	
	return render (request, 'elektromer_app/customers.html', {'all_customers': all_customers,
	 'form': form, })


@login_required(login_url='login')
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

	

@login_required(login_url='login')
def customer_update(request, pk):
	
	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form=CustomerForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('customers')

	return render(request, 'elektromer_app/customer.html', {'form': form,})


@login_required(login_url='login')
def customer_delete(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()
	messages.success(request,("Zákazník byl úspěšně smazán."))
	return redirect('customers')


@login_required(login_url='login')
def flat(request, pk):

	flat = Flat.objects.get(id=pk)
	form = FlatForm(instance=flat)

	return render (request, 'elektromer_app/flat.html', {'flat': flat, 
		'form': form,})

@login_required(login_url='login')
def flats(request):

	all_flats = Flat.objects.all().order_by('svj')
	form = FlatForm()

	return render (request, 'elektromer_app/flats.html', {'all_flats': all_flats, 
		'form': form,})

@login_required(login_url='login')
def flat_add(request):

	submitted=False
	
	if request.method == 'POST':
		form=FlatForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Bytová jednotka byla úspěšně přidána."))

		else:
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))

			return redirect('flats')

	else:
	
		form = FlatForm()
		if 'submitted' in request.GET:
			submitted = True


	return render(request, 'elektromer_app/flat.html', {'form': form, 
		'submitted': submitted,})


@login_required(login_url='login')
def flat_update(request):	

	flat = Flat.objects.get(id=pk)
	
	form = FlatForm(request.POST, instance=flat)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o Bytové jednotce byly změněny.'))

		return redirect("flat")

	

	return render(request, "web_app/flat.html", {'form': form, 
		'flat': flat, })


@login_required(login_url='login')
def flat_delete(request, pk):
	
	flat = Flat.objects.get(id=pk)
	flat.delete()
	messages.sucgcess(request,("Bytová jednotka byla úspěšně smazána."))
	return redirect('flats')




"""

def chairman(request):
	return render (request, 'elektromer_app/chairman.html', {})


def sub_chairman(request):
	return render (request, 'elektromer_app/sub_chairman.html', {})

"""



@login_required(login_url='login')
def gsm_modul(request, pk):

	gsm_modul = Gsm_modul.objects.get(id=pk)
	form = Gsm_modulForm(instance=gsm_modul)

	return render (request, 'elektromer_app/gsm_modul.html', {'gsm_modul':gsm_modul, 
		'form': form, })


@login_required(login_url='login')
def gsm_moduls(request):

	all_gsm_moduls = Gsm_modul.objects.all().order_by('svj')
	form = Gsm_modulForm()

	return render (request, 'elektromer_app/gsm_moduls.html', {'all_gsm_moduls': all_gsm_moduls, 
		'form': form})

@login_required(login_url='login')
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

	return render(request, 'elektromer_app/gsm_moduls.html', {'form': form, 
		'submitted': submitted,})

	
@login_required(login_url='login')
def gsm_modul_update(request, pk):


	gsm_modul = Gsm_modul.objects.get(id=pk)
	
	form = Gsm_modulForm(request.POST, instance=gsm_modul)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o GSM modulu byly změněny.'))

		return redirect('main_electrometers')

	

	return render(request, "web_app/gsm_moduls.html", {'form': form, 
		'gsm_modul': gsm_modul, })



@login_required(login_url='login')
def gsm_modul_delete(request, pk):

	gsm_modul = Gsm_modul.objects.get(id=pk)
	gsm_modul.delete()
	messages.success(request,("Gsm modul byl úspěšně smazán."))
	return redirect('gsm_moduls')


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get("username")
		password = request.POST.get('password')

		user = authenticate(request, username=username, password = password)

		if user is not None:
			login(request, user)
			return redirect("home")

		else:
			messages.info(request, "Uživatelské jméno nebo Heslo je nesprávné.")
			return render(request, "elektromer_app/login.html")

	return render(request, 'elektromer_app/login.html',{})


@login_required(login_url='login')
def logoutUser(request):

	logout(request)

	return redirect("login")


@login_required(login_url='login')
def main_electrometer(request, pk):

	main_electrometer = Main_electrometer.objects.get(id=pk)
	form = Main_electrometerForm(instance=main_electrometer)

	return render (request, 'elektromer_app/main_electrometer.html', {'main_electrometer': main_electrometer, 'form': form,})


@login_required(login_url='login')
def main_electrometers(request):

	all_main_electrometers = Main_electrometer.objects.all()
	form = Main_electrometerForm()

	return render (request, 'elektromer_app/main_electrometers.html', {'all_main_electrometers': all_main_electrometers, 'form': form, })


@login_required(login_url='login')
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


@login_required(login_url='login')
def main_electrometer_update(request, pk):

	
	
	main_electrometer = Main_electrometer.objects.get(id=pk)
	
	form = Main_electrometerForm(request.POST, instance=main_electrometer)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o Hlavním elektroměru byly změněny.'))

		return redirect('main_electrometers')

	

	return render(request, "web_app/main_electrometers.html", {'form': form, 'main_elektrometer': main_electrometer, })


@login_required(login_url='login')
def main_electrometer_delete(request, pk):
	
	main_electrometer = Main_electrometer.objects.get(id=pk)
	main_electrometer.delete()
	messages.success(request,("Hlavní elektroměr byl úspěšně smazán."))
	return redirect('main_electrometers')


@login_required(login_url='login')
def overview(request):

	return render(request, "elektromer_app/overview.html", {})



@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)

			Customer.objects.create(user=user)

			messages.success(request, "Váš účet byl úspěšně vytvořen pro " + user)
			return redirect('login')

	return render(request, 'elektromer_app/register.html',{'form': form,})


@login_required(login_url='login')
def solar_electrometer(request, pk):

	solar_electrometer = Solar_electrometer.objects.get(id=pk)
	form = Solar_electrometerForm(instance=solar_electrometer)

	return render (request, 'elektromer_app/solar_electrometer.html', {'solar_electrometer': solar_electrometer, 'form': form, })


@login_required(login_url='login')
def solar_electrometers(request):

	all_solar_electrometers = Solar_electrometer.objects.all()

	form = Solar_electrometerForm()

	return render (request, 'elektromer_app/solar_electrometers.html', {'all_solar_electrometers': all_solar_electrometers, 'form': form, })


@login_required(login_url='login')
def solar_electrometer_add(request):

	submitted=False
	
	if request.method == 'POST':
		form = Solar_electrometerForm(request.POST)

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

	return render(request, 'elektromer_app/solar_electrometers.html', {'form': form, 
		'submitted': submitted})



@login_required(login_url='login')
def solar_electrometer_update(request, pk):

	solar_electrometer = Solar_electrometer.objects.get(id=pk)
	
	form = Solar_electrometerForm(request.POST, instance=solar_electrometer)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o Solárním elektroměru byly změněny.'))

		return redirect('solar_electrometers')

	

	return render(request, "web_app/solar_electrometers.html", {'form': form, 
		'solar_elektrometer': solar_electrometer, })


@login_required(login_url='login')
def solar_electrometer_delete(request, pk):
	
	solar_electrometer = Solar_electrometer.objects.get(id=pk)
	solar_electrometer.delete()
	messages.success(request,("Solární elektroměr byl úspěšně smazán."))
	return redirect("solar_electrometers")

	

@login_required(login_url='login')
def sub_electrometer(request, pk):

	sub_electrometer = Sub_electrometer.objects.get(id=pk)
	form = Sub_electrometerForm(instance=sub_electrometer)

	return render (request, 'elektromer_app/sub_electrometer.html', {'sub_electrometer': sub_electrometer, 'form': form,})


@login_required(login_url='login')
def sub_electrometers(request):

	all_sub_electrometers = Sub_electrometer.objects.all().order_by('svj')

	form = Sub_electrometerForm()

	return render (request, 'elektromer_app/sub_electrometers.html', {'all_sub_electrometers': all_sub_electrometers, 'form': form})


@login_required(login_url='login')
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


@login_required(login_url='login')
def sub_electrometer_update(request, pk):

	sub_electrometer = Sub_electrometer.objects.get(id=pk)
	
	form = Sub_electrometerForm(request.POST, instance=sub_electrometer)

	if form.is_valid():
		form.save()
		messages.success(request, ('Informace o Podružném elektroměru byly změněny.'))

		return redirect('sub_electrometers')

	

	return render(request, "web_app/sub_electrometers.html", {'form': form, 'sub_elektrometer': sub_electrometer, })




@login_required(login_url='login')
def sub_electrometer_delete(request, pk):
	
	sub_electrometer = Sub_electrometer.objects.get(id=pk)
	sub_electrometer.delete()
	messages.success(request,("Podružný elektroměr byl úspěšně smazán."))
	return redirect('sub_electrometers')



@login_required(login_url='login')
def svj (request, pk):


	svj = Svj.objects.get(id=pk)
	form = SvjForm(instance=svj)

	return render (request, 'elektromer_app/svj.html', {'svj': svj, 'form': form,})



@login_required(login_url='login')
def svjs (request):

	form = SvjForm()

	all_svj = Svj.objects.all()

	return render (request, 'elektromer_app/svjs.html', {'all_svj': all_svj,
		'form': form,})



@login_required(login_url='login')
def svj_add (request):

	submitted=False
	
	if request.method == 'POST':
		form=SvjForm(request.POST)

		if form.is_valid():
			form.save()
			messages.success(request,("Společenství vlastníků bylo úspěšně přidáno."))

		else:
			
			messages.error(request, ("Zkontrolujte prosím údaje zda jsou správné"))
		
		return redirect("svjs")

	else:
	
		form = CustomerForm()
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'elektromer_app/svjs.html', {'form': form, 
		'submitted': submitted,})

	
@login_required(login_url='login')
def svj_delete (request, pk):

	svj = Svj.objects.get(id=pk)
	svj.delete()
	messages.success(request,("Svj bylo úspěšně smazáno."))
	return redirect('svjs')




@login_required(login_url='login')
def svj_update (request, pk):

	svj = Svj.objects.get(id=pk)

	form = SvjForm(instance=customer)

	if request.method == 'POST':
		form=SvjForm(request.POST, instance=customer)
		if form.is_valid():
			form.save()
			return redirect('svj')

	return render(request, 'elektromer_app/svj.html', {'form': form,})
	


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	
	#orders = request.user.inhabitant.order_set.all()
	return render(request, 'elektromer_app/user.html',{})