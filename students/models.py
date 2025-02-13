# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answerdiscussion(models.Model):
    id = models.IntegerField(primary_key=True)
    id_students = models.IntegerField(blank=True, null=True)
    id_topicdiscussion = models.IntegerField(db_column='id_topicDiscussion', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField()
    file = models.TextField(blank=True, null=True)
    reactions = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answerdiscussion'


class Categirytopic(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categirytopic'


class Categorynote(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorynote'


class Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    teacher = models.CharField(max_length=75, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    sector_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'


class Cooperation(models.Model):
    id = models.IntegerField(primary_key=True)
    id_students = models.IntegerField(blank=True, null=True)
    id_project = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cooperation'


class Filesproject(models.Model):
    id = models.IntegerField(primary_key=True)
    id_project = models.IntegerField(blank=True, null=True)
    link = models.TextField()
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filesproject'


class Notes(models.Model):
    id = models.IntegerField(primary_key=True)
    id_categorynote = models.IntegerField(db_column='id_categoryNote', blank=True, null=True)  # Field name made lowercase.
    id_students = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=75)
    content = models.TextField(blank=True, null=True)
    type_note = models.CharField(max_length=45, blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    students_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class Sector(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'sector'


class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    pseudo = models.CharField(max_length=45)
    civilitÚ = models.CharField(max_length=45, blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=45)
    pass_field = models.CharField(db_column='pass', max_length=45)  # Field renamed because it was a Python reserved word.
    sector_id = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    id_topicforum = models.IntegerField(db_column='id_topicForum', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class Tasks(models.Model):
    id = models.IntegerField(primary_key=True)
    id_students = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=45)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    notification = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tasks'


class Topicdiscussion(models.Model):
    id = models.IntegerField(primary_key=True)
    id_students = models.IntegerField(blank=True, null=True)
    id_topicforum = models.IntegerField(db_column='id_topicForum', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField()
    reaction = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topicdiscussion'


class Topicforum(models.Model):
    id = models.IntegerField(primary_key=True)
    id_students = models.IntegerField(blank=True, null=True)
    id_categirytopic = models.IntegerField(db_column='id_categiryTopic', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=200)
    reactions = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topicforum'
