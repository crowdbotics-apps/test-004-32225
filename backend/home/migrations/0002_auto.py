# Generated by Django 2.2.24 on 2021-12-02 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=256)),
                ('fourwheeldrive', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]