from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    a='''
    <h1>Hello</h1>
    '''
    return HttpResponse(a)