# Generated by Django 3.2.7 on 2021-09-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctac', '0007_auto_20210905_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shepherd',
            name='phone',
        ),
        migrations.AlterField(
            model_name='member',
            name='age',
            field=models.CharField(choices=[('20-29 years', '20-29 years'), ('40-49 years', '40-49 years'), ('30-39 years', '30-39 years'), ('60 and above', '60 and above'), ('50-59 years', '50-59 years'), ('10-19 years', '10-19 years')], max_length=15, verbose_name='Select your Age Group'),
        ),
        migrations.AlterField(
            model_name='member',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('widow', 'widow')], max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='online_service',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50, verbose_name='Are You Able To Join Our Online Services?'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone_usage',
            field=models.CharField(choices=[('I use a tablet for online service', 'I use a tablet for online service'), ('I use a smartphone for online service', 'I use a smartphone for online service'), ("I don't have a phone", "I don't have a phone"), ("I don't have a smartphone but i have a yam", "I don't have a smartphone but i have a yam")], max_length=50, verbose_name='Which of The Following Applies To You'),
        ),
        migrations.AlterField(
            model_name='member',
            name='state',
            field=models.CharField(choices=[('Member', 'Member'), ('Assisting Shepherd or Trainee Shepherd', 'Assisting Shepherd or Trainee Shepherd'), ("Don't Understand", "Don't Understand"), ('Ministry Shepherd', 'Ministry Shepherd'), ('Shepherd', 'Shepherd')], max_length=100, verbose_name='Please Tick Where Applicable'),
        ),
        migrations.AlterField(
            model_name='pastor',
            name='title',
            field=models.CharField(choices=[('Bishop', 'Bishop'), ('Rev', 'Rev'), ('Ps', 'Ps')], max_length=30),
        ),
        migrations.AlterField(
            model_name='shepherd',
            name='type',
            field=models.CharField(choices=[('Trainee Shepherd', 'Trainee Shepherd'), ('Bacenta Leader', 'Bacenta Leader'), ('Assistant Shepherd', 'Assistant Shepherd'), ('Ministry Shepherd', 'Ministry Shepherd')], max_length=30, verbose_name='Type of Shepherd'),
        ),
    ]