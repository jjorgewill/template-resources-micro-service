import requests
from django.http import JsonResponse
from django.core.cache import cache
from apps.core import models as models_security
CACHE_TTL = 60 * 15


class UserAuthMidleware:
    """
        This class ensure every request have been execute by one user the platform
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request:
            TOKEN = request.META.get("HTTP_AUTHORIZATION")
            user = cache.get(TOKEN, None)
            if not user:
                url = 'http://URL_SERVICE_AUTH/rest-auth/user/'
                headers = {'Content-Type': 'application/x-www-form-urlencoded',
                           'Authorization': TOKEN}

                r = requests.get(url, headers=headers)
                if r.status_code == 403:
                    print("no user")
                if r.status_code == 200:
                    user = r.json()
                    cache.set(TOKEN, user, timeout=CACHE_TTL)
                    perfil = models_security.Profile.objects.filter(usuario=user.get('pk')).first()
                    if not perfil:
                        print("crear perfil")
                        return JsonResponse({'msg':'Usuario sin perfil'})
                    else:
                        cache.set('%s-%s' % ("perfil", TOKEN), perfil, timeout=CACHE_TTL)
                        print('verficar los permisos')
                    # return
            else:
                print(cache.get(TOKEN))

        response = self.get_response(request)
        return response

