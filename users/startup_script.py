import os
import django

from django.db import IntegrityError
from django.contrib.auth import get_user_model

# configure django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "users.settings")
django.setup()

User = get_user_model()

try:
    u = User(username="superadmin")
    u.set_password("superadminpassword123")
    u.is_superuser = True
    u.is_staff = True
    u.save()

except IntegrityError:
    print(f"superadmin already exists")
