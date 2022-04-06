import pytest
from test_one import app


class TestOneTest:

    @pytest.fixture()
    def app(self):
        app.config.update({
            "TESTING": True,
        })

        yield app

    @pytest.fixture()
    def client(self, app):
        return app.test_client()

    def test_should_return_min_numbers_by_quantifier(self, client):
        response = client.get(
            '/min', query_string={'numbers': [7, 34, 98, 1, 45, 18, 63, 15], 'quantifier': 3})
        assert response.status_code == 200
        assert response.json['data'] == [1, 7, 15]

    def test_should_return_max_numbers_by_quantifier(self, client):
        response = client.get(
            '/max', query_string={'numbers': [7, 34, 98, 1, 45, 18, 63, 15], 'quantifier': 3})
        assert response.status_code == 200
        assert response.json['data'] == [98, 63, 45]

    def test_should_return_avg_of_numbers(self, client):
        response = client.get(
            '/avg', query_string={'numbers': [7, 34, 98, 1, 45, 18, 63, 15]})
        assert response.status_code == 200
        assert response.json['data'] == 35.125

    def test_should_return_median_of_numbers(self, client):
        response = client.get(
            '/median', query_string={'numbers': [7, 34, 98, 1, 45, 18, 63, 15]})
        assert response.status_code == 200
        assert response.json['data'] == 26.0

    def test_should_return_percentile_of_numbers(self, client):
        response = client.get(
            '/percentile', query_string={'numbers': [7, 34, 98, 1, 45, 18, 63, 15], 'quantifier': 3})
        assert response.status_code == 200
        assert response.json['data'] == 2.26
