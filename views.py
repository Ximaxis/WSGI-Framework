from core.templator import render
from datetime import date
from models import TrainingSite

site = TrainingSite()

class NotFound404View:
	def __call__(self, request):
		content = '<h1>404 PAGE Not Found</h1>'
		return '404 WHAT', content	


class CategoriesList:
	
	def __call__(self, request):
		content = render('other.html',
		title = "Список категорий", 
		objects=site.courses, 
		objects_list=site.categories)
		return '200 OK', content


class CreateCategory:

	def __call__(self, request):
		if request['method'] == 'POST':
			data = request['data']
			name = data['name']
			category_id = data.get('category_id')

			category = None
			if category_id:
				category = site.find_category_by_id(int(category_id))

			new_category = site.create_category(name, category)
			site.categories.append(new_category)
			return '200 OK', render('create.html')
		else:
			categories = site.categories
			return '200 OK', render('create.html', categories=categories)


class CreateCourse:

	def __call__(self, request):
		if request['method'] == 'POST':
			data = request['data']
			name = data['name']
			category_id = data.get('category_id')

			category = None
			if category_id:
				category = site.find_category_by_id(int(category_id))

				course = site.create_course('record', name, category)
				site.courses.append(course)
			return '200 OK', render('create.html')
		else:
			categories = site.categories
			return '200 OK', render('create.html', categories=categories)


def copy_course(request):
    request_params = request['request_params']
    name = request_params['name']
    old_course = site.get_course(name)
    if old_course:
        new_name = f'copy_{name}'
        new_course = old_course.clone()
        new_course.name = new_name
        site.courses.append(new_course)

    return '200 OK', render('other.html', objects=site.courses)


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
