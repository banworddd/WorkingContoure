from django.test import TestCase
from projects.models import Project
from django.contrib.auth import get_user_model


User = get_user_model()


class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

    def setUp(self):
        self.project = Project.objects.create(
            name='test_project',
            owner=self.user
        )

    def test_project_str_returns_name(self):
        self.assertEqual(
            str(self.project),
            self.project.name
        )

    def test_project_default_status_is_active(self):
        self.assertEqual(
            self.project.status,
            Project.ProjectStatusChoices.ACTIVE
        )

    def test_project_belongs_to_user(self):
        self.assertEqual(
            self.user,
            self.project.owner
        )

    def test_user_has_project_in_related_name(self):
        self.assertIn(
            self.project,
            self.user.projects.all()
        )