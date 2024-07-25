# Generated by Django 5.0.6 on 2024-07-22 21:00

import django.db.models.deletion
import materials.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_alter_material_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('lectures', 'Lectures'), ('classes', 'Classes'), ('labs', 'Labs'), ('projects', 'Projects')], max_length=20)),
                ('file', models.FileField(upload_to=materials.models.upload_path)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='materials.material')),
            ],
        ),
    ]