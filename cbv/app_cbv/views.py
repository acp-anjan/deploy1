from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse
from app_cbv.models import Hospital, PatientQuery

# Create your views here.


# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Hello there! from Class Based Views")

class IndexView(TemplateView):
    template_name = 'app_cbv/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['my_var'] = 'Basic Injection'
    #     return context

class HospitalListView(ListView):#model_list context goes
    """
    To give different context name other than model_list we can use following command
    context_object_name = 'hospitalsss'
    """
    model = Hospital
    

class HospitalDetailView(DetailView):
    #detail view gives lowecase modelname as context variable for html i.e hospital
    model = Hospital
    template_name = "app_cbv/hospital_detail.html"

class HospitalCreateView(CreateView):
    fields = '__all__'
    model = Hospital
    # template_name = "app_cbv/hospital_form.html"

class HospitalUpdateView(UpdateView):
    fields = ('name_hospital', 'location_hospital',)
    model = Hospital
    template_name = "app_cbv/hospital_form.html"

class HospitalDeleteView(DeleteView):
    model = Hospital
    success_url = reverse_lazy('app_cbv:list')
    # template_name = ".html"


