# Generated by Django 2.2 on 2019-11-12 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('ImageId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ImageName', models.CharField(max_length=300)),
                ('ImageSize', models.CharField(max_length=300)),
                ('ImageLink', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('ProductId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=50)),
                ('ProductCategory', models.CharField(max_length=20)),
                ('ProductPrice', models.CharField(max_length=20)),
                ('ProductDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('ProductText', models.CharField(max_length=300)),
                ('ProductType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('UserId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=20)),
                ('UserNameSet', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('KakaoId', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserImageModel',
            fields=[
                ('UserImageModelId', models.AutoField(primary_key=True, serialize=False)),
                ('ImageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.ImageModel')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.UserModel')),
            ],
        ),
        migrations.CreateModel(
            name='SaleModel',
            fields=[
                ('SaleId', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('SaleDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.ProductModel')),
            ],
        ),
        migrations.CreateModel(
            name='ProImageModel',
            fields=[
                ('ProImageModelId', models.AutoField(primary_key=True, serialize=False)),
                ('ImageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.ImageModel')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.ProductModel')),
            ],
        ),
        migrations.AddField(
            model_name='productmodel',
            name='UserId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.UserModel'),
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('Like', models.AutoField(primary_key=True, serialize=False)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.ProductModel')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.UserModel')),
            ],
        ),
    ]
