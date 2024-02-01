#!/usr/bin/env bash

wait_count=0
while ! python3 manage.py shell -c "
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute('select 1')
    cursor.fetchall()
"  #  2> /dev/null
do
  echo Wait until DB is ready... $((wait_count += 1))
  sleep 5
done

if [ "${ENVIRONMENT_TIER}" = "app" ]; then
    python manage.py
fi

# gunicorn --bind 0.0.0.0:8000 --capture-output --timeout 0 --workers=2 wsgi:application
python3 manage.py runserver 0.0.0.0:8000