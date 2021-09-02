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
from django.contrib.auth.decorators import login_required
import xlwt
from django.http import HttpResponse, Http404
import requests
import json
from .resources import *
from tablib import Dataset
import requests
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import ensure_csrf_cookie


#
# # Create your views here.

# @login_required(login_url='users:login')
# def list_pastor(request):
#     paslist = Pastor.objects.all().order_by('created_at')
#     paspage = Paginator(paslist, 50)
#
#     page_num = request.GET.get('page', 1)
#     try:
#         page = paspage.page(page_num)
#     except EmptyPage:
#         page = paspage(1)
#     context = {
#         'paslist': page,
#
#     }
#     return render(request, 'pastor.html', context)
#

#
#

#
@login_required(login_url='users:login')
def list_shepherd(request):
    sheplist = Shepherd.objects.all()
    shpage = Paginator(sheplist, 50)

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
@login_required(login_url='users:login')
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
@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
def list_service(request):
    service = Service.objects.all()
    context = {'service': service}
    return render(request, 'services.html', context)


# withcount
@login_required(login_url='users:login')
def list_area(request):
    area = AreaResidence.objects.all()
    new_area = area.count()
    areapage = Paginator(area, 100)

    page_num = request.GET.get('page', 1)
    try:
        page = areapage.page(page_num)
    except EmptyPage:
        page = areapage(1)
    context = {'area': page,
               'new_area': new_area}
    return render(request, 'area.html', context)


@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
def list_member(request):
    memblist = Member.objects.all()
    memcount = memblist.count()
    membs = Paginator(memblist, 100)

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


@login_required(login_url='users:login')
def list_attendance(request):
    attd = AttendanceMember.objects.all()
    atmem = Paginator(attd, 100)

    page_num = request.GET.get('page', 1)
    try:
        page = atmem.page(page_num)
    except EmptyPage:
        page = atmem(1)
    context = {'attd': page}
    return render(request, 'attendance.html', context)


# @login_required(login_url='users:login')
def index(request, chapel__slug=None):
    memcount = Member.objects.all().count()
    shecounts = Shepherd.objects.all().count()
    new_area = AreaResidence.objects.all().count()
    mini_count = Ministry.objects.all().count()
    attd = AttendanceMember.objects.all().order_by('-id')[:5]
    mat = Member.objects.order_by('-created_at', 'shepherd')[:5]

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    else:
        request.session.set_test_cookie()
        messages.error(request, 'Please enable cookies')

    context = {
        'memcount': memcount,
        'shecounts': shecounts,
        'new_area': new_area,
        'mini_count': mini_count,
        'attd': attd,
        'mat': mat,


    }

    chapel_page = None
    member = None
    if chapel__slug != None:
        chapel_page = get_object_or_404(Chapel, slug=chapel__slug)
        member = Member.objects.filter(chapel=chapel_page, availabe=True)

    return render(request, 'index.html', context)


#
#
# # details
# @login_required(login_url='users:login')
# def pastor_details(request, slug):
#     pas_details = get_object_or_404(Pastor, slug=slug)
#     context = {'pas_details': pas_details}
#     return render(request, 'tems/pastor.html', context)


#
@login_required(login_url='users:login')
def shepherd_details(request, slug):
    shepdetails = get_object_or_404(Shepherd, slug=slug)
    return render(request, 'tems/shepherd.html', {'shepdetails': shepdetails})


@login_required(login_url='users:login')
def ministry_details(request, slug):
    mindetails = get_object_or_404(Ministry, slug=slug)
    return render(request, 'tems/ministry.html', {'mindetails': mindetails})


@login_required(login_url='users:login')
def member_details(request, slug):
    membdetails = get_object_or_404(Member, slug=slug)
    context = {'membdetails': membdetails}
    return render(request, 'tems/member.html', context)


#
@login_required(login_url='users:login')
def chapel_details(request, slug):
    chapdetail = get_object_or_404(Chapel, slug=slug)
    context = {
        'chapdetail': chapdetail
    }
    return render(request, 'tems/chap.html', context)


# create
@login_required(login_url='users:login')
@ensure_csrf_cookie
def create_pastor(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    pastor_create = CreatePastorForm(request.POST or None, request.FILES)
    if pastor_create.is_valid():
        instance = pastor_create.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Pastor successfully Created")
        return redirect('ctac:urls_pastor_list')
    context = {
        'pastor_create': pastor_create
    }
    return render(request, 'create/pastor.html', context)


#
# +
@ensure_csrf_cookie
@login_required(login_url='users:login')
def create_shepherd(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    shepherd_create = CreateShepherdForm(request.POST or None, request.FILES)
    if shepherd_create.is_valid():
        instance = shepherd_create.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Shepherd successfully Created")
        return redirect('ctac:urls_shepherd_list')
    context = {
        'shepherd_create': shepherd_create
    }
    return render(request, 'create/shepherd.html', context)


#
#
@ensure_csrf_cookie
@login_required(login_url='users:login')
def create_ministry(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    ministry_create = CreateMinistryForm(request.POST or None, request.FILES)
    if ministry_create.is_valid():
        instance = ministry_create.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Ministry Successfully Added')
        return redirect('ctac:urls_list_shepherd')
    context = {
        'ministry_create': ministry_create
    }
    return render(request, 'create/member.html', context)


#


# @ensure_csrf_cookie
# @login_required(login_url='users:login')
# def create_member(request):
#     if not request.user.is_staff or not request.user.is_superuser:
#         raise Http404
#     member_create = CreateMemberForm(request.POST or None, request.FILES)
#     if member_create.is_valid():
#         instance = member_create.save(commit=False)
#         instance.user = request.user
#         instance.save()
#         messages.success(request, 'Ministry Successfully Added')
#         return redirect('ctac:urls_list_member')
#     context = {
#         'member_create': member_create
#     }
#     return render(request, 'create/member.html', context)


@ensure_csrf_cookie
@login_required(login_url='users:login')
def create_member(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    member_create = CreateMemberForm(request.POST or None, request.FILES)
    if member_create.is_valid():
        print('hi')
        instance = member_create.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Shepherd successfully Created")
        return redirect('ctac:urls_list_member')
    context = {
        'member_create': member_create
    }
    return render(request, 'create/member.html', context)


@ensure_csrf_cookie
@login_required(login_url='users:login')
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


@ensure_csrf_cookie
@login_required(login_url='users:login')
def create_services(request):
    if request.user.is_superuser or not request.user.is_staff:
        raise Http404
    services_create = CreateServiceForm(request.POST or None, request.FILES)
    if services_create.is_valid():
        instance = services_create.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'New Service has be added')
        return redirect('ctac:urls_services_list')
    context = {
        'services_create': services_create
    }
    return render(request, 'create/services.html', context)


@ensure_csrf_cookie
@login_required(login_url='users:login')
def create_area_residences(request):
    if not request.user.is_superuser or not request.user.is_staff:
        raise Http404
    arearesidences = CreateAreaResidenceForm(request.POST or None, request.FILES)
    if arearesidences.is_valid():
        instance = arearesidences.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Added a new Residences')
        return redirect('ctac:urls_areas_list')
    context = {
        'arearesidences': arearesidences
    }
    return render(request, 'create/area.html', context)


@ensure_csrf_cookie
@login_required(login_url='users:login')
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


@ensure_csrf_cookie
@login_required(login_url='users:login')
def create_attendance(request):
    if not request.user.is_superuser or request.user.is_staff:
        raise Http404
    attend = CreateAttendanceForm(request.POST or None, request.FILES)
    if attend.is_valid():
        instance = attend.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Added a New attendee')
        return redirect('ctac:home')
    context = {
        'attend': attend
    }
    return render(request, 'create/attend.html', context)


#
# update
@login_required(login_url='users:login')
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



@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
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
@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
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
@login_required(login_url='users:login')
def pastor_delete(request, slug):
    delete_pastor = get_object_or_404(Pastor, slug=slug)
    if request.method == "POST":
        delete_pastor.delete()
        return redirect('ctaclci:urls_list_pastor')
    context = {}
    return render(request, 'delete/pastor.html', context)


@login_required(login_url='users:login')
def ministry_delete(request, slug):
    delete_ministry = get_object_or_404(Ministry, slug=slug)
    if request.method == "POST":
        delete_ministry.delete()
        return redirect('ctaclci:urls_list_ministry')
    context = {}
    return render(request, 'delete/ministry.html', context)


@login_required(login_url='users:login')
def member_delete(request, slug):
    delete_member = get_object_or_404(Member, slug=slug)
    if request.method == "POST":
        delete_member.delete()
        return redirect('ctaclci:urls_list_member')
    return render(request, 'delete/member.html', context={})


@login_required(login_url='users:login')
def shepherd_delete(request, slug):
    delete_shepherd = get_object_or_404(Shepherd, slug=slug)
    if request.method == "POST":
        delete_shepherd.delete()
        return redirect('ctaclci:urls_list_shepherd')
    return render(request, 'delete/shepherd.html', context={})


class MinistryViewSet(viewsets.ModelViewSet):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PastorViewSet(viewsets.ModelViewSet):
    queryset = Pastor.objects.all()
    serializer_class = PastorSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ShepherdViewSet(viewsets.ModelViewSet):
    queryset = Shepherd.objects.all()
    serializer_class = ShepherdSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Attendance(viewsets.ModelViewSet):
    queryset = AttendanceMember.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@login_required(login_url='users:login')
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

    rows = Member.objects.raw(
        ' select  ctac_member.first_name,'
        'ctac_member.second_name, ctac_member.surname,'
        'ctac_member.sex,ctac_member.occupation,ctac_arearesidence.area_residence,'
        'ctac_member.nearest_landmark, ctac_chapel.chapel_name, ctac_chapelheads.chapel_heads,'
        'ctac_shepherd.surname from((((ctac_member',
        'join ctac_arearesidence on((ctac_arearesidence.id = ctac_member.area_of_residence_id)))'
        'join ctac_chapel on((ctac_chapel.id=ctac_member.chapel_id)))'
        'join ctac_chapelheads on((ctac_chapelheads.id =ctac_member.chapel_head_id)))'
        'join ctac_shepherd on((ctac_shepherd.id =ctac_member.shepherd_id)))')
    for row in rows:
        row_num += 1
    for col_num in range(len(row)):
        ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
def ipcalls(request):
    response = requests.get('https://ipstack.com/json/')
    geodata = response.json()
    return render(request, 'ips.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name']
    }
                  )


@login_required(login_url='users:login')
def export_member(request):
    member_resource = MemberResource()
    dataset = member_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="member.xls"'
    return response


@login_required(login_url='users:login')
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


@login_required(login_url='users:login')
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


def error_404(request):
    data = {}
    return render(request, 'pages/examples/404.html', data)


def error_500(request):
    data = {}
    return render(request, 'pages/examples/404.html', data)


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = AreaResidence.objects.all()
    authentication_classes = (TokenAuthentication,)

# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
