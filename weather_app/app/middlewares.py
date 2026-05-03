def first_middleware(get_response):
    
    def middleware(request):

        print('⚡start the 1️⃣  FIRST MIDDLEWARE')

        response = get_response(request)

        print('🔚 end the 1️⃣  FIRST MIDDLEWARE')

        return response
    
    return middleware


class SecondMiddleware:
    def __init__(self,get_response):

        self.get_response = get_response

    def __call__(self,request):
        print('⚡start the 2️⃣  SECOND MIDDLEWARE')

        response = self.get_response(request)

        print('🔚 end the 2️⃣  SECOND MIDDLEWARE')

        return response

import time    
class Logging:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        start = time.time()

        response = self.get_response(request)

        duration = time.time() - start

        print(f"{request.method} - {request.path} => {duration:.2f}")

        return response

from django.core.cache import cache
from django.http import JsonResponse
class RateLimitMiddleware:
    def __init__(self,get_response):
        
        self.get_response = get_response

    def __call__(self,request):

        ip = request.META.get('REMOTE_ADDR')
        key = f"rate_limit_{ip}"
        
        requests = cache.get(key,0)

        if requests > 100:
            return JsonResponse({"error":"Too many requests"},status=429)
        
        cache.set(key,requests + 1,timeout=60)

        return self.get_response(request)    
    

class SecurityHeaderMiddleware:

    def __init__(self,get_response):

        self.get_response = get_response

    def __call__(self,request):
        
        response = self.get_response(request)

        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['X-XSS-Protection'] = '1; mode=block'

        return response
    
class TenantMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        host = request.get_host()

        if "company1" in host:
            request.tenant = "company1"    
        elif "company2" in host:
            request.tenant = "company2"

        tenant=getattr(request, "tenant", None)
        print(tenant)

        return self.get_response(request)


from django.http import HttpResponse

def mantenance_middleware(get_response):

    def middleware(request):
        
        maintenance_mode = False
        
        if maintenance_mode:
            return HttpResponse("<h1>Site dose under maintenance...</h1>",status=503)
        
        return get_response(request)
    
    return middleware
    
        