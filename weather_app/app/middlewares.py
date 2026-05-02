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

    
