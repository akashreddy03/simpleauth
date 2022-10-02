python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; import os; User.objects.create_superuser(os.environ['DJ_USERNAME'], os.environ['DJ_EMAIL'], os.environ['DJ_PASS'])" | python manage.py shell