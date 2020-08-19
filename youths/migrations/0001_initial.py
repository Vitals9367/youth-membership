# Generated by Django 2.2.14 on 2020-07-28 13:32

import uuid

import django.db.models.deletion
import enumfields.fields
from django.conf import settings
from django.db import migrations, models

import youths.enums
import youths.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="YouthProfile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("membership_number", models.CharField(blank=True, max_length=16)),
                ("birth_date", models.DateField()),
                ("school_name", models.CharField(blank=True, max_length=128)),
                ("school_class", models.CharField(blank=True, max_length=10)),
                (
                    "expiration",
                    models.DateField(default=youths.models.calculate_expiration),
                ),
                (
                    "language_at_home",
                    enumfields.fields.EnumField(
                        default="fi", enum=youths.enums.YouthLanguage, max_length=32
                    ),
                ),
                ("approver_first_name", models.CharField(blank=True, max_length=255)),
                ("approver_last_name", models.CharField(blank=True, max_length=255)),
                ("approver_phone", models.CharField(blank=True, max_length=50)),
                ("approver_email", models.EmailField(blank=True, max_length=254)),
                (
                    "approval_token",
                    models.CharField(
                        blank=True, default=uuid.uuid4, editable=False, max_length=36
                    ),
                ),
                (
                    "approval_notification_timestamp",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                (
                    "approved_time",
                    models.DateTimeField(blank=True, editable=False, null=True),
                ),
                ("photo_usage_approved", models.NullBooleanField()),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="AdditionalContactPerson",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                (
                    "youth_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_contact_persons",
                        to="youths.YouthProfile",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
