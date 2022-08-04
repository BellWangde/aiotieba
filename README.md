<div align="center">

![Tieba-Manager](https://socialify.git.ci/Starry-OvO/Tieba-Manager/image?font=Bitter&forks=1&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F48282276&name=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Dark)

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Starry-OvO/Tieba-Manager/CI?label=CI&logo=github)](https://github.com/Starry-OvO/Tieba-Manager/actions)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Starry-OvO/Tieba-Manager?logo=lgtm)](https://lgtm.com/projects/g/Starry-OvO/Tieba-Manager/context:python)
[![Code style: black](https://img.shields.io/badge/code_style-black-000000)](https://github.com/psf/black)

</div>

## 简介

`aiotieba`库是一个使用[`asyncio`](https://docs.python.org/zh-cn/3/library/asyncio.html)+[`aiohttp`](https://github.com/aio-libs/aiohttp)实现的**贴吧客户端**

<details>

<summary>封装的贴吧接口列表</summary>

> 按**回复时间**/**发布时间**/**热门序**获取贴吧**主题帖**/**精华帖列表**。支持获取带**转发**/**投票**/**转发嵌套投票**/**各种卡片**的主题帖信息
> 
> 获取带**图片链接**/**小尾巴内容**/**点赞情况**/**用户信息**（[**用户名**](docs/tutorial.md#user_name)/[**portrait**](docs/tutorial.md#portrait)/[**user_id**](docs/tutorial.md#user_id)/**等级**/**性别**/**是否锁回复**）/每条回复的**前排楼中楼**（支持按或不按点赞数排序）的**楼层列表**
> 
> 获取带所有前述用户信息的**楼中楼列表**
> 
> 根据[**用户名**](docs/tutorial.md#user_name)/[**portrait**](docs/tutorial.md#portrait)/[**user_id**](docs/tutorial.md#user_id)中的任一项反查其他用户信息，或通过用户主页的[**tieba_uid**](docs/tutorial.md#tieba_uid)反查其他用户信息
> 
> 使用小吧主、语音小编的账号**删帖**/**屏蔽**/**封禁任意用户3天或10天**
> 
> 使用已被大吧主分配解封/恢复/处理申诉权限的吧务账号**解封**/**恢复**/**处理申诉**
> 
> 使用大吧主账号**推荐帖子到首页**/**移动帖子到指定分区**/**加精**/**撤精**/**置顶**/**撤置顶**/**添加黑名单**/**查看黑名单**/**取消黑名单**
> 
> 获取其他用户的**主页信息**/**关注贴吧列表**/**关注用户列表**/**粉丝列表**/**发布的主题帖列表**
> 
> 使用当前账号**关注贴吧**/**取关贴吧**/**关注用户**/**取关用户**/**移除粉丝**/**获取屏蔽贴吧列表**/**屏蔽贴吧**/**取消屏蔽贴吧**/**签到**/**水帖**/**发送私信**/**获取回复历史**
> 
> 获取一个贴吧的**最新关注用户列表**/**等级排行榜**/**吧务列表**/**吧详情**

</details>

<details>

<summary>附加功能列表</summary>

> 数据库功能：**缓存贴吧常量**（如贴吧名到fid的映射关系）/**为用户添加标记**/**为帖子或回复添加标记**/**为图像hash添加标记**
> 
> 图像处理功能：**图像解码**/**二维码解析**/**图像hash计算**

</details>

## 安装并使用

+ 确保你的[`Python`](https://www.python.org/downloads/)版本在`3.9`及以上

+ 拉取代码

```bash
git clone https://github.com/Starry-OvO/Tieba-Manager.git
```

+ 安装依赖项

```bash
cd ./Tieba-Manager
pip install -r requirements.txt
```

+ 体验一下

```python
import asyncio

import aiotieba


async def main():
    async with aiotieba.Client() as client:
        print(await client.get_threads("图拉丁"))


asyncio.run(main())
```

+ 继续阅读[入门教程](docs/tutorial.md)

## 客户名单

2022.08.04更新

|      吧名      | 关注用户数 | 最近29天日均访问量 | 日均主题帖数 | 日均回复数 |
| :------------: | :--------: | :----------------: | :----------: | :--------: |
|    抗压背锅    | 3,862,277  |     1,168,254      |    2,808     |   85,194   |
|     孙笑川     | 2,202,422  |      673,914       |    8,015     |  196,532   |
|    lol半价     | 1,955,172  |      136,948       |     464      |   8,378    |
|      宫漫      | 1,301,435  |       50,377       |     254      |   3,667    |
|    新孙笑川    |  276,314   |       47,760       |     452      |   16,252   |
|     vtuber     |  210,966   |       22,105       |     165      |   1,681    |
|     asoul      |  158,845   |       29,430       |     312      |   2,142    |
|      嘉然      |   55,704   |       20,728       |     140      |   2,059    |
|      向晚      |   28,595   |       17,074       |     158      |   2,237    |
|      贝拉      |   21,554   |       13,603       |      77      |   1,476    |
|      乃琳      |   16,882   |       6,002        |      42      |    557     |
| vtuber自由讨论 |   16,604   |       3,749        |      4       |     74     |
| asoul一个魂儿  |   14,837   |       1,449        |      11      |    136     |
|     贝贝珈     |   1,658    |       1,242        |      3       |     41     |

## 友情链接

+ [另一个仍在活跃更新的贴吧管理器（有用户界面）](https://github.com/dog194/TiebaManager)
+ [用户反馈（我的个人吧）](https://tieba.baidu.com/starry)
