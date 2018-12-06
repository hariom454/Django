from django.shortcuts import render, get_object_or_404,redirect



# Create your views here.
from .models import Movie, Actor, Producer
from .forms import MovieForm, ActorForm, ProducerForm
def actorFormView(request):
	if request.method == "POST":
		form = ActorForm(request.POST)
		if form.is_valid():
			actor = form.save(commit=False)
			actor.save()
			return redirect('actor-detail', my_id=actor.id)
	else:
		form = ActorForm()

			
	return render(request, 'Detail/actor_form.html',{'form':form})

def producerFormView(request):
	if request.method == "POST":
		form = ProducerForm(request.POST)
		if form.is_valid():
			producer = form.save(commit=False)
			producer.save()
			return redirect('producer-detail', my_id=producer.id)
	else:
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
def actor_detail(request, my_id):
	
	obj = get_object_or_404(Actor, id=my_id)
	return render(request, "Detail/actor_detail.html",{'obj':obj})

def producerDetailView(request, my_id):
	
	obj = get_object_or_404(Producer, id=my_id)
	return render(request, "Detail/producer_detail.html",{'obj':obj})
def movie_detail(request,mv_id):
	obj = get_object_or_404(Movie, id=mv_id)
	return render(request, 'Detail/movie_detail.html',{'obj':obj})

def movie_edit(request, my_id):
    movie = get_object_or_404(Movie, id=my_id)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('movie-detail', mv_id=post.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'Detail/form.html', {'form': form})

def producer_edit(request, my_id):
    producer = get_object_or_404(Producer, id=my_id)
    if request.method == "POST":
        form = ProducerForm(request.POST, instance=producer)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('producer-detail', my_id=post.id)
    else:
        form = ProducerForm(instance=producer)
    return render(request, 'Detail/producer_form.html', {'form': form})

def actor_edit(request, my_id):
    actor = get_object_or_404(Actor, id=my_id)
    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('actor-detail', my_id=post.id)
    else:
        form = ActorForm(instance=actor)
    return render(request, 'Detail/actor_form.html', {'form': form})