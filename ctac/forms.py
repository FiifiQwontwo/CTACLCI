from django import forms
from .models import *


class CreatePastorForm(forms.ModelForm):
    class Meta:
        model = Pastor
        fields = (
            'title', 'first_name', 'second_name', 'surname',
            'sex', 'phone_number',
        )


class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'service_name',
        )


class CreateChapelHeadsForm(forms.ModelForm):
    class Meta:
        model = ChapelHeads
        fields = (
            'chapel_heads',
        )


class CreateAreaResidenceForm(forms.ModelForm):
    class Meta:
        model = AreaResidence
        fields = (
            'area_residence',
        )


class CreateShepherdForm(forms.ModelForm):
    class Meta:
        model = Shepherd
        fields = (
            'first_name', 'second_name', 'surname',
            'sex', 'type',
        )


class CreateMinistryForm(forms.ModelForm):
    class Meta:
        model = Ministry
        fields = ('ministry_name',)


class CreateChapelForm(forms.ModelForm):
    class Meta:
        model = Chapel
        fields = ('chapel_name',)


class CreateMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('first_name',
                  'second_name',
                  'surname',
                  'sex',
                  'age',
                  'occupation',
                  'marital_status',
                  'area_of_residence',
                  'contact_number', 'owner_of_phone_number',
                  'details_of_owner', 'whatsapp_number',
                  'micro_area_name',
                  'nearest_landmark', 'phone_usage', 'online_service', 'services',
                  'ministries', 'chapel', 'shepherd', 'chapel_head', 'state', 'bacenta_leader',)


class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceMember
        fields = ('present_in',
                  'date',
                  'member',
                  'chapel',
                  'shepherd',
                  'services',)
