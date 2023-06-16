# -*- coding: utf-8 -*-
from app.plugin.ecs import EcsPlugin
from tests.common import BaseTest


class TestEcsPlugin(BaseTest):

    def setup_method(self) -> None:
        super(TestEcsPlugin, self).setup_method()
        self.plugin = EcsPlugin(region_id=self.REGION_ID)

    async def test_get_sg(self):
        result = await self.plugin.get_security_group()
        self._pprint_json(result)
