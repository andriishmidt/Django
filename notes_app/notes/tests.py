from django.test import TestCase
from django.urls import reverse
from .models import Articles, Category

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Personal")
        self.assertEqual(category.name, "Personal")

class ArticlesModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Work")
        self.article = Articles.objects.create(
            title="Test Note",
            full_text="This is a test note.",
            reminder="Reminder text",
            date="2025-03-25 10:00:00",
            categories=self.category
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Note")
        self.assertEqual(self.article.full_text, "This is a test note.")
        self.assertEqual(self.article.reminder, "Reminder text")
        self.assertEqual(self.article.categories, self.category)

class ViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Health")
        self.article = Articles.objects.create(
            title="Workout Plan",
            full_text="Go to the gym daily.",
            reminder="Evening workout",
            date="2025-03-25 18:00:00",
            categories=self.category
        )

    def test_index_view(self):
        response = self.client.get(reverse('home'))  # Make sure 'home' is the correct URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Workout Plan")

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Health")

    def test_delete_note(self):
        response = self.client.post(reverse('delete_note', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertFalse(Articles.objects.filter(id=self.article.id).exists())  # Note should be deleted
