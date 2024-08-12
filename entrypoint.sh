#!/bin/bash

# Navigate to the working directory
cd /app/

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Execute the container's main command (passed as arguments)
exec "$@"
