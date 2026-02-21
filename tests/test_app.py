from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app


class TestName:
    def test_should_successfully_call_root_endpoint(self):
        client = TestClient(app)
        response = client.get('/')
        assert response.status_code == HTTPStatus.OK
        assert response.json() == {'message': 'Hello, World!'}
