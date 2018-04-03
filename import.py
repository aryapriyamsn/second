import csv, sys, os

project_dir = "/Users/priyam/Desktop/django/old_projects/beta/beta/beta"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from users.models import Users

data = csv.reader(open("/Users/priyam/Desktop/django/old_projects/beta/beta/user_id.csv"),delimiter=",")

for row in data:
	instance = Users()
	instance.user_id=row[0]
	instance.save()
	