from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from rest_framework.generics import ListAPIView

from BackUpDispatch.forms import CFSCreateForm
from BackUpDispatch.models import CFS
from BackUpDispatch.serializers import CallSerializer


def home(request):
    return render(request, 'BackupDispatch/home.html')


def vuetest(request):
    return render(request, 'BackupDispatch/vuetest.html')

class CFSCreateView(CreateView):
    model = CFS
    form_class = CFSCreateForm
    template_name = 'BackupDispatch/create_cfs.html'


def active_calls(request):
    return render(request, 'BackupDispatch/listcalls.html')


def active_callsxhr(request):
    return render(request, 'BackupDispatch/listcallsxhr.html')


class API_list_calls(ListAPIView):
    serializer_class = CallSerializer
    queryset = CFS.objects.all()


class CFSDetailView(DetailView):
    model = CFS
    template_name = 'BackupDispatch/calldetails.html'

