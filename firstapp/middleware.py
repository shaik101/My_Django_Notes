
from django.http import HttpResponse

class Maintenance:

    def __init__(self,get_response):
        self.get_response = get_response
    
    def __call__(self,request):
        request.GET = request.GET.copy()
        request.GET['test'] = "testing"

        response = self.get_response(request)

        # return HttpResponse("Maintenance Mode")

        return response
    
    def process_exception(self,request,exception):

        print(exception)

        return HttpResponse(exception)

