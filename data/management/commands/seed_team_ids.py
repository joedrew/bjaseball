from django.core.management.base import BaseCommand
from pybaseball import team_ids

from data.models import TeamYearID


class Command(BaseCommand):
    help = "recreate team id models"

    def handle(self, *args, **options):
        seed_team_ids()
        self.stdout.write("done.")


def create_obj(row):
    print(row)
    obj = TeamYearID(
        year=row["yearID"],
        league=row["lgID"],
        team_id=row["teamID"],
        franchise_id=row["franchID"],
        fangraphs_team_id=row["teamIDfg"],
        baseball_reference_team_id=row["teamIDBR"],
        retrosheet_team_id=row["teamIDretro"],
    )
    obj.save()


def seed_team_ids():
    print("deleting TeamYearIDs")
    TeamYearID.objects.all().delete()

    ids = team_ids()

    ids.apply(create_obj, axis=1)
