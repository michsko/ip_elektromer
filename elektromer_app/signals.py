from django.db.models.signals import post_save


def create_profile(sender, instance, created, **kwargs):

	if created:
		Profile.objects.create(user=instance)
		print("Profile created!")

	post_save.connect(create_profile, sender=User)


def update_profile():

	if created == False:
		print()

		try;
			instance.profile.save()
			print('Profile updated.')
		except:
			Profile.objects.create(user=instance)
			print("Profile created for existing user!")

post_save.connect(update_profile, sender=User)