from django.db import models

# Create your models here.

class Players(models.Model):
    player_id = models.AutoField(blank=True, primary_key=True)
    team_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    position = models.CharField(max_length=10, blank=True, null=True)
    id = models.IntegerField(blank=True, null=False, primary_key=False)
    position_id = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'players'


class Teams(models.Model):
    team_id = models.IntegerField(blank=True, null=True)
    team_name = models.CharField(max_length=500, blank=True, null=True)
    owner = models.CharField(max_length=500, blank=True, null=True)
    id = models.IntegerField(blank=True, null=False,primary_key=True)

    class Meta:

        db_table = 'teams'


class Draft_Picks(models.Model):
    id = models.IntegerField(blank=True, null=False, primary_key=True)
    team_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True,null=True)
    round = models.IntegerField(blank=True,null=True)
    owner_id = models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = 'draft_picks'
