from app.plugin.vpc import VpcPlugin
from tests.common import BaseTest


class TestVpcPlugin(BaseTest):

    def setup_method(self) -> None:
        super(TestVpcPlugin, self).setup_method()
        self.plugin = VpcPlugin(region_id=self.REGION_ID)

    async def test_get_vpc(self):
        vpcs = await self.plugin.get_one_vpc()
        self._pprint_json(vpcs)

    async def test_get_vsw(self):
        vsw = await self.plugin.get_one_vswitch(vpc_id='vpc-mock')
        self._pprint_json(vsw)
