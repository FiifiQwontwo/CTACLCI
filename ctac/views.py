from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import *

from django.contrib import messages
from django.db.models import Q
from django.db.models import Count


#
# # Create your views here.

def index(request):
    return render(request, 'index.html')


def list_pastor(request):
    paslist = Pastor.objects.all()
    context = {
        'paslist': paslist

    }
    return render(request, 'pastor.html', context)


#
#

#
def list_shepherd(request):
    sheplist = Shepherd.objects.all()
    context = {
        'sheplist': sheplist
    }
    return render(request, 'shepherd.html', context)


#
#
def list_ministry(request):
    minlist = Ministry.objects.all()
    context = {'minlist': minlist}
    return render(request, 'ministry.html', context)


#

def list_chapel(request):
    chap = Chapel.objects.all()
    context = {'chap': chap}
    return render(request, 'chapel.html', context)


def list_service(request):
    services = Service.objects.all()
    context = {'new': services}
    return render(request, 'services.html', context)


# withcount
def list_area(request):
    area = AreaResidence.objects.all()
    new_area = area.count()
    context = {'area': area,
               'new_area': new_area}
    return render(request, 'area.html', context)


def list_chapel_heads(request):
    heads = ChapelHeads.objects.all()
    context = {'head': heads}
    return render(request, 'chapelheads.html', context)


def list_member(request):
    memblist = Member.objects.all()
    mem = memblist.count()
    context = {
        'memblist': memblist,
        'mem': mem
    }
    return render(request, 'member.html', context)


#
#
# # details
def pastor_details(request, slug):
    pas_details = get_object_or_404(Pastor, slug=slug)
    return render(request, 'tems/pastor.html', {'pas_details': pas_details})


#
def shepherd_details(request, slug):
    shepdetails = get_object_or_404(Shepherd, slug=slug)
    return render(request, 'tems/shepherd.html', {'shepdetails': shepdetails})


def ministry_details(request, slug):
    mindetails = get_object_or_404(Ministry, slug=slug)
    return render(request, 'tems/ministry.html', {'mindetails': mindetails})


#
#
def member_details(request, slug):
    membdetails = get_object_or_404(Member, slug=slug)
    context = {
        'membdetails': membdetails
    }
    return render(request, 'tems/member.html', context)


#
#
def chapel_details(request, slug):
    chapdetail = get_object_or_404(Chapel, slug=slug)
    context = {
        'chapdetail': chapdetail
    }
    return render(request, 'tems/chap.html', context)


# create
def create_pastor(request):
    pastor_create = CreatePastorForm(request.POST or None, request.FILES)
    if pastor_create.is_valid():
        pastor_create.save(commit=False)
        pastor_create.save()
        messages.success(request, "Pastor successfully Created")
        return redirect('ctac:urls_pastor_list')
    context = {
        'pastor_create': pastor_create
    }
    return render(request, 'create/pastor.html', context)


#
#
def create_shepherd(request):
    shepherd_create = CreateShepherdForm(request.POST or None, request.FILES)
    if shepherd_create.is_valid():
        shepherd_create.save(commit=False)
        shepherd_create.save()
        messages.success(request, "Shepherd successfully Created")
        return redirect('ctac:urls_list_shepherd')
    context = {
        'create_shepherd': create_shepherd
    }
    return render(request, 'create/shepherd.html', context)


#
#

def create_ministry(request):
    ministry_create = CreateMinistryForm(request.POST or None, request.FILES)
    if ministry_create.is_valid():
        ministry_create.save(commit=False)
        ministry_create.save()
        messages.success(request, 'Ministry Successfully Added')
        return redirect('ctac:urls_list_shepherd')
    context = {
        'ministry_create': ministry_create
    }
    return render(request, 'create/ministry.html', context)


#
#


def create_member(request):
    member_create = CreateMemberForm(request.POST or None, request.FILES)
    if member_create.is_valid():
        member_create.save(commit=False)
        member_create.save()
        messages.success(request, 'Ministry Successfully Added')
        return redirect('ctac:urls_list_member')
    context = {
        'member_create': member_create
    }
    return render(request, 'create/member.html', context)


def create_chapel(request):
    chapel_create = CreateChapelForm(request.POST or None, request.FILES)
    if chapel_create.is_valid():
        chapel_create.save(commit=False)
        chapel_create.save()
        message.success(request, 'Chapel Successfully Created')
        return redirect('ctac:urls_list_chapel')
    context = {
        'chapel_create': chapel_create
    }
    return render(request, 'create/chapel.html', context)


def create_services(request):
    services_create = CreateServiceForm(request.POST or None, request.FILES)
    if services_create.is_valid():
        services_create.save(commit=False)
        services_create.save()
        messages.success(request, 'New Service has be added')
        return redirect('ctac:urls_services_list')
    context = {
        'services_create': services_create
    }
    return render(request, 'create/services.html', context)


def create_area_residences(request):
    arearesidences = CreateServiceForm(request.POST or None, request.FILES)
    if arearesidences.is_valid():
        arearesidences.save(commit=False)
        arearesidences.save()
        messages.success(request, 'Added a new Residences')
        return redirect('ctac:urls_areas_list')
    context = {
        'arearesidences': arearesidences
    }
    return render(request, 'create/area.html', context)


def create_chapel_heads(request):
    heads_chapel = CreateChapelHeadsForm(request.POST or None, request.FILES)
    if heads_chapel.is_valid():
        heads_chapel.save(commit=False)
        heads_chapel.save()
        messages.success(request, 'Added a New Chapel Head')
        return redirect('ctac:urls_head_list')
    context = {
        'heads_chapel': heads_chapel
    }
    return render(request, 'create/chapel_heads.html', context)


#
# update
def member_update(request, slug):
    update_member = get_object_or_404(Member, slug=slug)
    updatemember = CreateMemberForm(request.POST or None, instance=update_member)
    if updatemember.is_valid():
        updatemember.save()
        return redirect('ctac:urls_details_member')
    context = {
        'updatemember': updatemember
    }
    return render(request, 'update/member.html', context)


#
def pastor_update(request, slug):
    update_pastor = get_object_or_404(Pastor, slug=slug)
    updatepastor = CreatePastorForm(request.POST or None, instance=update_pastor)
    if updatepastor.is_valid():
        updatepastor.save()
        return redirect('ctac:urls_details_pastor')
    context = {
        'updatepastor': updatepastor
    }
    return render(request, 'update/pastor.html', context)


#

def ministrty_update(request, slug):
    update_ministry = get_object_or_404(Ministry, slug=slug)
    updateministry = CreateMinistryForm(request.POST or None, instance=update_ministry)
    if updateministry.is_valid():
        updateministry.save()
        return redirect('ctac:urls_details_ministry')
    context = {
        'updateministry': updateministry
    }
    return render(request, 'update/ministry.html', context)


#
#

def shepherd_update(request, slug):
    update_shepherd = get_object_or_404(Shepherd, slug=slug)
    updateshepherd = CreateShepherdForm(request.POST or None, instance=update_shepherd)
    if updateshepherd.is_valid():
        updateshepherd.save()
        return redirect('ctac:urls_details_pastor')
    context = {
        'updateshepherd': updateshepherd
    }
    return render(request, 'update/shepherd.html', context)


#
#

def chapel_update(request, slug):
    update_chapel = get_object_or_404(Chapel, slug=slug)
    updatechapel = CreateChapelForm(request.POST or None, instance=update_chapel)
    if updatechapel.is_valid():
        updatechapel.save()
        return redirect('ctac:chapel_details_urls')
    context = {
        'updatechapel': updatechapel
    }
    return render(request, 'update/chapel.html', context)


def chapel_heads_update(request, slug):
    update_heads_chapel = get_object_or_404(Chapel, slug=slug)
    updateheadschapel = CreateChapelForm(request.POST or None, instance=update_heads_chapel)
    if updateheadschapel.is_valid():
        updateheadschapel.save()
        return redirect('ctac:chapel_details_urls')
    context = {
        'updateheadschapel': updateheadschapel
    }
    return render(request, 'update/chapelheads.html', context)


def area_update(request, slug):
    update_area = get_object_or_404(Chapel, slug=slug)
    areaupdate = CreateChapelForm(request.POST or None, instance=update_area)
    if areaupdate.is_valid():
        areaupdate.save()
        return redirect('ctac:urls_areas_list')
    context = {
        'areaupdate': areaupdate
    }
    return render(request, 'update/area.html', context)


# def services_update(request,slug):
#     updateservice = get_object_or_404(Service, slug=slug)
#     services = CreateServiceForm(request.POST or None, instance = updateservice)
#     if services.is_va


# # delete
# def pastor_delete(request, slug):
#     delete_pastor = get_object_or_404(Pastor, slug=slug)
#     if request.method == "POST":
#         delete_pastor.delete()
#         return redirect('ctaclci:urls_list_pastor')
#     context = {}
#     return render(request, 'delete/pastor.html', context)
#
#
# def ministry_delete(request, slug):
#     delete_ministry = get_object_or_404(Ministry, slug=slug)
#     if request.method == "POST":
#         delete_ministry.delete()
#         return redirect('ctaclci:urls_list_ministry')
#     context = {}
#     return render(request, 'delete/ministry.html', context)
#
#
# def member_delete(request, slug):
#     delete_member = get_object_or_404(Member, slug=slug)
#     if request.method == "POST":
#         delete_member.delete()
#         return redirect('ctaclci:urls_list_member')
#     return render(request, 'delete/member.html', context={})
#
#
# def shepherd_delete(request, slug):
#     delete_shepherd = get_object_or_404(Shepherd,slug=slug)
#     if request.method =="POST":
#         delete_shepherd.delete()
#         return redirect('ctaclci:urls_list_shepherd')
#     return render(request,'delete/shepherd.html',context={})
#
#

class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PastorViewSet(viewsets.ModelViewSet):
    queryset = Pastor.objects.all()
    serializer_class = PastorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ShepherdViewSet(viewsets.ModelViewSet):
    queryset = Shepherd.objects.all()
    serializer_class = ShepherdSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Shepherd.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
