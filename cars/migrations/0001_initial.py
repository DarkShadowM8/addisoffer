# Generated by Django 3.2.15 on 2022-10-08 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin_number', models.CharField(max_length=20, unique=True, verbose_name='VIN Number')),
                ('seller_name', models.CharField(max_length=50, verbose_name='Seller Name')),
                ('reserve_bid', models.IntegerField(blank=True, default=0, verbose_name='Reserve Bid')),
                ('high_bid', models.IntegerField(default=0, verbose_name='Highest Bid')),
                ('total_bids', models.IntegerField(default=0, verbose_name='Total Bids')),
                ('total_comments', models.IntegerField(default=0, verbose_name='Total Comments')),
                ('time_left', models.DateTimeField(verbose_name='Time Left')),
                ('bid_days', models.IntegerField(verbose_name='Bidding Days')),
                ('seller_type', models.CharField(max_length=10, verbose_name='Seller Type')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('make', models.CharField(max_length=30, verbose_name='Make')),
                ('model', models.CharField(max_length=30, verbose_name='Model')),
                ('body_type', models.CharField(max_length=20, verbose_name='Body Type')),
                ('engine', models.CharField(max_length=20, verbose_name='Engine')),
                ('interior_color', models.CharField(max_length=30, verbose_name='Interior Color')),
                ('exterior_color', models.CharField(max_length=30, verbose_name='Exterior Color')),
                ('transmission', models.CharField(max_length=10, verbose_name='Transmission')),
                ('condition', models.CharField(max_length=30, verbose_name='Condition')),
                ('mileage', models.IntegerField(verbose_name='Mileage')),
                ('gas_type', models.CharField(max_length=20, verbose_name='Gas Type')),
                ('plate_code', models.CharField(max_length=30, verbose_name='Plate Code')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('coupon_code', models.CharField(blank=True, max_length=20, verbose_name='Coupon Code')),
                ('highlight_modification', models.TextField(max_length=200, verbose_name='Highlight/Modification')),
                ('known_flaws', models.TextField(max_length=200, verbose_name='Known Flaws')),
                ('other_info', models.TextField(max_length=200, verbose_name='Other Information')),
                ('car_status', models.CharField(choices=[('pending', 'PENDING'), ('listed', 'LISTED'), ('ended', 'ENDED')], default='pending', max_length=7, verbose_name='Car Status')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PublishedComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor_name', models.CharField(default='None', max_length=50, verbose_name='Commentor Name')),
                ('comment', models.TextField(max_length=100, verbose_name='Comment')),
                ('commentor_type', models.CharField(default='None', max_length=100, verbose_name='Commentor Type')),
                ('published_time', models.DateTimeField(auto_now=True)),
                ('commented_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('commentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publishedcomment_requests_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Car Image')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.IntegerField(verbose_name='Amount')),
                ('bid_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]