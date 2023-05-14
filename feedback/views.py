from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView


class FeedBackView(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


# Create your views here.

# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})

class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov'
        context['date'] = '23.04.2022'
        return context


# def done(request):
#     return render(request, 'feedback/done.html')


class UpdateFeedBack(View):
    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})


# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})

class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback

class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['write'] = Feedback.objects.get(id=kwargs['id_feedback'])
#         return context
