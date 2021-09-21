from django import forms
from .models import *
import json


class CreatePastorForm(forms.ModelForm):
    class Meta:
        model = Pastor
        fields = (
            'title', 'first_name', 'second_name', 'surname',
            'sex', 'phone_number', 'email_address',
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
            'chapel_heads', 'chapel',
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
            'first_name', 'second_name', 'surname','email_address', 'phone_number','gps_address',
            'sex', 'type','ministry','chapel',
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
    # dshepherds = {}
    # list_shepherds = []
    # for shepherd in Shepherd.objects.all():
    #     if shepherd.chapel.chapel_name in dshepherds:
    #         dshepherds[shepherd.chapel.chapel_name].append(shepherd.surname)
    #     else:
    #         dshepherds[shepherd.chapel.chapel_name] = [shepherd.surname]
    #     list_shepherds.append((shepherd.surname, shepherd.surname))
    #
    # chapels = [str(chapel) for chapel in Chapel.objects.all()]

    # chapel_select = forms.ChoiceField(choices=([(chapel, chapel) for chapel in chapels]))
    # shepherd_select = forms.ChoiceField(choices=(list_shepherds))
    #
    # chapels = json.dumps(chapels)
    # shepherd = json.dumps(dshepherds)

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
                  'contact_number',
                  'owner_of_phone_number',
                  'details_of_owner',
                  'whatsapp_number',
                  'micro_area_name',
                  'nearest_landmark',
                  'phone_usage',
                  'online_service',
                  'services',
                  'ministries',
                  'chapel',
                  'shepherd',
                  'chapel_head',
                  'state',
                  'bacenta_leader',)


class CreateAttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceMember
        fields = ('present_in',
                  'date',
                  'member',
                  'chapel',
                  'shepherd',
                  'services',)



class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code',help_text='Enter SMS verification code')
    class Meta:
        model = Code
        fields = ('number',)