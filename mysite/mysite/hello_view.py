from django.http import HttpResponse, Http404
from django.template import Template, Context, loader


def hello(request):  
    message = "<html><body>Hello. Django!</body></html>"
    return HttpResponse(message, content_type='text/plain')

def error(request):
    raise Http404

def getIP(request):
    return HttpResponse(request.META['REMOTE_ADDR'], content_type='text/plain')


def form_test(request):
    message = """
        <html>
                <body>
                            <form action='http://localhost:8000/formdata/' method="GET">
                                            <p>Given name<input name="given_name" type="text"/></p>
                                                            <p>Family name<input name="family_name" type="text"/></p>
                                                                            <p><input type="submit" value="hello"/></p>
                                                                                        </form>
                                                                                                </body>
                                                                                                    </html>
              """
    return HttpResponse(message)

def greet_with_form_data(request):
    given_name = request.GET['given_name']
    family_name = request.GET['family_name']
    return HttpResponse('Hello, %s %s!' % (given_name, family_name))

def reverse_url_bit(request, bit=''):
    return  HttpResponse(reversed(bit), content_type='text/plain')

def url_sum(request, a, b):
    a = int(a, 10)
    b = int(b, 10)
    return HttpResponse(str(a*b), content_type='text/plain')

def show_metadata(request):
    template_string = """
    <html>
    <body>
        <table>
        <tr><td>Key</td><td>Value</td></tr>
        {% for item in metadata.items %}
        <tr>
        <td>{{item.0}}</td><td>{{item.1}}</td>
         <tr>
         {% endfor %}
        <table>
     </body>
    </html>
    """
    template = Template(template_string)
    context = Context()
    context.update({'metadata': request.META})
    return HttpResponse(template.render(context))

def show_metadata_with_load(request):
    context = Context()
    context.update(dict(metadata=request.META))
    template = loader.get_template('showmeta.html')
    return HttpResponse(template.render(context))
