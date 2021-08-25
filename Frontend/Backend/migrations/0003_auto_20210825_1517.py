# Generated by Django 3.2.6 on 2021-08-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_rename_contact_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='country',
            field=models.CharField(choices=[('IN', 'India'), ('US', 'United States'), ('FR', 'France'), ('CN', 'China'), ('RU', 'Russia'), ('IT', 'Italy'), ('OTH', 'Other')], default='India', max_length=300),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], default='Male', max_length=130),
        ),
    ]
