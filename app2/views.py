from django.shortcuts import render
from django.http import HttpResponse
# Create your v
# iews here.
def index(request):
    html="""
    <h1>App2 titulo</h1>
    <br>
    <p>parrafo app2</p>

"""
    return HttpResponse(html)

def vista2(request):
    html="""
<h4>Titulo de la vista 2</h4>
<hr>
<p>Parrafo de la vista 2</p>


"""
    return HttpResponse(html)