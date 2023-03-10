from django.test import TestCase, Menu

class MenuViewTest(TestCase):
    def setup(self):
        items = Menu.objects.all()
        self.assertEqual(items, f'{self.title} : {str(self.price)}')
    
    def test_getall(self):
        client = Menu()
        response = client.get('menu/')
        
        self.assertEqual(response.status_code, 200)