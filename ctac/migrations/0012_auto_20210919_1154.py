# Generated by Django 3.2.7 on 2021-09-19 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctac', '0011_auto_20210908_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemember',
            name='present_in',
            field=models.CharField(choices=[('present', 'present'), ('not_available', 'not_available')], max_length=20),
        ),
        migrations.AlterField(
            model_name='chapelheads',
            name='chapel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctac.chapel'),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('60 and above', '60 and above'), ('40-49 years', '40-49 years'), ('20-29 years', '20-29 years'), ('30-39 years', '30-39 years'), ('10-19 years', '10-19 years'), ('50-59 years', '50-59 years')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('Divorced', 'Divorced'), ('widow', 'widow'), ('Married', 'Married'), ('Single', 'Single')], max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='owner_of_phone_number',
            field=models.CharField(choices=[('another person', 'another person'), ('self', 'self')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_usage',
            field=models.CharField(choices=[('I use a tablet for online service', 'I use a tablet for online service'), ("I don't have a smartphone but i have a yam", "I don't have a smartphone but i have a yam"), ("I don't have a phone", "I don't have a phone"), ('I use a smartphone for online service', 'I use a smartphone for online service')], max_length=50, verbose_name='Which of The Following Applies To You'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[('Member', 'Member'), ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ("Don't Understand", "Don't Understand"), ('Shepherd', 'Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='title',
            field=models.CharField(choices=[('Ps', 'Ps'), ('Rev', 'Rev'), ('Bishop', 'Bishop')], max_length=30),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
    ]
