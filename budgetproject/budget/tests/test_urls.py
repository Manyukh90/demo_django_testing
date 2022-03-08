from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, ProjectCreateView, project_detail 

# class TestUrls(SimpleTestCase):

#     def test_list_url_resolves(self):
#         # assert 1 == 2
#         url = reverse('list')
#         print(url)
#         print('----------')
#         print(resolve(url))
#         print('----------')
#         print(resolve(url).func)
#         print('----------')
#         self.assertEquals(resolve(url).func, project_list)
#         print('----------')

#     def test_add_url_resolves(self):
#         # assert 1 == 2
#         url = reverse('add')
#         print(url)
#         print('----------')
#         print(resolve(url))
#         print('----------')
#         print(resolve(url).func)
#         print('----------')
#         self.assertEquals(resolve(url).func.view_class, ProjectCreateView)
#         print('----------')  

#     def test_detail_url_resolves(self):
#         # assert 1 == 2
#         url = reverse('detail', args=['some-slug'])
#         print(url)
#         print('----------')
#         print(resolve(url))
#         print('----------')
#         print(resolve(url).func)
#         print('----------')
#         self.assertEquals(resolve(url).func, project_detail)
#         print('----------')    