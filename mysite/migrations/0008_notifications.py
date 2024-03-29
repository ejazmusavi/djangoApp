# Generated by Django 2.0.3 on 2019-10-17 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0007_future_student_post_teacher_connections_teacher_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logged_type', models.CharField(max_length=200)),
                ('sending_type', models.CharField(max_length=200)),
                ('pending', models.BooleanField(default=1)),
                ('logged_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sending_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
