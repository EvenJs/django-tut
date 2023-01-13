# Create your tests here.
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase): 
    def test_was_published_recently_with_futhure_question():
        '''
        was_published_recently() returns False for questions whose pub_date
        is in the future 
    '''