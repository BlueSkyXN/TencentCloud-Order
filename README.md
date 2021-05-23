# TencentCloud-Renew

腾讯云产品-自定义续费一键单页，免额外抓包，直接输入参数提交自动跳转对应订单页面

## 网址
记得先登陆好腾讯云：https://console.cloud.tencent.com

入口：https://tencentcloud-renew.pages.dev

# WARNING

仅供研究学习HTML基本语法和HTTP-POST的使用，请勿用于非法用途或对腾讯云等公司造成损失

如果您打开了相关页面，则默认您仅学习HTML基本语法和HTTP-POST的使用，且所造成的后果由您自负，与本开发者无关

同时，无论何种目的，请在12小时内停止浏览/使用/保存相关内容


# 参数参考

自己修改实例名，购买时长等，下方参数和我博客的抓包所抓到的参数一致

不过这个pid，不知道有没有影响，目前怀疑是产品ID，而新加坡24是1002660是确定的，我抓包来的

其他香港啊什么的就不清楚了，可能需要再抓，pid不对也不清楚有没有影响

如果你有兴趣抓包的，可以抓一下丢issues

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
                "resourceId": "【lhins-xxxxxx这种格式的，是你的实例名，请修改】",
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
