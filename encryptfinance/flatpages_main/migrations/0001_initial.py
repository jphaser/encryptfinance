# Generated by Django 3.2.3 on 2021-05-18 21:30

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('question', models.CharField(blank=True, max_length=500, null=True, unique=True, verbose_name='FAQ Question')),
                ('answer', models.TextField(blank=True, null=True, unique=True, verbose_name='FAQ Answer')),
                ('active', models.BooleanField(default=False, verbose_name='Wallet is Active?')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
                'ordering': ['created'],
            },
        ),
    ]
