from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

class AudioUploadTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user('testuser', password='testpassword')

    def test_audio_upload(self):
        self.client.login(username='testuser', password='testpassword')

        # Create a sample audio file using SimpleUploadedFile
        audio_file = SimpleUploadedFile("sample_audio.mp3", b"file_content")

        # Send a POST request to your upload view with the audio file
        response = self.client.post('/upload/', {'file': audio_file}, follow=True)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upload successful')
