from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Movie, Actor, Producer
from .forms import MovieForm, ActorForm, ProducerForm
def actorFormView(request):
	form = ActorForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ActorForm()
	return render(request, 'Detail/actor_form.html',{'form':form})
def producerFormView(request):
	form = ProducerForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ProducerForm()
	return render(request, 'Detail/producer_form.html',{'form':form})

def movieFormView(request):
	form = MovieForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = MovieForm()
	return render(request, 'Detail/form.html',{'form':form})

def home_view(request):
	obj = Movie.objects.all()
	return render(request, 'Detail/home.html', {})