# Generated by Django 5.0.7 on 2024-08-02 08:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('startup_idea', models.TextField()),
                ('target_number_of_users_goal', models.IntegerField()),
                ('target_date_goal', models.DateField()),
                ('generated_idea', models.TextField()),
                ('generated_slogan', models.TextField()),
                ('generated_problem', models.TextField()),
                ('generated_solution', models.TextField()),
                ('generated_user_persona', models.TextField()),
                ('generated_market_analysis', models.TextField()),
                ('generated_mvp_builder', models.TextField()),
                ('generated_user_feedback_analyzer', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]