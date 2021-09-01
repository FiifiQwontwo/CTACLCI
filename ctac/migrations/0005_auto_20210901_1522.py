# Generated by Django 3.2.6 on 2021-09-01 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctac', '0004_auto_20210901_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemember',
            name='present_in',
            field=models.CharField(choices=[('not_available', 'not_available'), ('present', 'present')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('30-39 years', '30-39 years'), ('50-59 years', '50-59 years'), ('20-29 years', '20-29 years'), ('40-49 years', '40-49 years'), ('10-19 years', '10-19 years'), ('60 and above', '60 and above')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('widow', 'widow'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Married', 'Married')], max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_usage',
            field=models.CharField(choices=[("I don't have a phone", "I don't have a phone"), ('I use a smartphone for online service', 'I use a smartphone for online service'), ('I use a tablet for online service', 'I use a tablet for online service'), ("I don't have a smartphone but i have a yam", "I don't have a smartphone but i have a yam")], max_length=50, verbose_name='Which of The Following Applies To You'),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[('Ministry Shepherd', 'Ministry Shepherd'), ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ("Don't Understand", "Don't Understand"), ('Shepherd', 'Shepherd'), ('Member', 'Member')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='title',
            field=models.CharField(choices=[('Ps', 'Ps'), ('Bishop', 'Bishop'), ('Rev', 'Rev')], max_length=30),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='type',
            field=models.CharField(choices=[('Ministry Shepherd', 'Ministry Shepherd'), ('Trainee Shepherd', 'Trainee Shepherd'), ('Bacenta Leader', 'Bacenta Leader'), ('Assistant Shepherd', 'Assistant Shepherd')], max_length=30, verbose_name='Type of Shepherd'),
        ),
    ]