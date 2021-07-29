from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import *
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django.db.models import Q
from django.db.models import Count
import xlwt
from django.http import HttpResponse
import requests
import json
from .resources import *
from tablib import Dataset
import requests


#
# # Create your views here.


def list_pastor(request):
    paslist = Pastor.objects.all().order_by('created_at')
    paspage = Paginator(paslist, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = paspage.page(page_num)
    except EmptyPage:
        page = paspage(1)
    context = {
        'paslist': page,

    }
    return render(request, 'pastor.html', context)


#
#

#
def list_shepherd(request):
    sheplist = Shepherd.objects.all()
    shpage = Paginator(sheplist, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = shpage.page(page_num)
    except EmptyPage:
        page = shpage(1)
    context = {
        'sheplist': sheplist
    }
    return render(request, 'shepherd.html', context)


#
#
def list_ministry(request):
    minlist = Ministry.objects.all().order_by('created_at')
    mispage = Paginator(minlist, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = mispage.page(page_num)
    except EmptyPage:
        page = mispage(1)
    context = {'minlist': page}
    return render(request, 'ministry.html', context)


#

def list_chapel(request):
    chap = Chapel.objects.all()
    chapage = Paginator(chap, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = chapage.page(page_num)
    except EmptyPage:
        page = chapage(1)
    context = {'chap': page}
    return render(request, 'chapel.html', context)


def list_service(request):
    service = Service.objects.all()
    context = {'service': service}
    return render(request, 'services.html', context)


def list_attendance(request):
    att = AttendanceMember.objects.all()
    context = {'att': att}
    return render(request, 'attendance.html', context)


# withcount
def list_area(request):
    area = AreaResidence.objects.all()
    new_area = area.count()
    areapage = Paginator(area, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = areapage.page(page_num)
    except EmptyPage:
        page = areapage(1)
    context = {'area': page,
               'new_area': new_area}
    return render(request, 'area.html', context)


def list_chapel_heads(request):
    heads = ChapelHeads.objects.all()
    cheadpage = Paginator(heads, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = cheadpage.page(page_num)
    except EmptyPage:
        page = cheadpage(1)
    context = {'head': page}
    return render(request, 'chapelheads.html', context)


def list_member(request):
    memblist = Member.objects.all()
    memcount = memblist.count()
    membs = Paginator(memblist, 10)

    page_num = request.GET.get('page', 1)
    try:
        page = membs.page(page_num)
    except EmptyPage:
        page = membs(1)
    context = {
        'memblist': page,
        'memcount': memcount
    }
    return render(request, 'member.html', context)


def index(request):
    memcount = Member.objects.all().count()
    shecounts = Shepherd.objects.all().count()
    new_area = AreaResidence.objects.all().count()
    mini_count = Ministry.objects.all().count()
    context = {
        'memcount': memcount,
        'shecounts': shecounts,
        'new_area': new_area,
        'mini_count': mini_count

    }
    return render(request, 'index.html', context)


#
#
# # details
def pastor_details(request, slug):
    pas_details = get_object_or_404(Pastor, slug=slug)
    context = {'pas_details': pas_details}
    return render(request, 'tems/pastor.html', context)


#
def shepherd_details(request, slug):
    shepdetails = get_object_or_404(Shepherd, slug=slug)
    return render(request, 'tems/shepherd.html', {'shepdetails': shepdetails})


def ministry_details(request, slug):
    mindetails = get_object_or_404(Ministry, slug=slug)
    return render(request, 'tems/ministry.html', {'mindetails': mindetails})


#


def member_details(request, slug):
    membdetails = get_object_or_404(Member, slug=slug)
    context = {'membdetails': membdetails}
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
    return render(request, 'create/member.html', context)


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
        messages.success(request, 'Chapel Successfully Created')
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


def create_attendance(request):
    attend = CreateAttendanceForm(request.POST or None, request.FILES)
    if attend.is_valid():
        attend.save(commit=False)
        attend.save()
        messages.success(request, 'Added a New attendee')
        return redirect('ctac:home')
    context = {
        'attend': attend
    }
    return render(request, 'create/attendance.html', context)


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
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Attendance(viewsets.ModelViewSet):
    queryset = AttendanceMember.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


def export_members_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Members.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Members')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First Name', 'Second name', 'Last Name', 'Gender', 'Occupation', 'Area_of_Residence',
               'nearest_landmark', 'contact_number', 'chapel', 'chapel_head', 'shepherd']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Member.objects.all().values_list('first_name',
                                            'second_name',
                                            'surname',
                                            'sex',
                                            'occupation',
                                            'area_of_residence', 'nearest_landmark', 'chapel', 'chapel_head',
                                            'shepherd')
    row = []
    for row in rows:
        row_num += 1
    for col_num in range(len(row)):
        ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_shepherd_xls(request):
    responses = HttpResponse(content_type='application/ms-excel')
    responses['Content-Disposition'] = 'attachment; filename="Shepherds.xls"'

    wba = xlwt.Workbook(encoding='utf-8')
    wsa = wba.add_sheet('Shepherds')

    # Sheet header, first row
    row_nums = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First Name', 'Second name', 'Last Name', 'Gender', 'type']

    for col_num in range(len(columns)):
        wsa.write(row_nums, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Shepherd.objects.all().values_list('first_name', 'second_name', 'surname', 'sex', 'type')
    row = []
    for row in rows:
        row_nums += 1
    for col_num in range(len(row)):
        wsa.write(row_nums, col_num, row[col_num], font_style)

    wba.save(responses)
    return responses


def export_pastor_xls(request):
    responsed = HttpResponse(content_type='application/ms-excel')
    responsed['Content-Disposition'] = 'attachment; filename="Pastor.xls"'

    wad = xlwt.Workbook(encoding='utf-8')
    wa = wad.add_sheet('Pastor')

    # Sheet header, first row
    row_nums = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Title', 'First Name', 'Second name', 'Last Name', 'Gender', 'Phone']

    for col_num in range(len(columns)):
        wa.write(row_nums, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Pastor.objects.all().values_list('title',
                                            'first_name',
                                            'second_name',
                                            'surname',
                                            'sex',
                                            'phone_number')
    row = []
    for row in rows:
        row_nums += 1
    for col_num in range(len(row)):
        wa.write(row_nums, col_num, row[col_num], font_style)

    wad.save(responsed)
    return responsed


def ipcalls(request):
    response = requests.get('https://ipstack.com/json/')
    geodata = response.json()
    return render(request, 'ips.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    }
                  )


def export_member(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="member.xls"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        mem_resource = MemberResource()
        datasets = Dataset()
        new_persons = request.FILES['new_persons']

        imported_data = datasets.load(new_members.read())
        result = mem_resource.import_data(datasets, dry_run=True)  # Test the data import

        if not result.has_errors():
            mem_resource.import_data(datasets, dry_run=False)  # Actually import now

    return render(request, 'import.html')


def export_area_xls(request):
    responsed = HttpResponse(content_type='application/ms-excel')
    responsed['Content-Disposition'] = 'attachment; filename="Residence.xls"'

    wad = xlwt.Workbook(encoding='utf-8')
    wa = wad.add_sheet('AreaResidence')

    # Sheet header, first row
    row_nums = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['area residence']

    for col_num in range(len(columns)):
        wa.write(row_nums, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = AreaResidence.objects.all().values_list('area_residence'

                                                   )
    row = []
    for row in rows:
        row_nums += 1
    for col_num in range(len(row)):
        wa.write(row_nums, col_num, row[col_num], font_style)

    wad.save(responsed)
    return responsed


#
# def send_sms(request, contactnumber, sms):
#     endPoint = 'https://api.mnotify.com/api/sms/quick'
#     apiKey = 'KeQAdN74Bquug7OBX0pDzAdGEFGqi8i3n8DAWLFxc92th'
#     sms = 'Your profile has been created on LCI CTAC Sakumono'
#
#     a = Member.objects.get(contactnumber=contact_number(request))
#
#
#
# data = {
#     'recipient[]': ['0249706365', '0203698970'],
#     'sender': 'mNotify',
#     'message': 'API messaging is fun!',
#     'is_schedule': False,
#     'schedule_date': ''
# }
# url = endPoint + '?key=' + apiKey
# response = requests.post(url, data)
# data = response.json()


def red(request):
    return render(request, 'as.html')
