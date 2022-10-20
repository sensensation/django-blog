from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import BbForm
from .models import Bb, Rubric
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os


#класс-контроллер

class BbCreateView(LoginRequiredMixin, CreateView):

    login_url = "login"
    redirect_field_name = "index"
    
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {"bbs": bbs, "rubrics": rubrics, "current_rubric": current_rubric}
    return render(request, "bboard/by_rubric.html", context)


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {"bbs":bbs, "rubrics": rubrics}
    return render(request, "bboard/index.html", context)

class Post():
    @login_required(login_url='login')
    @staticmethod
    def post_edit(request, pk):
        post = Bb.objects.get(id=pk)
        form = BbForm(instance=post)
        if request.method == 'POST':
            if len(request.FILES) != 0:
                if len(post.image) > 0:
                    os.remove(post.image.path)
                post.image = request.FILES['image']
            form = BbForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('index')
        context = {'form': form}
        return render(request, 'bboard/post_edit.html', context)

    @login_required(login_url='login')
    @staticmethod   
    def post_delete(request, pk):
        post = Bb.objects.get(id=pk)
        
        if request.method == 'POST':
            post.delete()
            return redirect('index')
        return redirect('index')




