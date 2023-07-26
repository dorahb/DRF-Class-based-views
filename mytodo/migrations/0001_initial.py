# Generated by Django 4.2.3 on 2023-07-26 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mytodolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('due_on', models.DateTimeField(null=True)),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytodo.mytodolist')),
            ],
        ),
    ]