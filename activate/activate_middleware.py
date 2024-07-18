from .models import ActivateLog


class activate_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if 'admin' not in str(request.path):
                # Create a log entry
                ActivateLog.objects.create(
                    user=request.user,
                    method=request.method,
                    ip_address=request.META.get('REMOTE_ADDR'),
                    url=request.path,
                    user_agent=request.META.get('HTTP_USER_AGENT'),
                
                )
        # Code to be executed for each request/response after
        # the view is called.

        return response

   
