from django.shortcuts import render
from django.http import HttpResponse
# Create your v
# iews here.
def index(request):
    html="""
    <h1>App3 titulo</h1>
    <br>
    <p>parrafo app3</p>

"""
    return HttpResponse(html)

def vista3(request):
    html="""
<h4>Titulo de la vista 3</h4>
<hr>
<p>Parrafo de la vista 3</p>


"""
    return HttpResponse(html)