from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Park
from .forms import ParkForm
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

def get_place(request):
    if request.method == "POST":
        form = ParkForm(request.POST)
        
        if form.is_valid():
            
            post = form.save(commit=False)
            #var = post.place == 'A' or post.place == 'B'
            post.save()
            return redirect('post_edit', pk=post.pk)
    else:
        form = ParkForm()
    return render(request, 'Fragatapp/index.html', {'form': form})

    #def place(self):
        #place = self.place
        #if self.place !='A' or self.place != 'B':

            #raise ValidationError('только а или в')
        #return self.place

#def fill_form(request, pk):
    #post = get_object_or_404(Park, pk=pk)
    #form = ParkForm(instance=post)
    #return render(request, 'Fragatapp/fill_form.html', {'form': form})

def fill_form(request, pk):
    post = get_object_or_404(Park, pk=pk)
    return render(request,'Fragatapp/fill_form.html', {'post': post})
#def get_place(request, fregat):
    #fregat = get_object_or_404(Park)
    #form = ParkForm
    #if request.method == "POST":
        #form = ParkForm(request.POST)
        #instance_time = form.save()
        #Park.time.add(instance_time)
        #Park.save()
    #elif request.method == "Get":
        #form = ParkForm()

    #return render(request, "Fragatapp/index12.html", {"fregat": fregat, "Park_time": Park.time == request.user,
                                                    #"form": form})

# Create your views here.
