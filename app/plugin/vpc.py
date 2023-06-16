# -*- coding: utf-8 -*-
from app.plugin.base_plugin import TeaSDKPlugin


class VpcBasePlugin(TeaSDKPlugin):

    product = 'VPC'

    def module_name(self):
        return 'alibabacloud_vpc20160428'


class VpcPlugin(VpcBasePlugin):

    async def get_one_vpc(self, vpc_id: str = None):
        kwargs = dict(VpcId=vpc_id, PageSize=50)
        response = await self.send_request('DescribeVpcsRequest', **kwargs)
        vpcs = response['Vpcs']['Vpc']
        for vpc in vpcs:
            if vpc['VSwitchIds']['VSwitchId']:
                return vpc

    async def get_one_vswitch(self, vpc_id: str = None, vsw_id: str = None, zone_id: str = None):
        kwargs = dict(VpcId=vpc_id, VSwitchId=vsw_id, ZoneId=zone_id)
        response = await self.send_request('DescribeVSwitchesRequest', **kwargs)
        vsws = response['VSwitches']['VSwitch']
        for vsw in vsws:
            if vsw['AvailableIpAddressCount'] > 1:
                return vsw
