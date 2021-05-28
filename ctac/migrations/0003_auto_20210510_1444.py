# Generated by Django 3.1.7 on 2021-05-10 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctac', '0002_auto_20210502_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='arearesidence',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendancemember',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chapel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chapelheads',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ministry',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pastor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shepherd',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendancemember',
            name='present_in',
            field=models.CharField(choices=[('not_available', 'not_available'), ('present', 'present')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('30-39 years', '30-39 years'), ('60 and above', '60 and above'), ('40-49 years', '40-49 years'), ('20-29 years', '20-29 years'), ('50-59 years', '50-59 years'), ('10-19 years', '10-19 years')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('widow', 'widow'), ('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='owner_of_phone_number',
            field=models.CharField(choices=[('another person', 'another person'), ('self', 'self')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_usage',
            field=models.CharField(choices=[("I don't have a phone", "I don't have a phone"), ("I don't have a smartphone but i have a yam", "I don't have a smartphone but i have a yam"), ('I use a smartphone for online service', 'I use a smartphone for online service'), ('I use a tablet for online service', 'I use a tablet for online service')], max_length=50, verbose_name='Which of The Following Applies To You'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[("Don't Understand", "Don't Understand"), ('Shepherd', 'Shepherd'), ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd'), ('Member', 'Member')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='type',
            field=models.CharField(choices=[('Ministry Shepherd', 'Ministry Shepherd'), ('Trainee Shepherd', 'Trainee Shepherd'), ('Assistant Shepherd', 'Assistant Shepherd'), ('Bacenta Leader', 'Bacenta Leader')], max_length=30, verbose_name='Type of Shepherd'),
        ),
    ]
