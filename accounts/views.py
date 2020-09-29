from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.

def login(request):
    if request.method == "POST":
        pass
        # form = MyForm(request.POST)
        # if form.is_valid():
            # <process form cleaned data>
            # return HttpResponseRedirect('/success/')

    return render(request, 'accounts/index.html',{'title':'Login'})

# from .forms import MyForm

class MyFormView(View):
    # form_class = MyForm
    initial = {'title': 'Login'}
    template_name = 'accounts/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'title': initial})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        # user = authenticate(username=username, password=password)

        # if user is not None:
        #     if user.is_active:
        #         login(request, user)

        #         return HttpResponseRedirect('/form')
        #     else:
        #         return HttpResponse("Inactive user.")
        # else:
        #     return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, self.template_name)