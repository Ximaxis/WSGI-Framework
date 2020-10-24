
from urls import urlpatterns
from core.wsgi import Application, FakeApplication, DebugApplication


# Front controllers
def secret_front(request):
	request['secret'] = 'My secret'


front_controller = [secret_front]

#application = Application(urlpatterns, front_controller)
#application = DebugApplication(urlpatterns, front_controller)
application = FakeApplication(urlpatterns, front_controller)