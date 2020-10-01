
from urls import urlpatterns
from core.wsgi import Application


# Front controllers
def secret_front(request):
	request['secret'] = 'My secret'


front_controller = [secret_front]

application = Application(urlpatterns, front_controller)
