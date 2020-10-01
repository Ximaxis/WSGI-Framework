from core.templator import render
from datetime import date

class NotFound404View:
	def __call__(self, request):
		content = '<h1>404 PAGE Not Found</h1>'
		return '404 WHAT', content	


class Other:
	
	def __call__(self, request):
		content = render('other.html',
		title = "Прочее")
		return '200 OK', content


class Contact:
	
	def __call__(self, request):
		if request['method'] == 'POST':
			data = request['data']
			with open('text.txt', 'w') as file:
				for key,val in data.items():
					file.write(f'{key}:{val}\n')
		content = render('contact.html',
		title = "Контакты"   )
		return '200 OK', content


class Main:

	def __call__(self, request):
		today = date.today()
		content = render('index.html', 
		object_list=[{'name': 'Maxis_EA'}],
		today = today,
		title = "Главная")
		return '200 OK', content
