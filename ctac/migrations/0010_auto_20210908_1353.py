# Generated by Django 3.2.7 on 2021-09-08 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctac', '0009_auto_20210907_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='ministry',
            name='chapel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ctac.chapel'),
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('20-29 years', '20-29 years'), ('60 and above', '60 and above'), ('50-59 years', '50-59 years'), ('10-19 years', '10-19 years'), ('40-49 years', '40-49 years'), ('30-39 years', '30-39 years')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='online_service',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=50, verbose_name='Are You Able To Join Our Online Services?'),
        ),
        migrations.AlterField(
            model_name='member',
            name='owner_of_phone_number',
            field=models.CharField(choices=[('self', 'self'), ('another person', 'another person')], max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[('Shepherd', 'Shepherd'), ("Don't Understand", "Don't Understand"), ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd'), ('Member', 'Member')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='type',
            field=models.CharField(choices=[('Ministry Shepherd', 'Ministry Shepherd'), ('Bacenta Leader', 'Bacenta Leader'), ('Trainee Shepherd', 'Trainee Shepherd'), ('Assistant Shepherd', 'Assistant Shepherd')], max_length=30, verbose_name='Type of Shepherd'),
        ),
    ]
