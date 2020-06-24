# Generated by Django 3.0.7 on 2020-06-24 11:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, max_length=150, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('allow_comments', models.BooleanField(default=True)),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Topic')),
            ],
        ),
    ]