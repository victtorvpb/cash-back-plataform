import logging
import requests

from typing import Any

from pydantic import ValidationError

from commons.schemas import PurchaseCreditRequest
from commons.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_credit_value(cpf: str) -> Any:
    extra = {"cpf": cpf}
    logger.info('get_credit_value: Get credit value', extra=extra)
    heardes = {"token": settings.CREDIT_SERVICE_TOKEN}

    cpf = cpf.replace('.', '').replace('-', '')
    url = f'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={cpf}'

    try:
        response = requests.get(url=url, headers=heardes)
        response.raise_for_status()

        response.json()
        try:
            response_data = PurchaseCreditRequest.parse_obj(response.json())
            if response_data.statusCode != 200:
                extra['status_code'] = response_data.statusCode
                logger.exception(
                    'get_credit_value: Service credit cashback return status code error ',
                    extra=extra,
                )
                return False

            return response_data.body

        except ValidationError:
            pass

    except requests.HTTPError:
        extra['status_code'] = response.status_code
        logger.exception(
            'get_credit_value: Service credit cashback return status code error ', extra=extra
        )
    except requests.ConnectionError:
        logger.exception(
            'get_credit_value: Connection error in request service credit cashback', extra=extra
        )
    except Exception:
        logger.exception('get_credit_value: Generic error', extra=extra)

    return False
