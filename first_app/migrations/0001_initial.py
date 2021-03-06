# Generated by Django 2.2 on 2019-04-25 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=120)),
                ('Category', models.CharField(choices=[('sport', 'SPORT'), ('electronic', 'ELECTRONIC'), ('other', 'OTHER')], default='other', max_length=120)),
                ('Brand', models.CharField(max_length=120)),
                ('Title', models.CharField(max_length=120)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Price', models.PositiveIntegerField()),
                ('Negotiation', models.CharField(max_length=120)),
                ('Picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(blank=True, to='first_app.Product_Details')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='first_app.Product_Details')),
            ],
        ),
    ]
