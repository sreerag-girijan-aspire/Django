import time
from django.http import HttpResponseForbidden


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # The next middleware or view

    def __call__(self, request):
        start_time = time.time()  # Track the start time

        # Process the request (this passes control to the next middleware or view)
        response = self.get_response(request)

        end_time = time.time()  # Track the end time
        duration = end_time - start_time
        print(f"Request took {duration:.3f} seconds")

        return response





class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You are not authenticated.")

        # Proceed to the next middleware or view
        response = self.get_response(request)
        return response


class AddCustomHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request (you can modify request here if needed)
        response = self.get_response(request)

        # Add custom headers to the response
        response['X-Custom-Header'] = 'SomeValueBySree'
        return response