# Generated by Django 5.1.1 on 2024-10-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_rename_description_task_content_remove_task_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcourse',
            name='course',
            field=models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development'), ('OS', 'Operating Systems'), ('DBMS', 'Database Management Systems'), ('AIML', 'ArtificialIntelligence and machine learning')], max_length=50),
        ),
        migrations.AlterField(
            model_name='marks',
            name='course',
            field=models.CharField(choices=[('AOOP', 'Advanced Object-Oriented Programming'), ('PFSD', 'Python Full Stack Development'), ('OS', 'Operating Systems'), ('DBMS', 'Database Management Systems'), ('AIML', 'ArtificialIntelligence and machine learning')], max_length=50),
        ),
    ]
