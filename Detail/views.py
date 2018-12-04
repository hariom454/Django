from django.shortcuts import render, get_object_or_404,redirect



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
	#form = MovieForm(request.POST or None)
	if request.method == "POST":
		form = MovieForm(request.POST)
		if form.is_valid():
			movie = form.save(commit=False)
			movie.save()
			return redirect('movie-detail', mv_id=movie.id)
	else:
		form = MovieForm()
	return render(request, 'Detail/form.html',{'form':form})

def home_view(request):
	obj = Movie.objects.all()
	return render(request, 'Detail/home.html', {'obj':obj})

def producerDetailView(request, my_id):
	
	obj = get_object_or_404(Producer, id=my_id)
	return render(request, "Detail/producer_detail.html",{'obj':obj})
def movie_detail(request,mv_id):
	obj = get_object_or_404(Movie, id=mv_id)
	return render(request, 'Detail/movie_detail.html',{'obj':obj})
