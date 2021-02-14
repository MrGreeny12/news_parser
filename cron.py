from django_cron import CronJobBase, Schedule

class CronJob(CronJobBase):
    RUN_EVERY_MINS = 180 # every 3 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'parsing.management.commands.parser.py'

    def do(self):
        pass