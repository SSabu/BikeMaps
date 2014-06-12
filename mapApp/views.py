from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.contrib.gis.geos import GEOSGeometry, Point, fromstr

from mapApp.models import Incident, Route
from mapApp.forms import IncidentForm, RouteForm

def index(request):
	context = {
		'incidents': Incident.objects.all(),
		"incidentForm": IncidentForm(), 	#the form to be rendered
		"incidentFormErrors": False,
		"routeForm": RouteForm(),
		"routeFormErrors": False
	}
	return render(request, 'mapApp/index.html', context)

def postRoute(request):
	if request.method == 'POST':
		routeForm = RouteForm(request.POST)

		# Convert string coords to valid geometry object
		routeForm.data = routeForm.data.copy()
		routeForm.data['line'] = GEOSGeometry(routeForm.data['line'])

		if routeForm.is_valid():
			routeForm.save()	
			return HttpResponseRedirect(reverse('mapApp:index')) 
		else:
			# Form is not valid, display modal with highlighted errors 
			return render(request, 'mapApp/index.html', {
				'incidents': Incident.objects.all(),
				"incidentForm": IncidentForm(),
				"incidentFormErrors": False,
				"routeForm": routeForm,
				"routeFormErrors": True
			})
	
	else:
		return HttpResponseRedirect(reverse('mapApp:index')) 

def postIncident(request):
	if request.method == 'POST':
		incidentForm = IncidentForm(request.POST)
		
		# Convert string coords to valid geometry object
		incidentForm.data = incidentForm.data.copy()
		incidentForm.data['point'] = GEOSGeometry(incidentForm.data['point'])

		if incidentForm.is_valid():
			incidentForm.save()	
			return HttpResponseRedirect(reverse('mapApp:index')) 
		
		else:
			# Form is not valid, display modal with highlighted errors 
			return render(request, 'mapApp/index.html', {
				'incidents': Incident.objects.all(),
				"incidentForm": incidentForm,
				"incidentFormErrors": True,
				"routeForm": RouteForm(),
				"routeFormErrors": False
			})
	
	else:
		return HttpResponseRedirect(reverse('mapApp:index')) 



def about(request):
	context = {
		'incidents': Incident.objects.all(),
	}

	return render(request, 'mapApp/about.html', context)

def sponsors(request):
	return render(request, 'mapApp/sponsors.html')

def contact(request):
	return render(request, 'mapApp/contact.html')

