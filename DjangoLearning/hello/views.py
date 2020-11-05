from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from django.views.generic import TemplateView
from django.views.generic import FormView

# Create your views here.
""" def index(request):
    params = {
        'title':'Hello',
        'message':'all friends',
        'form':HelloForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
    return render(request, 'hello/index.html', params) """

class UserView(TemplateView):
    def __init__(self):
        self.data = Friend.objects.all()
        self.params ={
            'title': 'Hello',
            'data': self.data,
        }

    def get(self, request):
        return render(request, 'hello/index.html', self.params)

class CreateView(FormView):
    def __init__(self):
        self.params = {
            'title': 'Create User',
            'form':FriendForm(),
        }

    def post(self, request):
        self.obj = Friend()
        self.friend = FriendForm(request.POST, instance=self.obj)
        self.friend.save()
        return redirect(to='/hello')

    def get(self, request):
        return render(request, 'hello/create.html', self.params)

class EditView(FormView):
    def __init__(self):
        self.params = {
            'title':"Edit User",
        }

    def get(self,request, num):
        self.obj=Friend.objects.get(id=num)
        self.params['id'] =num
        self.params['form'] = FriendForm(instance=self.obj)
        return render(request, 'hello/edit.html', self.params)

    def post(self, request, num):
        self.obj = Friend.objects.get(id=num)
        self.friend=FriendForm(request.POST, instance=self.obj)
        self.friend.save()
        return redirect(to="/hello")

class DeleteView(TemplateView):
    def __init__(self):
        self.params = {
            'title':'Delete User'
        }

    def get(self,request,num):
        self.friend = Friend.objects.get(id=num)
        self.params['id'] = num
        self.params['obj'] = self.friend
        return render(request, 'hello/delete.html', self.params)

    def post(self, request, num):
        self.friend = Friend.objects.get(id=num)
        self.friend.delete()
        return redirect(to='/hello')
