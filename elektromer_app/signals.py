from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Customer


#@receiver(post_save, sender=user)
def create_customer_profile(sender, instance, created, **kwargs):

	if created:
		group = Group.objects.get(name='customer')
		instance.groups.add(group)

		Customer.objects.create(user=instance, name=instance.username)

			
		print("Profile created!")

post_save.connect(create_customer_profile, sender=User)




#@receiver(post_save, sender=user)
"""def update_customer_profile():

	if created == False:
		print()

		try:
			instance.profile.save()
			print('Profile updated.')
		except:
			Profile.objects.create(user=instance)
			print("Profile created for existing user!")

post_save.connect(update_customer_profile, sender=User)
"""