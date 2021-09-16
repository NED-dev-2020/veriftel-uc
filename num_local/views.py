from django.shortcuts import render
from django.http import HttpResponseRedirect
import phonenumbers
from phonenumbers import geocoder, carrier
from django.contrib import messages

charge = 0

#la vue de ma page
def home(request):
	
	#variables
	pays = None
	service = None
	charge = 0
	
	
	if request.method == "POST":
		num = request.POST['num']
		
		try:
			#voir le pays
			num_ver = phonenumbers.parse(num, 'CH')
			pays = geocoder.description_for_number(num_ver, 'fr')
		
			#le reseau
			num_service = phonenumbers.parse(num, 'RO')
			service = carrier.name_for_number(num_service, 'fr')
			charge = 1
			messages.success(request, "Ce numero est du reseau {} ({})".format(service, pays))
			return HttpResponseRedirect('/')
			
		except:
			charge = 1
			messages.error(request, "Il semble que ce numero n est pas valide, veuillez verifier et ressayer")
			return HttpResponseRedirect('/')
	
	#page html
	template = 'home.html'
	
	#dict
	context = {
		'pays':pays,
		'service':service,
		'charge':charge,
	}
	return render(request, template, context)