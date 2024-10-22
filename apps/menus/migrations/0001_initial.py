# Generated by Django 4.0.3 on 2022-03-25 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='companies.brand')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menus.category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('currency', models.CharField(choices=[('XYZ', 'XYZ'), ('ADP', 'ADP'), ('AFA', 'AFA'), ('ALK', 'ALK'), ('AON', 'AON'), ('AOR', 'AOR'), ('ARA', 'ARA'), ('ARP', 'ARP'), ('ATS', 'ATS'), ('AZM', 'AZM'), ('BAD', 'BAD'), ('BEF', 'BEF'), ('BGL', 'BGL'), ('BRC', 'BRC'), ('BRE', 'BRE'), ('BRN', 'BRN'), ('BRR', 'BRR'), ('BYR', 'BYR'), ('CLE', 'CLE'), ('CSD', 'CSD'), ('CSK', 'CSK'), ('CYP', 'CYP'), ('DDM', 'DDM'), ('DEM', 'DEM'), ('ECS', 'ECS'), ('ECV', 'ECV'), ('EEK', 'EEK'), ('ESA', 'ESA'), ('ESB', 'ESB'), ('ESP', 'ESP'), ('FIM', 'FIM'), ('FRF', 'FRF'), ('GHC', 'GHC'), ('GRD', 'GRD'), ('GWP', 'GWP'), ('HRD', 'HRD'), ('IEP', 'IEP'), ('ITL', 'ITL'), ('LTL', 'LTL'), ('LUF', 'LUF'), ('LVL', 'LVL'), ('MGF', 'MGF'), ('MLF', 'MLF'), ('MRO', 'MRO'), ('MTL', 'MTL'), ('MZM', 'MZM'), ('NLG', 'NLG'), ('PEI', 'PEI'), ('PLZ', 'PLZ'), ('PTE', 'PTE'), ('ROL', 'ROL'), ('RUR', 'RUR'), ('SDD', 'SDD'), ('SIT', 'SIT'), ('SKK', 'SKK'), ('SRG', 'SRG'), ('STD', 'STD'), ('TJR', 'TJR'), ('TMM', 'TMM'), ('TPE', 'TPE'), ('TRL', 'TRL'), ('UAK', 'UAK'), ('USS', 'USS'), ('VEB', 'VEB'), ('VEF', 'VEF'), ('VNN', 'VNN'), ('XEU', 'XEU'), ('YDD', 'YDD'), ('YUM', 'YUM'), ('YUN', 'YUN'), ('ZAL', 'ZAL'), ('ZMK', 'ZMK'), ('ZRN', 'ZRN'), ('ZRZ', 'ZRZ'), ('ZWD', 'ZWD'), ('ZWL', 'ZWL'), ('ZWR', 'ZWR'), ('AOK', 'AOK'), ('ARL', 'ARL'), ('ARM', 'ARM'), ('BAN', 'BAN'), ('BEC', 'BEC'), ('BEL', 'BEL'), ('BGM', 'BGM'), ('BGO', 'BGO'), ('BOL', 'BOL'), ('BOP', 'BOP'), ('BRB', 'BRB'), ('BRZ', 'BRZ'), ('BUK', 'BUK'), ('BYB', 'BYB'), ('CNH', 'CNH'), ('CNX', 'CNX'), ('GEK', 'GEK'), ('GNS', 'GNS'), ('GQE', 'GQE'), ('GWE', 'GWE'), ('ILP', 'ILP'), ('ILR', 'ILR'), ('ISJ', 'ISJ'), ('KRH', 'KRH'), ('KRO', 'KRO'), ('LTT', 'LTT'), ('LUC', 'LUC'), ('LUL', 'LUL'), ('LVR', 'LVR'), ('MAF', 'MAF'), ('MCF', 'MCF'), ('MDC', 'MDC'), ('MKN', 'MKN'), ('MRU', 'MRU'), ('MTP', 'MTP'), ('MVP', 'MVP'), ('MXP', 'MXP'), ('MZE', 'MZE'), ('NIC', 'NIC'), ('PES', 'PES'), ('RHD', 'RHD'), ('SDP', 'SDP'), ('STN', 'STN'), ('SUR', 'SUR'), ('UGS', 'UGS'), ('UYP', 'UYP'), ('UYW', 'UYW'), ('VES', 'VES'), ('XRE', 'XRE'), ('YUD', 'YUD'), ('YUR', 'YUR'), ('AED', 'AED'), ('AFN', 'AFN'), ('ALL', 'ALL'), ('AMD', 'AMD'), ('ANG', 'ANG'), ('AOA', 'AOA'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('AWG', 'AWG'), ('AZN', 'AZN'), ('BAM', 'BAM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('BGN', 'BGN'), ('BHD', 'BHD'), ('BIF', 'BIF'), ('BMD', 'BMD'), ('BND', 'BND'), ('BOB', 'BOB'), ('BOV', 'BOV'), ('BRL', 'BRL'), ('BSD', 'BSD'), ('BTN', 'BTN'), ('BWP', 'BWP'), ('BYN', 'BYN'), ('BZD', 'BZD'), ('CAD', 'CAD'), ('CDF', 'CDF'), ('CHE', 'CHE'), ('CHF', 'CHF'), ('CHW', 'CHW'), ('CLF', 'CLF'), ('CLP', 'CLP'), ('CNY', 'CNY'), ('COP', 'COP'), ('COU', 'COU'), ('CRC', 'CRC'), ('CUC', 'CUC'), ('CUP', 'CUP'), ('CVE', 'CVE'), ('CZK', 'CZK'), ('DJF', 'DJF'), ('DKK', 'DKK'), ('DOP', 'DOP'), ('DZD', 'DZD'), ('EGP', 'EGP'), ('ERN', 'ERN'), ('ETB', 'ETB'), ('EUR', 'EUR'), ('FJD', 'FJD'), ('FKP', 'FKP'), ('GBP', 'GBP'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('GIP', 'GIP'), ('GMD', 'GMD'), ('GNF', 'GNF'), ('GTQ', 'GTQ'), ('GYD', 'GYD'), ('HKD', 'HKD'), ('HNL', 'HNL'), ('HRK', 'HRK'), ('HTG', 'HTG'), ('HUF', 'HUF'), ('IDR', 'IDR'), ('ILS', 'ILS'), ('IMP', 'IMP'), ('INR', 'INR'), ('IQD', 'IQD'), ('IRR', 'IRR'), ('ISK', 'ISK'), ('JMD', 'JMD'), ('JOD', 'JOD'), ('JPY', 'JPY'), ('KES', 'KES'), ('KGS', 'KGS'), ('KHR', 'KHR'), ('KMF', 'KMF'), ('KPW', 'KPW'), ('KRW', 'KRW'), ('KWD', 'KWD'), ('KYD', 'KYD'), ('KZT', 'KZT'), ('LAK', 'LAK'), ('LBP', 'LBP'), ('LKR', 'LKR'), ('LRD', 'LRD'), ('LSL', 'LSL'), ('LYD', 'LYD'), ('MAD', 'MAD'), ('MDL', 'MDL'), ('MGA', 'MGA'), ('MKD', 'MKD'), ('MMK', 'MMK'), ('MNT', 'MNT'), ('MOP', 'MOP'), ('MUR', 'MUR'), ('MVR', 'MVR'), ('MWK', 'MWK'), ('MXN', 'MXN'), ('MXV', 'MXV'), ('MYR', 'MYR'), ('MZN', 'MZN'), ('NAD', 'NAD'), ('NGN', 'NGN'), ('NIO', 'NIO'), ('NOK', 'NOK'), ('NPR', 'NPR'), ('NZD', 'NZD'), ('OMR', 'OMR'), ('PAB', 'PAB'), ('PEN', 'PEN'), ('PGK', 'PGK'), ('PHP', 'PHP'), ('PKR', 'PKR'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('QAR', 'QAR'), ('RON', 'RON'), ('RSD', 'RSD'), ('RUB', 'RUB'), ('RWF', 'RWF'), ('SAR', 'SAR'), ('SBD', 'SBD'), ('SCR', 'SCR'), ('SDG', 'SDG'), ('SEK', 'SEK'), ('SGD', 'SGD'), ('SHP', 'SHP'), ('SLL', 'SLL'), ('SOS', 'SOS'), ('SRD', 'SRD'), ('SSP', 'SSP'), ('SVC', 'SVC'), ('SYP', 'SYP'), ('SZL', 'SZL'), ('THB', 'THB'), ('TJS', 'TJS'), ('TMT', 'TMT'), ('TND', 'TND'), ('TOP', 'TOP'), ('TRY', 'TRY'), ('TTD', 'TTD'), ('TVD', 'TVD'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('UAH', 'UAH'), ('UGX', 'UGX'), ('USD', 'USD'), ('USN', 'USN'), ('UYI', 'UYI'), ('UYU', 'UYU'), ('UZS', 'UZS'), ('VND', 'VND'), ('VUV', 'VUV'), ('WST', 'WST'), ('XAF', 'XAF'), ('XAG', 'XAG'), ('XAU', 'XAU'), ('XBA', 'XBA'), ('XBB', 'XBB'), ('XBC', 'XBC'), ('XBD', 'XBD'), ('XCD', 'XCD'), ('XDR', 'XDR'), ('XFO', 'XFO'), ('XFU', 'XFU'), ('XOF', 'XOF'), ('XPD', 'XPD'), ('XPF', 'XPF'), ('XPT', 'XPT'), ('XSU', 'XSU'), ('XTS', 'XTS'), ('XUA', 'XUA'), ('XXX', 'XXX'), ('YER', 'YER'), ('ZAR', 'ZAR'), ('ZMW', 'ZMW'), ('ZWN', 'ZWN')], max_length=3)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='companies.brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='companies.brand')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_details', to='menus.category')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_details', to='menus.menu')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_details', to='menus.product')),
            ],
        ),
        migrations.AddConstraint(
            model_name='menudetail',
            constraint=models.UniqueConstraint(fields=('menu', 'product'), name='unique_product'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('parent', 'name'), name='unique_category'),
        ),
    ]
