# Generated by Django 3.1.7 on 2021-05-02 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctac', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancemember',
            name='slug',
        ),
        migrations.AddField(
            model_name='attendancemember',
            name='services',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='ctac.service'),
        ),
        migrations.AlterField(
            model_name='attendancemember',
            name='present_in',
            field=models.CharField(choices=[('present', 'present'), ('not_available', 'not_available')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('20-29 years', '20-29 years'), ('40-49 years', '40-49 years'), ('50-59 years', '50-59 years'), ('60 and above', '60 and above'), ('30-39 years', '30-39 years'), ('10-19 years', '10-19 years')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('widow', 'widow'), ('Single', 'Single'), ('Divorced', 'Divorced')], max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='owner_of_phone_number',
            field=models.CharField(choices=[('self', 'self'), ('another person', 'another person')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_usage',
            field=models.CharField(choices=[('I use a tablet for online service', 'I use a tablet for online service'), ('I use a smartphone for online service', 'I use a smartphone for online service'), ("I don't have a smartphone but i have a yam", "I don't have a smartphone but i have a yam"), ("I don't have a phone", "I don't have a phone")], max_length=50, verbose_name='Which of The Following Applies To You'),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd'), ("Don't Understand", "Don't Understand"), ('Member', 'Member'), ('Shepherd', 'Shepherd')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='title',
            field=models.CharField(choices=[('Bishop', 'Bishop'), ('Rev', 'Rev'), ('Ps', 'Ps')], max_length=30),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='type',
            field=models.CharField(choices=[('Trainee Shepherd', 'Trainee Shepherd'), ('Assistant Shepherd', 'Assistant Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd'), ('Bacenta Leader', 'Bacenta Leader')], max_length=30, verbose_name='Type of Shepherd'),
        ),
    ]
