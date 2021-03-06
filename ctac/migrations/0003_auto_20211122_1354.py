# Generated by Django 2.1.7 on 2021-11-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctac', '0002_auto_20211122_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemember',
            name='present_in',
            field=models.CharField(choices=[('present', 'present'), ('not_available', 'not_available')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('50-59 years', '50-59 years'), ('60 and above', '60 and above'), ('40-49 years', '40-49 years'), ('20-29 years', '20-29 years'), ('10-19 years', '10-19 years'), ('30-39 years', '30-39 years')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Divorced', 'Divorced'), ('widow', 'widow'), ('Single', 'Single')], max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_usage',
            field=models.CharField(choices=[("I don't have a phone", "I don't have a phone"), ('I use a smartphone for online service', 'I use a smartphone for online service'), ("I don't have a smartphone but i have a yam", "I don't have a smartphone but i have a yam"), ('I use a tablet for online service', 'I use a tablet for online service')], max_length=50, verbose_name='Which of The Following Applies To You'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[('Shepherd', 'Shepherd'), ("Don't Understand", "Don't Understand"), ('Member', 'Member'), ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='title',
            field=models.CharField(choices=[('Bishop', 'Bishop'), ('Rev', 'Rev'), ('Ps', 'Ps')], max_length=30),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='type',
            field=models.CharField(choices=[('Assistant Shepherd', 'Assistant Shepherd'), ('Trainee Shepherd', 'Trainee Shepherd'), ('Bacenta Leader', 'Bacenta Leader'), ('Ministry Shepherd', 'Ministry Shepherd')], max_length=30, verbose_name='Type of Shepherd'),
        ),
    ]
