from django.test import TestCase

# Create your tests here.

from .models import Question, Choice
import datetime
from django.utils import timezone
class QuestionModelTestCase(TestCase):
    def test_was_published_recently(self):
        some_time_in_the_future = timezone.now() + datetime.timedelta(days=30)
        q = Question(pub_date = some_time_in_the_future)
        self.assertFalse(q.was_published_recently())
