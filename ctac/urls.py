from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('area_api', AreaViewSet)
# router.register('users', UserViewSet)

app_name = 'ctac'

urlpatterns = [
    path('', index, name='home'),
    path('chapel/<slug:chapel__slug>', index, name='memberbychapel'),
    path('pastors/', list_pastor, name='urls_pastor_list'),
    path('shepherds/', list_shepherd, name='urls_shepherd_list'),
    path('ministries/', list_ministry, name='urls_ministry_list'),
    path('chapels/', list_chapel, name='urls_chapel_list'),
    path('services/', list_service, name='urls_services_list'),
    path('areas/', list_area, name='urls_areas_list'),
    path('chapel_heads/', list_chapel_heads, name='urls_head_list'),
    path('members/', list_member, name='urls_member_list'),
    path('list_attend/', list_attendance, name='urls_attendance_list'),
    # details
    path('pastors/<slug:slug>', pastor_details, name='pastor_details_url'),
    path('shepherds/<slug:slug>', shepherd_details, name='shepherd_details_url'),
    path('ministries/<slug:slug>', ministry_details, name='ministries_details_url'),
    path('members/<slug:slug>', member_details, name='member_details_url'),
    path('chapels/<slug:slug>', chapel_details, name='chapel_details_urls'),
    # path('attendance/<date:date>', atendance_details, name='attendane_details' ),
    # create
    path('add_pastor/', create_pastor, name='new_pastor_url'),
    path('add_shepherd/', create_shepherd, name='new_shepherd_url'),
    path('add_ministry/', create_ministry, name='new_ministry_url'),
    path('add_member/', create_member, name='add_member_url'),
    # path('add_chapel/', create_chapel, name='add_chapel_url'),
    path('add_area/', create_area_residences, name='add_area_url'),
    path('add_chapel_head/', create_chapel_heads, name='add_heads_chapel'),
    path('add_services/', create_services, name='new_services'),
    path('attendance_new/', attend_created, name='dance'),
    # path('chapel_add/', create_chapels, name='dont_dance_chapel'),
    path('chapelsadd/', new_chapel, name='new_url'),
    path('memberadds/', create_member, name='new member'),

    # update
    path('update_members/<slug:slug>', member_update, name='member_update_url'),
    path('update_pastors/<slug:slug>', pastor_update, name='pastor_update_url'),
    path('update_ministry/<slug:slug>', ministrty_update, name='ministries_update_url'),
    ##api views
    path('ministry_list_api/', MinistryViewSet.as_view({'get': 'list', }), name='ministry_list_api'),
    path('pastor_list_api/', PastorViewSet.as_view({'get': 'list', }), name='pastor_list_api'),
    path('add_osofo/', PastorViewSet.as_view({'post': 'create', }), name='new_osofo_api'),
    path('add_shepherd_api/', ShepherdViewSet.as_view({'post': 'create'}), name='new_shepherd_api'),
    path('shepherd_list_api/', ShepherdViewSet.as_view({'get': 'list'}), name='sheperd_list_api'),
    path('api_attendance/', Attendance.as_view({'get': 'list'}), name='attendance_list'),
    path('new_attendance/', Attendance.as_view({'post': 'create'}), name='new_attendance'),
    path('member_list_api/', MemberViewSet.as_view({'get': 'list', }), name='member_list_api'),
    path('add_member_api/', MemberViewSet.as_view({'post': 'create', }), name='new_member_api'),
    path('export_member/xls/', export_members_xls, name='export_members_xls'),
    path('export_shepherd/xls/', export_shepherd_xls, name='export_shepherd_xls'),
    path('export_pastor/xls/', export_pastor_xls, name='export_pastor_xls'),
    # path('export_chapelheads/xls/', export_chapel_heads_xls, name='export_chapelheads_xls'),
    path('uploads_dz0uio63/', simple_upload, name='upload'),
    path('exmem2300zia/', export_member, name='memex'),
    path('x_ip_calls/', ipcalls, name='ipslocation'),
    path('export_area/xls/', export_area_xls, name='export_area_xls'),
    path('conta/', red, name='contact'),
    path('', include(router.urls)),

]
