# Generated by Django 2.0.3 on 2019-10-23 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0027_teacherfuturenotifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='FutureTeacherMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('connected_future_student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_future_student_id', to=settings.AUTH_USER_MODEL)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Teacher')),
                ('teacher_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]