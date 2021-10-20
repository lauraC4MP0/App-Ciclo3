# Generated by Django 3.2.8 on 2021-10-07 04:33

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id_departament', models.AutoField(primary_key=True, serialize=False)),
                ('name_departament', models.CharField(max_length=15, verbose_name='Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('date_sale', models.DateTimeField(max_length=30)),
                ('date_delivery', models.DateTimeField(max_length=30)),
                ('total_order', models.IntegerField()),
                ('sales_unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usersname', models.IntegerField(primary_key=True, serialize=False, verbose_name='Num Doc de Identidad')),
                ('name_user', models.CharField(max_length=30, verbose_name='Nombres')),
                ('lastname_user', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('email', models.CharField(max_length=100, verbose_name='Correo electronico')),
                ('address_user', models.CharField(max_length=50, verbose_name='Direccion')),
                ('id_city', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('id_department', models.CharField(max_length=50, verbose_name='Departamento')),
                ('num_phone', models.IntegerField(verbose_name='Telefono')),
                ('password', models.CharField(max_length=256, verbose_name='Contraseña')),
                ('sex_user', models.CharField(choices=[('Masculino', 'Masculino')], max_length=10)),
                ('rol_user', models.CharField(choices=[('Vendedor', 'Vendedor')], max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=30)),
                ('description_product', models.CharField(max_length=80, null=True)),
                ('price_product', models.IntegerField()),
                ('sales_unit_product', models.CharField(max_length=20)),
                ('amount_product', models.IntegerField()),
                ('image_product', models.BinaryField(null=True)),
                ('username_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id_order_detail', models.AutoField(primary_key=True, serialize=False)),
                ('total_price_product', models.IntegerField()),
                ('amount_order', models.IntegerField()),
                ('id_order_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AgronetApp.order')),
                ('id_product_fk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AgronetApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id_city', models.AutoField(primary_key=True, serialize=False)),
                ('name_city', models.CharField(max_length=30, verbose_name='Ciudad')),
                ('Departament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Departamento', to='AgronetApp.departament')),
            ],
        ),
    ]