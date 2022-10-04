from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest
from .forms import NotesForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


from .models import Notes

class User:
    @staticmethod
    def register(request):
        if request.user.is_authenticated == True:
            return redirect('home')
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegisterForm()
            
        context = {"form": form}
        return render(request, 'base/register.html', context)

    @staticmethod
    def user_login(request):
        if request.user.is_authenticated == True:
            return redirect('home')
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
        else:
            form = UserLoginForm()
        return render(request, 'base/login.html', {"form": form})

    @staticmethod
    def user_logout(request):
        if request.user.is_authenticated == False:
            return redirect('home')
        logout(request)
        return redirect('home')

class Note:
    @staticmethod
    @login_required(login_url='login')
    def allnotes(request):
        notes = Notes.objects.filter(owner_id = request.user)  # Get notes from db
        context = {
            'notes': notes,
            'title': 'Notes' 
        }
        return render(request, 'base/home.html', context)

    @staticmethod
    @login_required(login_url='login')
    def create(request):
        if request.method == 'POST':
            form = NotesForm(request.POST)
            print(form.__dict__)
            if form.is_valid():
                note = form.save(commit=False)
                note.owner = request.user
                note.save()
                return redirect('home')
        form = NotesForm()  # Create instance of class (to display fields)
        context = {'form': form, 'title': 'Create'}
        return render(request, 'base/create_note.html', context)

    @staticmethod
    def update(request, pk):
        note = Notes.objects.get(id=pk)
        form = NotesForm(instance=note)

        if request.method == 'POST':
            form = NotesForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = { 'form': form }
        return render(request, 'base/update_note.html', context)

    @staticmethod
    def completed(request, pk):
        if request.method == 'POST':
            note = Notes.objects.get(id=pk)
            note.completed = not note.completed
            note.save()
            return redirect('home')
        return redirect('home')


    @staticmethod
    def delete(request, pk):
        note = Notes.objects.get(id=pk)

        if request.method == 'POST':
            note.delete()
            return redirect('/')
        
        return redirect('/')