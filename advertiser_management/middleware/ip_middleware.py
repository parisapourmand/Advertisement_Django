class IPMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR')

        response = self.get_response(request)

        print("**********response*********")
        print(response)

        return response
