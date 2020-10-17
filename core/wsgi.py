from views import NotFound404View

class Application:

	def get_wsgi_input_data(self, environ):
		content_length_data = environ.get('CONTENT_LENGTH')
		content_length = int(content_length_data) if content_length_data else 0
		data = environ['wsgi.input'].read(content_length) if content_length > 0 else b''
		return data
	
	def parse_wsgi_input_data(self, data: bytes):
		result = {}
		if data:
			data_str = data.decode(encoding='utf-8')
			result = self.parse_input_data(data_str)
		return result
	
	def parse_input_data(self, data: str):
		result = {}
		if data:
			params = data.split('&')
			for item in params:
				k, v = item.split('=')
				result[k] = v
		return result
	
	def __init__(self, urlpatterns: dict, front_controller: list):
		self.urlpatterns = urlpatterns
		self.front_controller = front_controller
	
	def __call__(self, environ, start_response):
		path = environ['PATH_INFO']
		if not path.endswith('/'):
			path = f'{path}/'
			
		method = environ['REQUEST_METHOD']
		data = self.get_wsgi_input_data(environ)
		data = self.parse_wsgi_input_data(data)
		
		query_string = environ['QUERY_STRING']
		request_params = self.parse_input_data(query_string)

		# Если нет такой вьюхи отправляет 404
		view = NotFound404View()

		if path in self.urlpatterns:
			# получаем view по url
			view = self.urlpatterns[path]
			request = {}
			request['method'] = method
			request['data'] = data
			request['request_params'] = request_params
		# добавляем в запрос данные из front controllers
		for front in self.front_controller:
			front(request)
		# вызываем view, получаем результат
		code, body = view(request)
		# возвращаем заголовки
		start_response(code, [('Content-Type', 'text/html')])
		# возвращаем тело ответа
		return [body.encode('utf-8')]