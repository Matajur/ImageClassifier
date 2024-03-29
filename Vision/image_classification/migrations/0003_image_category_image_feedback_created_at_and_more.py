# Generated by Django 5.0.2 on 2024-02-12 10:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image_classification", "0002_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="category",
            field=models.CharField(default=45, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="feedback_created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="Feedback",
        ),
    ]
