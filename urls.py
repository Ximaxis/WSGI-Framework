import views

urlpatterns = {
	'/': views.Main(),
	'/category/': views.CategoriesList(),
	'/contact/': views.Contact(),
	'/create-category/': views.CreateCategory(),
	'/create-course/': views.CreateCourse(),
	'/copy-course/' :  views.copy_course,
}