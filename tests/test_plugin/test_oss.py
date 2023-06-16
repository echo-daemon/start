from app.plugin.oss import OssPlugin
from tests.common import BaseTest


class TestOssPlugin(BaseTest):

    def setup_method(self) -> None:
        super(TestOssPlugin, self).setup_method()
        self.plugin = OssPlugin(region_id=self.REGION_ID, bucket_name='iact3-beijing')

    def test_exist(self):
        self.plugin.object_exists('')

