import pytest
from test_two import app, get_ok_file_path
import os


class TestTwoTest:

    @pytest.fixture()
    def app(self):
        app.config.update({
            "TESTING": True,
        })

        yield app

    @pytest.fixture()
    def client(self, app):
        return app.test_client()

    @pytest.fixture()
    def tmp_ok_file(self):
        ok_file_path = get_ok_file_path()
        with open(ok_file_path, 'w') as ok_file:
            ok_file.write('ok')
        yield
        os.remove(ok_file_path)

    def test_should_return_ok_message_if_file_exists_on_ping(self, client, tmp_ok_file):
        response = client.get('/ping')
        assert response.status_code == 200
        assert response.json['message'] == 'OK'

    def test_should_return_503_if_file_not_exists_on_ping(self, client):
        response = client.get('/ping')
        assert response.status_code == 503

    def test_should_return_200_when_reading_gif_file(self, client):
        response = client.get('/img')
        assert response.status_code == 200
