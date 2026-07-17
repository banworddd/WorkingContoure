from django.test import TestCase
from projects.models import Project
from tasks.models import Task
from django.contrib.auth import get_user_model


User = get_user_model()


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )
        cls.project = Project.objects.create(
            name='test_project',
            owner=cls.user
        )

    def setUp(self):
        self.task = Task.objects.create(
            title='test_task',
            project=self.project,
            created_by=self.user
        )

    def test_task_creation_default(self):
        self.assertEqual(
            self.task.status,
            Task.TaskStatusChoices.TODO
        )

    def test_task_str_returns_title(self):
        self.assertEqual(
            str(self.task),
            self.task.title
        )

    def test_task_belongs_to_project(self):
        self.assertEqual(
            self.project,
            self.task.project
        )

    def test_project_has_task_in_related_name(self):
        self.assertIn(
            self.task,
            self.project.tasks.all()
        )

