import json
import bcrypt
import jwt
import re

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import User


class UserView(View):
    def validate_id(self, user_id):
        if User.objects.filter(user_id=user_id).exists():
            return False
        return True

    def validate_pw(self, password):
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@.#^* ?+=_~])[A-Za-z\d!@.#^* ?+=_~]{8,}$", password):
            return False
        return True

    def validate_name(self, name):
        if name is None or len(name) == 0:
            return False
        return True

    def validate_birth_date(self, birth_date):
        if birth_date is None or len(birth_date) == 0:
            return False
        if not re.match(r"(\d{4})-(\d{2})-(\d{2})", birth_date):
            return False
        return True

    def validate_phone(self, phone):
        if User.objects.filter(phone=phone).exists():
            return False
        if phone is None or len(phone) == 0:
            return False
        return True

    def validate_email(self, email):
        if email is None or len(email) == 0 or not re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            return False
        if User.objects.filter(email=email).exists():
            return False
        return True

    def post(self, request):
        try:
            data = json.loads(request.body)
            hashed_password = bcrypt.hashpw(
                data['password'].encode('utf-8'), bcrypt.gensalt())

            VALIDATION_RULES = {
                'user_id': self.validate_id,
                'password': self.validate_pw,
                'name': self.validate_name,
                'birth_date': self.validate_birth_date,
                'phone': self.validate_phone,
                'email': self.validate_email,
            }

            for field, validator in VALIDATION_RULES.items():
                if not validator(data[field]):
                    return HttpResponse(status=400)

            User.objects.create(
                user_id=data['user_id'],
                password=hashed_password.decode('utf-8'),
                name=data['name'],
                birth_date=data['birth_date'],
                phone=data['phone'],
                email=data['email'],
                address=data.get('address', None),
            )
            return HttpResponse(status=200)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)
