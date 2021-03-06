# Generated by Django 2.1.4 on 2019-04-07 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistantmodel', '0003_auto_20190313_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courselog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_operate', models.CharField(max_length=6)),
                ('log_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_renname', models.CharField(max_length=20, null=True)),
                ('file_filename', models.CharField(max_length=50, null=True)),
                ('file_groups', models.CharField(max_length=10, null=True)),
                ('file_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='cour_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_member1',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='studentset1', to='assistantmodel.Student', to_field='stu_id'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_member2',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='studentset2', to='assistantmodel.Student', to_field='stu_id'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_member3',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='studentset3', to='assistantmodel.Student', to_field='stu_id'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_member4',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='studentset4', to='assistantmodel.Student', to_field='stu_id'),
        ),
        migrations.AddField(
            model_name='courselog',
            name='log_cour',
            field=models.ForeignKey(on_delete='CASCADE', related_name='logcourseset', to='assistantmodel.Course', to_field='cour_id'),
        ),
        migrations.AddField(
            model_name='courselog',
            name='log_stu',
            field=models.ForeignKey(on_delete='CASCADE', related_name='logstudentset', to='assistantmodel.Student', to_field='stu_id'),
        ),
    ]
