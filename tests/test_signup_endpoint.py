from http import HTTPStatus
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.main import app


class TestName:
    def test_should_successfully_call_signup_endpoint(self):  # noqa: PLR6301
        client = TestClient(app)
        response = client.post(
            '/signup',
            json={
                'first_name': 'John',
                'last_name': 'Doe',
                'name': 'John Doe',
                'email': f'john.{uuid4()}@example.com',
            },
        )
        assert response.status_code == HTTPStatus.CREATED
        assert response.json().get('account_id') is not None
        # assert response.json() == {'account_id': '123456789'}
