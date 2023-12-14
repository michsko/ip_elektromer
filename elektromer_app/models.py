from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User

# Create your models here.


	



class Svj(models.Model):


	
	from_date = models.DateField(null=False)
	

	name = models.CharField(max_length=255)
	address_street = models.CharField(max_length=255)
	address_orientation_number = models.IntegerField(default=0, null=True, blank=True)
	address_number_subscription = models.IntegerField(null=True, blank=True)
	address_city = models.CharField(max_length=255)
	address_postal_code = models.IntegerField(null=True, blank=True)


	date_of_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	low_form = models.CharField(max_length=255)

	ico = models.CharField(max_length=255, blank=True)
	tax_number = models.CharField(max_length=255, null=True, blank=True)


	account_number = models.CharField(max_length=255, null=True, blank=True)

	email = models.EmailField(max_length=255, blank=True, null=True)
	phone = models.CharField(max_length=255, blank=True, null=True)

	active = models.BooleanField(default=True)
	active_from = models.DateField(auto_now_add = True, null=True, blank=True)
	active_to = models.DateField(null=True, blank=True)


	history = HistoricalRecords()


	def __str__(self):
		return self.name 


class Customer(models.Model):

	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=255, null=False)
	surname = models.CharField(max_length=255, null=False)
	phone = models.CharField(max_length=255, null=False)
	email = models.EmailField(max_length=244, null=False)
	address_street = models.CharField(max_length=255)
	address_orientation_number = models.IntegerField(default=0, null=True, blank=True)
	address_number_subscription= models.IntegerField(default=0)
	address_city = models.CharField(max_length=255)
	address_postal_code = models.IntegerField(default=0)
	contract_number = models.CharField(max_length=255, null=True, blank=True)
	
	svj = models.ManyToManyField(Svj)
	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	history = HistoricalRecords()


	def __str__(self):
		return self.name + " " + self.surname


"""

class Chairman(models.Model):


	STATE = (
		("Aktivní","Aktivní"),
		("Pozastavené", "Pozastavené"),
		("Neaktivní", "Neaktivní"), 
		)


	customer= models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True) 
	email=models.EmailField(max_length = 254, null=False)
	from_date = models.DateField(null=False)
	to_date = models.DateField(blank=True, null=True)
	
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	history = HistoricalRecords()


	def __str__(self):
		return str(self.customer) + " -- " + str(self.svj)
"""

class Event(models.Model):
	name = models.CharField(max_length=255, null=True)
	day = models.DateField('Day of the event')
	start_time  = models.TimeField('Starting time', )
	end_time = models.TimeField('Ending time', )
	notes = models.TextField('Textual Notes', blank = True, null = True)

	history = HistoricalRecords()


	def __str__(self):
		return str(self.name) + " -- " + str(self.day)
"""
	class Meta:
		verbose_name = "Scheduling"
		verbose_name_plural = "Scheduling"
}
"""
"""
	def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
 
        return overlap
 
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')
 
        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
"""

"""
class Sub_chairman(models.Model):


	customer= models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True) 
	email=models.EmailField(max_length = 254, null=False)
	from_date = models.DateField(null=False)
	to_date = models.DateField(blank=True, null=True)
	
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	history = HistoricalRecords()


	def __str__(self):
		return str(self.customer) + " -- " + str(self.svj)
"""

class Gsm_modul(models.Model):


	
	identification_number = models.CharField(max_length=255, null=False)
	from_date = models.DateField(null=False)
	to_date = models.DateField(blank=True, null=True)
	
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	history = HistoricalRecords()

	
	def __str__(self):
		return self.identification_number + " --  " + str(self.svj)


class Flat(models.Model):


	flat_number = models.IntegerField(null=False, default = None)

	from_date = models.DateField(null=False)
	to_date = models.DateField(blank=True, null=True)

	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
	gsm_modul = models.ForeignKey(Gsm_modul, on_delete=models.SET_NULL, null=True)
	owner = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	owner_from_date = models.DateField(null=True, blank=True)
	owner_to_date = models.DateField(blank=True, null=True)
	
	date_created = models.DateTimeField(auto_now_add=True, null=True) 
	history = HistoricalRecords()


	def __str__(self):
		return str("byt č. ") + str( self.flat_number ) + "  --  " + str(self.svj) 	












"""

class Main_electrometer(models.Model):


	identification_number = models.CharField(max_length=255, null=False)
	from_date = models.DateField(null=True)
	to_date = models.DateField(blank=True, null=True)
	
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	history = HistoricalRecords()


	def __str__(self):
		return str(self.identification_number) + "  -- " + str(self.svj)	


class Sub_electrometer(models.Model):


	identification_number = models.CharField(max_length=255, null=False)
	from_date = models.DateField(null=False)
	to_date = models.DateField(blank=True, null=True)

	flat = models.ForeignKey(Flat, on_delete=models.SET_NULL, null=True)
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return str(self.flat) + " -- " + str(self.svj)	


class Solar_electrometer(models.Model):


	identification_number = models.CharField(max_length=255, null=False)
	from_date = models.DateField(null=False)
	to_date = models.DateField(blank=True, null=True)

	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
	gsm_modul = models.ForeignKey(Gsm_modul, on_delete=models.SET_NULL, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	history = HistoricalRecords()


	def __str__(self):
		return str(self.identification_number) + " -- " + str(self.svj)	


class Balance_main(models.Model):

	
	main_electrometer = models.ForeignKey(Main_electrometer, on_delete=models.SET_NULL, null=True)
	balance = models.DecimalField(max_digits=10, decimal_places=3)
	from_date = models.DateField(null=True, blank=True)
	to_date = models.DateField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)


	history = HistoricalRecords()


	
	def __str__(self):
		return str(self.main_electrometer) + " -- " + str('stav: ' + str(self.balance))

class Balance_sub(models.Model):

	
	sub_electrometer = models.ForeignKey(Sub_electrometer, on_delete=models.SET_NULL, null=True)
	balance = models.DecimalField(max_digits=8, decimal_places=2)
	from_date = models.DateField(null=True, blank=True)
	to_date = models.DateField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)

	history = HistoricalRecords()


	def __str__(self):
		return str(self.sub_electrometer) + " -- " + str('stav: ' + str(self.balance))
class Balance_solar(models.Model):

	
	solar_electrometer = models.ForeignKey(Solar_electrometer, on_delete=models.SET_NULL, null=True)
	balance = models.DecimalField(max_digits=8, decimal_places=2)
	from_date = models.DateField(null=True, blank=True)
	to_date = models.DateField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	svj = models.ForeignKey(Svj, on_delete=models.SET_NULL, null=True)
 

	history = HistoricalRecords()



	def __str__(self):
		return str(self.solar_electrometer) + " -- " + str('stav: ' + str(self.balance))


"""


