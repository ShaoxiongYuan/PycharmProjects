import jwt
from django.conf import settings
from django.http import JsonResponse
from user.models import UserProfile


def login_check(func):
    def wrapper(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return JsonResponse({'code': 403, 'error': 'Please login.'})
        try:
            info = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms='HS256')
        except Exception as e:
            print(e)
            return JsonResponse({'code': 403, 'error': 'Please login.'})

        username = info['username']
        user = UserProfile.objects.get(username=username)
        request.myuser = user

        return func(self, request, *args, **kwargs)

    return wrapper
