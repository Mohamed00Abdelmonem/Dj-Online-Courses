import ipinfo
from .models import ActivateLog

# Use your actual access token from ipinfo.io
ACCESS_TOKEN = 'f07aac8d3e1ff2'
handler = ipinfo.getHandler(ACCESS_TOKEN)

def activate_middleware(get_response):
    def middleware(request):
        response = get_response(request)

        # Get IP address
        ip_address = request.META.get('REMOTE_ADDR')
        
        # Fetch location information using ipinfo
        details = handler.getDetails(ip_address)
        city = details.city
        region = details.region
        country = details.country
        
        # Create a log entry
        ActivateLog.objects.create(
            user=request.user,
            method=request.method,
            ip_address=ip_address,
            url=request.path,
            user_agent=request.META.get('HTTP_USER_AGENT'),
            city=city,
            region=region,
            country=country
        )

        return response

    return middleware
