# Generated by Django 3.2.8 on 2021-10-07 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20211007_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='location_taken',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.location'),
        ),
    ]