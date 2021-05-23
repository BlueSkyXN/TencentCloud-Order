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
                "resourceId": "【lhins-9w4aepmp这种格式的，是你的实例名，请修改】",
                "autoRenewFlag": 0,
                "timeUnit": "d",
                "timeSpan": 12
            }
        }
    ]
}
</pre>


## Productinfo 

在你的订单付款前的确认页，有产品信息，请复制输入

<pre>
商品清单
轻量应用服务器-标准型续费
10.40元
运算组件：
1核CPU、1GB内存 (Linux/Unix SMALL1 | 1T)
云SSD系统盘：
25GB SSD (Linux/Unix SMALL1 | 1T)
流量包：
1024GB (Linux/Unix SMALL1 | 1T)
地域：
新加坡
单价：
0.80元/天
数量：
1
付费方式：
预付费
购买时长：
13天
</pre>
