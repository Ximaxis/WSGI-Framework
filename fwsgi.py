from templator import render


# def application(environ, start_response):
# 	start_response('200 OK', [('Content-Type', 'text/html')])
# 	return [b'Hello world from a simple WSGI application!']

# page controller


def index_view(request):
	content = render('authors.html',
								object_list=[{'name': 'Maxim'}, {'name': 'Baranov'}])
	return '200 OK', content


def abc_view(request):
	return '200 OK', '<h1>Random page</h1>'


def not_found_404_view(request):
	print(request)
	return '404 WHAT', '404 PAGE Not Found'

	


class Other:
	
	def __call__(self, request):
		secret = request.get('secret', None)
		content = f'Main {secret}'
		return '200 OK', content


class About:
	
	def __call__(self, request):
		return '200 OK', 'About'


class Authors:

	def __call__(self, request):
		content = render('authors.html', object_list=[{'name': 'Max'}, {'name': 'Baranov'}])
		return '200 OK', content


routes = {
	'/': index_view,
	'/abc/': abc_view,
	'/other/': Other(),
	'/about/': About(),
	'/Authors_class/': Authors(),
}


# Front controllers
def secret_front(request):
	request['secret'] = 'My secret'


def other_front(request):
	request['key'] = 'key'


fronts = [secret_front]


class Application:
	
	def __init__(self, routes, fronts):
		self.routes = routes
		self.fronts = fronts
	
	def __call__(self, environ, start_response):
		path = environ['PATH_INFO']
		view = not_found_404_view
		if path in self.routes:
			view = self.routes[path]
		request = {}
		# front controller
		for front in self.fronts:
			front(request)
		
		code, body = view(request)
		start_response(code, [('Content-Type', 'text/html')])
		return [body.encode('utf-8')]


application = Application(routes, fronts)
