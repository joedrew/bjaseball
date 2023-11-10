from django.db import models


class TeamYearID(models.Model):
    year = models.IntegerField()
    league = models.CharField(max_length=2)
    team_id = models.CharField(max_length=3)
    franchise_id = models.CharField(max_length=3)
    fangraphs_team_id = models.IntegerField()
    baseball_reference_team_id = models.CharField(max_length=3)
    retrosheet_team_id = models.CharField(max_length=3)
