from django.db import models
import string
import random
from django.utils.text import slugify
from django.conf import settings
from django.core.exceptions import ValidationError
from datetime import date
from django.urls import reverse


# from django.core.validators import RegexValidator


# Create your models here.
##############
# author fiifi Qwontwo Ahwireng###

# PHONE_NUMBER_REGEX = RegexValidator(r'^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$', 'only valid phone is required')
# email = RegexValidator(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'only valid email is required')


def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('attendance date cannot be in the future.')


Gender = {
    ('Male', 'Male'),
    ('Female', 'Female'),
}

MARITAL = {
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
    ('widow', 'widow'),

}


# random slug imported to handle slug

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Chapel(models.Model):
    chapel_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(rand_slug() + "-" + self.chapel_name)
    #     super(Chapel, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('ctac:memberbychapel', args=[self.slug])

    def __str__(self):
        return self.chapel_name


Age_Group = {
    ('10-19 years', '10-19 years'),
    ('20-29 years', '20-29 years'),
    ('30-39 years', '30-39 years'),
    ('40-49 years', '40-49 years'),
    ('50-59 years', '50-59 years'),
    ('60 and above', '60 and above'),
}

Mobile_Usage = {
    ('I use a smartphone for online service', 'I use a smartphone for online service'),
    ('I use a tablet for online service', 'I use a tablet for online service'),
    ('I don\'t have a smartphone but i have a yam', 'I don\'t have a smartphone but i have a yam'),
    ('I don\'t have a phone', 'I don\'t have a phone'),
}

Online_Services = {
    ('Yes', 'Yes'),
    ('No', 'No'),
}

Types_of_Shepherd = {
    ('Ministry Shepherd', 'Ministry Shepherd'),
    ('Trainee Shepherd', 'Trainee Shepherd'),
    ('Assistant Shepherd', 'Assistant Shepherd'),
    ('Bacenta Leader', 'Bacenta Leader'),

}

Members_s = {
    ('Member', 'Member'),
    ('Ministry Shepherd', 'Ministry Shepherd'),
    ('Shepherd', 'Shepherd'),
    ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'),
    ('Don\'t Understand', 'Don\'t Understand'),
}

Owner = {
    ('self', 'self'),
    ('another person', 'another person'),
}

Title = {
    ('Bishop', 'Bishop'),
    ('Rev', 'Rev'),
    ('Ps', 'Ps'),

}

Attendance = {
    ('present', 'present'),
    ('not_available', 'not_available'),
}


class Ministry(models.Model):
    ministry_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    chapel = models.ForeignKey(Chapel, default=1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.ministry_name)
        super(Ministry, self).save(*args, **kwargs)

    def __str__(self):
        return self.ministry_name


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.service_name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.service_name


class ChapelHeads(models.Model):
    chapel_heads = models.CharField(max_length=100)
    chapel = models.ForeignKey(Chapel, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.chapel_heads)
        super(ChapelHeads, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.chapel) + "-" + self.chapel_heads


class Pastor(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=70)
    sex = models.CharField(choices=Gender, max_length=20)
    title = models.CharField(choices=Title, max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)
    email_address = models.EmailField(blank=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     account_sid = ['AC9d1a78bae11c1fbd7f948bf4f1db8447']
    #     auth_token = ['27f297040157b111e64385cb2de5fa80']
    #     client = Client(account_sid, auth_token)
    #
    #     message = client.messages.create(
    #         messaging_service_sid='MG5dc4b05a843ea4b93c9b8b85e08535e7',
    #         body='a pastor was created',
    #         to='+233547232768'
    #     )
    #
    #     print(message.sid)
    #     return super(Pastor, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.surname)
        super(Pastor, self).save(*args, **kwargs)

    def __str__(self):
        return self.surname + ' - ' + self.first_name


class Shepherd(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=70)
    # phone = models.CharField(max_length=12, blank=True)
    sex = models.CharField(choices=Gender, max_length=20)
    phone_number = models.CharField(max_length=15, blank=True)
    email_address = models.EmailField(blank=True)
    gps_address = models.CharField(max_length=15, blank=True)
    ministry = models.ForeignKey(Ministry, default=1, on_delete=models.CASCADE)
    chapel = models.ForeignKey(Chapel, default=1, on_delete=models.CASCADE)
    type = models.CharField('Type of Shepherd', choices=Types_of_Shepherd, max_length=30)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def chapelname(self):
        return self.chapel.chapel_name

    def __str__(self):
        return self.surname + ' - ' + self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.surname)
        super(Shepherd, self).save(*args, **kwargs)


class AreaResidence(models.Model):
    area_residence = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.area_residence)
        super(AreaResidence, self).save(*args, **kwargs)

    def __str__(self):
        return self.area_residence


class Member(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=70)
    contact_number = models.CharField(max_length=14)
    owner_of_phone_number = models.CharField(max_length=20, choices=Owner)
    details_of_owner = models.CharField('If Phone Is For Another Person Then Provide Details', max_length=200,
                                        blank=True)
    whatsapp_number = models.CharField(max_length=12, blank=True)
    sex = models.CharField(choices=Gender, max_length=20)
    age = models.CharField('Select your Age Group', choices=Age_Group, max_length=15)
    occupation = models.CharField('Your Profession', max_length=30)
    marital_status = models.CharField(choices=MARITAL, max_length=50)
    area_of_residence = models.ForeignKey(AreaResidence, on_delete=models.CASCADE)
    micro_area_name = models.CharField(max_length=100)
    nearest_landmark = models.CharField(max_length=100)
    phone_usage = models.CharField('Which of The Following Applies To You', choices=Mobile_Usage, max_length=50)
    online_service = models.CharField('Are You Able To Join Our Online Services?', choices=Online_Services,
                                      max_length=50)
    ministries = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    chapel = models.ForeignKey(Chapel, on_delete=models.CASCADE)
    shepherd = models.ForeignKey(Shepherd, on_delete=models.CASCADE)
    chapel_head = models.ForeignKey(ChapelHeads, on_delete=models.CASCADE)
    state = models.CharField('Please Tick Where Applicable', choices=Members_s, max_length=100)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    bacenta_leader = models.CharField('Name of Your Bacenta Leader. (Answer Only If Applicable', max_length=50,
                                      blank=True)
    slug = models.SlugField(unique=True, help_text='Enter any text', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def shepherd_name(self):
        return self.shepherd.surname

    def chapeled(self):
        return self.shepherd.chapeled.chapel_name

    def __str__(self):
        return self.surname + ' - ' + self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.surname)
        super(Member, self).save(*args, **kwargs)


class AttendanceMember(models.Model):
    present_in = models.CharField(choices=Attendance, max_length=20)
    date = models.DateField(help_text="Enter the date of purchase", validators=[no_future])
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    chapel = models.ForeignKey(Chapel, on_delete=models.CASCADE)
    shepherd = models.ForeignKey(Shepherd, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    services = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.present_in + ' ' + str(self.member) + ' - ' + str(self.shepherd) + ' ' + str(self.date)
