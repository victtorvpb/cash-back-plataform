import requests

import mock

from fastapi import status

from commons.services.purchase import get_credit_value
from tests.utils.utils import mock_response


@mock.patch('commons.services.purchase.requests.get')
def test_get_credit_value_generic_error(mock_requests):
    mock_requests.side_effect = Exception
    credit = get_credit_value('000')
    assert not credit


@mock.patch('commons.services.purchase.requests.get')
def test_get_credit_value_http_error(mock_requests):
    mock_requests.return_value = mock_response(
        status=status.HTTP_400_BAD_REQUEST, raise_for_status=requests.HTTPError
    )
    credit = get_credit_value('000')
    assert not credit


@mock.patch('commons.services.purchase.requests.get')
def test_get_credit_value_connection_error(mock_requests):
    mock_requests.return_value = mock_response(
        status=status.HTTP_400_BAD_REQUEST, raise_for_status=requests.ConnectionError
    )
    credit = get_credit_value('000')
    assert not credit


def test_get_credit_value_success():
    credit = get_credit_value('000')
    assert credit.credit
