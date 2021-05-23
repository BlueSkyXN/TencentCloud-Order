# TencentCloud-Renew
腾讯云产品-自定义续费模板

# 参数参考

自己修改实例名，购买时长等，下方参数和我博客的抓包所抓到的参数一致

<pre>
{
    "raw_goodsData": [
        {
            "goodsCategoryId": 101594,
            "goodsNum": 1,
            "payMode": 1,
            "regionId": 9,
            "goodsDetail": {
                "productCode": "p_lighthouse",
                "subProductCode": "sp_lighthouse_bundle_linux_sml1_1t",
                "pid": 1002660,
                "sv_lighthouse_compute_linux_sml1_1t": 1,
                "sv_lighthouse_rootdisk_cbsssd_linux_sml1_1t": 1,
                "sv_lighthouse_trafficpkg_linux_sml1_1t": 1,
                "productInfo": [
                    {
                        "name": "运算组件",
                        "value": "1核CPU、1GB内存 (Linux/Unix SMALL1 | 1T)"
                    },
                    {
                        "name": "云SSD系统盘",
                        "value": "25GB SSD (Linux/Unix SMALL1 | 1T)"
                    },
                    {
                        "name": "流量包",
                        "value": "1024GB (Linux/Unix SMALL1 | 1T)"
                    },
                    {
                        "name": "地域",
                        "value": "新加坡"
                    }
                ],
                "resourceId": "lh什么的东西，是你的实例名，请修改",
                "autoRenewFlag": 0,
                "timeUnit": "d",
                "timeSpan": 12
            }
        }
    ]
}
</pre>
