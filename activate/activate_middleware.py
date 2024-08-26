# activate/activate_middleware.py

from .models import ActivateLog

class ActivateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if 'admin' not in str(request.path):
            user = request.user if request.user.is_authenticated else None
            ActivateLog.objects.create(
                user=user,  # Ensure that user is either a User instance or None
                method=request.method,
                ip_address=request.META.get('REMOTE_ADDR'),
                url=request.path,
                user_agent=request.META.get('HTTP_USER_AGENT'),
            )
        # Code to be executed for each request/response after
        # the view is called.

        return response
