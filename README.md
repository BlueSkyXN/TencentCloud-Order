# TencentCloud-Order

腾讯云产品-自定义参数购买一键单页，免额外抓包，直接输入参数提交自动跳转对应订单页面

基于轻量服务器续费做演示 新购参数经过测试发现逻辑不一样，改不了

## 网址
记得先登陆好腾讯云：https://console.cloud.tencent.com

单页入口：https://tencentcloud.pages.dev

# WARNING

仅供研究学习HTML基本语法和HTTP-POST的使用，请勿用于非法用途或对腾讯云等公司造成损失

如果您打开了相关页面，则默认您仅学习HTML基本语法和HTTP-POST的使用，且所造成的后果由您自负，与本开发者无关

同时，无论何种目的，请在12小时内停止浏览/使用/保存相关内容

# 参数参考

自己修改实例名，购买时长等，下方参数和我博客的抓包所抓到的参数一致

如果你有兴趣抓包的，可以抓一下丢issues

<details><summary>续费参考</summary>
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
                "resourceId": "【lhins-xxxxxx这种格式的，是你的实例名，请修改，新购请移除此行】",
                "autoRenewFlag": 0,
                "timeUnit": "d",
                "timeSpan": 12
            }
        }
    ]
}
</pre>
</details>

# 参数说明

## regionId 

请阅读 https://www.blueskyxn.com/202007/1541.html 可以查到

新加坡9香港5，其他去上面查

## pid

产品类型，和地域无关

境外轻量24都是“1002660”

## resourceId

实例名，lhins-xxxxxx这种格式的

## timeSpan
时间数量 正整数

## timeUnit
时间单位 d/m等


## Productinfo 

在你的订单付款前的确认页，有产品信息，请复制输入

<details><summary>产品信息</summary>
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
</pre></details>
