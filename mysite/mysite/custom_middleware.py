from urllib import response


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("custom middleware before next middleware/view")

        print(2+2, " addition when the request comes")

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        print(10-2, "subtraction after getting the response")

        # Code to be executed for each response after the view is called 
        # 
        print("custom middleware after response or previous middleware")
        
        return response
        