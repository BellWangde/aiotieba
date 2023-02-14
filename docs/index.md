# 

<p align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/48282276/217530379-1348f7c5-7056-48f4-8c64-1c74caf5497c.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/48282276/217530385-98a2fb24-ff6e-4b27-990f-998b66c2ab5e.svg">
  <img src="https://user-images.githubusercontent.com/48282276/217530385-98a2fb24-ff6e-4b27-990f-998b66c2ab5e.svg">
</picture>
</p>

<p align="center">
<a href="https://github.com/Starry-OvO/aiotieba/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/Starry-OvO/aiotieba/CI.yml?branch=develop&label=CI&logo=github&style=flat-square" alt="GitHub Workflow Status">
</a>
<a href="https://pypi.org/project/aiotieba">
    <img src="https://img.shields.io/pypi/v/aiotieba?color=g&style=flat-square" alt="PyPI - Version">
</a>
<a href="https://pypi.org/project/aiotieba">
    <img src="https://img.shields.io/pypi/pyversions/aiotieba?style=flat-square" alt="PyPI - Python Version">
</a>
</p>

---

## 安装

```shell
pip install aiotieba
```

## 尝试一下

```python
import asyncio

import aiotieba


async def main():
    async with aiotieba.Client() as client:
        threads = await client.get_threads("天堂鸡汤")
        print(threads[3:6])


asyncio.run(main())
```

*输出样例*

```log
[{'tid': 8090519523, 'pid': 145826926675, 'user': '熙时T', 'text': '记录下我的生活吧\n远渡重洋来到这，一周课不算多，20个小时课时，加上每天自学时间，差不多40个小时。9点到17点，一周四天。今天是周五，去了趟镇上买了一周的食物，平时上课，早上就吃点面包和牛奶，中餐是14点溜出来吃个3.99磅的meal deal（挺丰富的，一个大的三明治，一瓶饮料，一份小吃）晚上不想做就吃个巧克力喝点牛奶。周末就会自己做点火锅或者焖锅改善一下生活。这个周末本来想去利物浦和曼城，但下周二有个debate，周末还有个essay和journal，虽然比较简单，还是想认真对待。班上只有两个国人，室友都是当地人，对我很好，没有歧视啥的。'}, {'tid': 8256346027, 'pid': 146825511891, 'user': '煞南波万', 'text': '如题，好奇大家会存什么样的图图✧◔.̮◔'}, {'tid':: 8255392021, 'pid': 146820360992, 'user': 'Yfy1357oy', 'text': '有没有一些治愈的音乐推荐呢？\n如题，范围很广阔，鼓舞人心的、轻快的、浪漫的，有词的、无词的，中文的、外文的，都可以。希望大家能从音乐中找到生活的力量'}]
```

继续阅读[**入门教程**](https://aiotieba.cc/tutorial/start)

## 项目特色

+ 收录[**72个常用API**](https://github.com/Starry-OvO/aiotieba/tree/develop/aiotieba/client)
+ 类型注解全覆盖，方法注释全覆盖，类属性注释全覆盖，内部命名统一
+ 请求参数支持protobuf序列化
+ 支持websocket接口
+ 高一致性的密码学实现