# Generated by Django 5.2 on 2025-04-12 21:01

import django.db.models.deletion
import djrichtextfield.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("title", models.CharField(max_length=200)),
                ("excerpt", models.CharField(max_length=500)),
                ("content", djrichtextfield.models.RichTextField(max_length=10000)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "focus",
                    models.CharField(
                        choices=[
                            ("general_fitness", "General Fitness"),
                            ("strength", "Strength"),
                            ("hypertrophy", "Hypertrophy"),
                            ("weight_loss", "Weight Loss"),
                        ],
                        default="general-fitness",
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Draft"), (1, "Published")], default=0
                    ),
                ),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on", "author", "focus"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(default="")),
                ("approved", models.BooleanField(default=False)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commenter",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.post",
                    ),
                ),
            ],
            options={
                "ordering": ["created_on", "author"],
            },
        ),
    ]
