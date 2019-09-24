# Generated by Django 2.0.3 on 2019-09-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_no', models.TextField()),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatLine',
            fields=[
                ('msg_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=36)),
                ('line_text', models.TextField()),
                ('src_id', models.CharField(max_length=36)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('dest_id', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pic', models.FileField(upload_to='')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('med_id', models.CharField(blank=True, max_length=36, primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=50)),
                ('qty', models.IntegerField(default=0)),
                ('is_available', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=36)),
                ('admin_id', models.CharField(max_length=36)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('delivered_time', models.DateTimeField(auto_now_add=True)),
                ('est_delivery_time', models.DateTimeField(auto_now_add=True)),
                ('is_upload', models.BooleanField(default=False)),
                ('photo_url', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('rejected', 'REJECTED'), ('approved', 'APPROVED'), ('delivered', 'DELIVERED')], default='pending', max_length=10)),
                ('total_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('email_id', models.CharField(max_length=36)),
                ('name', models.CharField(max_length=36)),
                ('phone_no', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
