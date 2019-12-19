import pytest

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import TestCase

from tests.user_logins import ADMIN_USER


class MediaUploadResourceTest(TestCase):
    fixtures = ['tests/test_user.json',
                'tests/test_oppia.json',
                'tests/test_quiz.json',
                'tests/test_permissions.json']

    course_file_path = './oppia/fixtures/reference_files/ncd1_test_course.zip'
    media_file_path = './oppia/fixtures/reference_files/sample_video.m4v'
    corrupt_media_file_path = \
        './oppia/fixtures/reference_files/corrupt_video.m4v'

    def setUp(self):
        super(MediaUploadResourceTest, self).setUp()
        self.admin_user = User.objects.get(pk=ADMIN_USER['id'])

    @pytest.mark.xfail(reason="works on local, but not on Github workflow \
        see issue: https://github.com/DigitalCampus/django-oppia/issues/689")
    def test_upload_template(self):
        with open(self.media_file_path, 'rb') as media_file_content:
            media_file = SimpleUploadedFile(media_file_content.name,
                                            media_file_content.read(),
                                            content_type="video/m4v")

        self.client.force_login(self.admin_user)
        response = self.client.post(reverse('oppia_av_upload'),
                                    {'media_file': media_file})
        self.assertRedirects(response,
                             reverse('oppia_av_upload_success', args=[4]),
                             302,
                             200)

    @pytest.mark.xfail(reason="works on local, but not on Github workflow \
        see issue: https://github.com/DigitalCampus/django-oppia/issues/689")
    def test_upload_template_corrupt_media(self):
        with open(self.corrupt_media_file_path, 'rb') as media_file_content:
            media_file = SimpleUploadedFile(media_file_content.name,
                                            media_file_content.read(),
                                            content_type="video/m4v")

        self.client.force_login(self.admin_user)
        response = self.client.post(reverse('oppia_av_upload'),
                                    {'media_file': media_file})
        self.assertRaisesMessage(Exception, "Corrupted media file")
        self.assertEqual(response.status_code, 200)
