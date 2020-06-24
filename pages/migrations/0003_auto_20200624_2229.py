# Generated by Django 3.0.7 on 2020-06-24 22:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_subtopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='subtopic',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Subtopic'),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('allow_comments', models.BooleanField(default=True)),
                ('timestamp', models.DateField(default=django.utils.timezone.now)),
                ('module', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Module')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Topic')),
            ],
        ),
    ]