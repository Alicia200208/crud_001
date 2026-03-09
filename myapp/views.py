from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
# Create your views here.

def user_list(request):
    records = User.objects.all()
    return render(request, 'listingpage.html', {'records': records})

def AddUser(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')

    return render(request, 'add.html', {'form': form})

def EditUser(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('user_list')

    return render(request, 'edit.html', {'form': form})

def DeleteUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('user_list')
    return render(request, 'delete.html', {'user': one_rec})

def ViewUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    return render(request, 'view.html', {'user': one_rec})