import json
import pytest

from app.logger import init_cli_logger


@pytest.mark.asyncio
class BaseTest:
    REGION_ID = 'cn-shanghai'

    def setup_method(self) -> None:
        pass
        # init_cli_logger(loglevel='Debug')

    @staticmethod
    def _pprint_json(data, ensure_ascii=False):
        print('\n')
        print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '),
                         ensure_ascii=ensure_ascii))
