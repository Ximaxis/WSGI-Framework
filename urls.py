import views

urlpatterns = {
	'/': views.Main(),
	'/other/': views.Other(),
	'/contact/': views.Contact(),
}