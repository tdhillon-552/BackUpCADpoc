from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.generics import ListAPIView

from BackUpDispatch.forms import CFSCreateForm
from BackUpDispatch.models import CFS
from BackUpDispatch.serializers import CallSerializer


def home(request):
    return render(request, 'BackupDispatch/home.html')


class CFSCreateView(CreateView):
    model = CFS
    form_class = CFSCreateForm
    template_name = 'BackupDispatch/create_cfs.html'


def active_calls(request):
    return render(request, 'BackupDispatch/listcalls.html')


class API_list_calls(ListAPIView):
    serializer_class = CallSerializer
    queryset = CFS.objects.all()
