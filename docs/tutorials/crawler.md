# 爬虫教程

***请认真阅读代码注释***

## 入门案例

*本案例将演示 如何实现一个简单并发爬虫*

复制下列代码并运行

```python
import asyncio

import aiotieba as tb


async def main():
    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client("default") as client:
        # 下面这行语句会同时请求用户个人信息和图拉丁吧首页前30帖
        # 你可以将若干协程作为参数传入asyncio.gather，这里传入的参数为client.get_self_info()和client.get_threads('图拉丁')
        # asyncio.gather会为每个传入的协程创建对应的任务来同时执行它们（并发）
        # 同时asyncio.gather(...)也会返回一个协程，在前面添加await等待其执行完毕
        # 执行完毕后，返回数据的顺序与传入参数的顺序一致，即user对应client.get_self_info()，threads对应client.get_threads('图拉丁')
        # 参考官方文档：并发运行任务
        # https://docs.python.org/zh-cn/3/library/asyncio-task.html#running-tasks-concurrently
        user, threads = await asyncio.gather(client.get_self_info(), client.get_threads('图拉丁'))

    # 将获取的信息打印到日志
    tb.LOG.info(f"当前用户信息: {user}")
    for thread in threads:
        # threads支持迭代，因此可以使用for循环逐条打印主题帖信息
        tb.LOG.info(f"tid: {thread.tid} 最后回复时间戳: {thread.last_time} 标题: {thread.title}")


# 使用asyncio.run执行协程main
asyncio.run(main())
```

运行效果如下所示

```log
<2022-07-16 20:56:47.006> [INFO] [main] 当前用户信息: {'user_id': 957339815, 'user_name': 'kk不好玩', 'portrait': 'tb.1.8277e641.gUE2cTq4A4z5fi2EHn5k3Q'}
<2022-07-16 20:56:47.006> [INFO] [main] tid: 7924884407 最后回复时间戳: 1657877692 标题: 分享贴子
<2022-07-16 20:56:47.016> [INFO] [main] tid: 2949701560 最后回复时间戳: 1655038527 标题: 【重要更新】百度图拉丁吧吧规 20140329
<2022-07-16 20:56:47.017> [INFO] [main] tid: 7896485738 最后回复时间戳: 1657976199 标题: 装机其他配件陆陆续续都买齐了，就差显示器了。
<2022-07-16 20:56:47.017> [INFO] [main] tid: 7926932272 最后回复时间戳: 1657976200 标题: 散人求问！就这，10块钱买到的！
<2022-07-16 20:56:47.018> [INFO] [main] tid: 7926963000 最后回复时间戳: 1657976195 标题: 有人福利价两条DDR38G内存条吗
<2022-07-16 20:56:47.018> [INFO] [main] tid: 7926025065 最后回复时间戳: 1657976194 标题: 果真电脑店都是奸商
<2022-07-16 20:56:47.019> [INFO] [main] tid: 7926209178 最后回复时间戳: 1657976191 标题: 怎么能阻止我爸玩我电脑
<2022-07-16 20:56:47.019> [INFO] [main] tid: 7926950537 最后回复时间戳: 1657976189 标题: 带佬们，擦了擦cpu，结果点不亮了。结果发现主板cpu卡槽
<2022-07-16 20:56:47.020> [INFO] [main] tid: 7926605589 最后回复时间戳: 1657976185 标题: 咸鱼到手刀真恶心
<2022-07-16 20:56:47.020> [INFO] [main] tid: 7926961253 最后回复时间戳: 1657976186 标题: 牛爷爷们，预算5-6k求个单子
<2022-07-16 20:56:47.021> [INFO] [main] tid: 7925878206 最后回复时间戳: 1657976184 标题: 这个配置怎么样？
<2022-07-16 20:56:47.022> [INFO] [main] tid: 7925341844 最后回复时间戳: 1657976180 标题: 这么高的配置打lol开团卡成幻灯片
<2022-07-16 20:56:47.022> [INFO] [main] tid: 7926838704 最后回复时间戳: 1657976180 标题: 完蛋了，换了主板，不会插线了，救命！
<2022-07-16 20:56:47.023> [INFO] [main] tid: 7926597738 最后回复时间戳: 1657976180 标题: 淘宝翻车我转手就上拼多多
<2022-07-16 20:56:47.023> [INFO] [main] tid: 7926952718 最后回复时间戳: 1657976175 标题: 兄弟们，这个电脑我要是入手什么价格合适
<2022-07-16 20:56:47.024> [INFO] [main] tid: 7926078320 最后回复时间戳: 1657976174 标题: 3050真的是垃圾卡吗🤔
<2022-07-16 20:56:47.025> [INFO] [main] tid: 7926962437 最后回复时间戳: 1657976170 标题:
<2022-07-16 20:56:47.025> [INFO] [main] tid: 7925259456 最后回复时间戳: 1657976170 标题: 求大佬看看可不可入🥰pdd上的整机为 啥这么便宜？
<2022-07-16 20:56:47.026> [INFO] [main] tid: 7926937893 最后回复时间戳: 1657976169 标题: 第一次买电脑，是买零件自己装还是买品牌机
<2022-07-16 20:56:47.027> [INFO] [main] tid: 7926958973 最后回复时间戳: 1657976205 标题:
<2022-07-16 20:56:47.027> [INFO] [main] tid: 7926962111 最后回复时间戳: 1657976156 标题: 有人买联想拯救者刃这款主机的么？质量咋样？求告知
<2022-07-16 20:56:47.028> [INFO] [main] tid: 7926477067 最后回复时间戳: 1657976152 标题: 这个信息是真的假的呀
<2022-07-16 20:56:47.029> [INFO] [main] tid: 7577926810 最后回复时间戳: 1657976151 标题: 显示屏一半暗一半亮怎么办
<2022-07-16 20:56:47.029> [INFO] [main] tid: 7926744414 最后回复时间戳: 1657976151 标题: 大佬们  这套配置加显示器卖我  2300亏吗？卖家说一年期配的
<2022-07-16 20:56:47.030> [INFO] [main] tid: 7926961884 最后回复时间戳: 1657976146 标题: 电脑视频线插独立显卡，显示检测不到信号线，插集成显卡屏幕黑屏！
<2022-07-16 20:56:47.031> [INFO] [main] tid: 7923574035 最后回复时间戳: 1657976143 标题: 卡诺基yyds
<2022-07-16 20:56:47.031> [INFO] [main] tid: 7925270056 最后回复时间戳: 1657976140 标题: 老哥们问个问题
<2022-07-16 20:56:47.032> [INFO] [main] tid: 7926056349 最后回复时间戳: 1657976140 标题: 新手第一次装机
<2022-07-16 20:56:47.033> [INFO] [main] tid: 7926912956 最后回复时间戳: 1657976137 标题: 8u们，这个配置最高能玩什么游戏。
<2022-07-16 20:56:47.034> [INFO] [main] tid: 7925518317 最后回复时间戳: 1657976132 标题: 救救孩子吧
```

## 进阶案例

*本案例将演示 如何通过任务队列实现一个多协程爬虫*

复制下列代码并运行

```python
import asyncio
import time
from typing import List

import aiotieba as tb


async def crawler(fname: str):
    """
    获取贴吧名为fname的贴吧的前32页中浏览量最高的10个主题帖

    Args:
        fname (str): 贴吧名
    """

    start_time = time.perf_counter()
    tb.LOG.info("Spider start")

    # thread_list用来保存主题帖列表
    thread_list: List[tb.Thread] = []

    # 使用键名"default"对应的BDUSS创建客户端
    async with tb.Client("default") as client:

        # asyncio.Queue是一个任务队列
        # maxsize=8意味着缓冲区长度为8
        # 当缓冲区被填满时，调用Queue.put的协程会被阻塞
        task_queue = asyncio.Queue(maxsize=8)
        # 当is_running被设为False后，消费者会在超时后退出
        is_running = True

        async def producer():
            """
            生产者协程
            """

            for pn in range(32, 0, -1):
                # 生产者使用Queue.put不断地将页码pn填入任务队列task_queue
                await task_queue.put(pn)
            # 这里需要nonlocal来允许对闭包外的变量的修改操作（类似于引用传递和值传递的区别）
            nonlocal is_running
            # 将is_running设置为False以允许各消费协程超时退出
            is_running = False

        async def worker(i: int):
            """
            消费者协程

            Args:
                i (int): 协程编号
            """

            while 1:
                try:
                    # 消费者协程不断地使用Queue.get从task_queue中拉取由生产者协程提供的页码pn作为任务
                    # asyncio.wait_for用于等待一个协程执行完毕直到超时
                    # timeout=1即把超时时间设为1秒
                    # 如果超过1秒未获取到新的页码pn，asyncio.wait_for将抛出asyncio.TimeoutError
                    pn = await asyncio.wait_for(task_queue.get(), timeout=1)
                    tb.LOG.debug(f"Worker#{i} handling pn:{pn}")
                except asyncio.TimeoutError:
                    # 捕获asyncio.TimeoutError以退出协程
                    if is_running is False:
                        # 如果is_running为False，意味着不需要再轮询task_queue获取新任务
                        tb.LOG.debug(f"Worker#{i} quit")
                        # 消费者协程通过return退出
                        return
                else:
                    # 执行被分派的任务，即爬取pn页的帖子列表
                    threads = await client.get_threads(fname, pn)
                    # 这里的nonlocal同样是为了修改闭包外的变量thread_list
                    nonlocal thread_list
                    thread_list += threads

        # 创建8个消费者协程
        workers = [worker(i) for i in range(8)]
        # 使用asyncio.gather并发执行
        # 需要注意这里*workers中的*意为将列表展开成多个参数
        # 因为asyncio.gather只接受协程作为参数，不接受协程列表
        await asyncio.gather(*workers, producer())

    tb.LOG.info(f"Spider complete. Time cost: {time.perf_counter()-start_time:.4f} secs")

    # 按主题帖浏览量降序排序
    thread_list.sort(key=lambda thread: thread.view_num, reverse=True)
    # 将浏览量最高的10个主题帖的信息打印到日志
    for i, thread in enumerate(thread_list[0:10], 1):
        tb.LOG.info(f"Rank#{i} view_num:{thread.view_num} title:{thread.title}")


# 执行协程crawler
asyncio.run(crawler("图拉丁"))
```

运行效果如下图所示

```log
<2022-07-16 20:57:29.227> [INFO] [crawler] Spider start
<2022-07-16 20:57:29.230> [DEBUG] [worker] Worker#0 handling pn:32
<2022-07-16 20:57:29.231> [DEBUG] [worker] Worker#1 handling pn:31
<2022-07-16 20:57:29.232> [DEBUG] [worker] Worker#2 handling pn:30
<2022-07-16 20:57:29.233> [DEBUG] [worker] Worker#3 handling pn:29
<2022-07-16 20:57:29.234> [DEBUG] [worker] Worker#4 handling pn:28
<2022-07-16 20:57:29.235> [DEBUG] [worker] Worker#5 handling pn:27
<2022-07-16 20:57:29.236> [DEBUG] [worker] Worker#6 handling pn:26
<2022-07-16 20:57:29.237> [DEBUG] [worker] Worker#7 handling pn:25
<2022-07-16 20:57:29.878> [DEBUG] [worker] Worker#4 handling pn:24
<2022-07-16 20:57:29.930> [DEBUG] [worker] Worker#3 handling pn:23
<2022-07-16 20:57:29.954> [DEBUG] [worker] Worker#2 handling pn:22
<2022-07-16 20:57:29.969> [DEBUG] [worker] Worker#7 handling pn:21
<2022-07-16 20:57:29.992> [DEBUG] [worker] Worker#1 handling pn:20
<2022-07-16 20:57:30.131> [DEBUG] [worker] Worker#6 handling pn:19
<2022-07-16 20:57:30.140> [DEBUG] [worker] Worker#5 handling pn:18
<2022-07-16 20:57:30.219> [DEBUG] [worker] Worker#0 handling pn:17
<2022-07-16 20:57:30.469> [DEBUG] [worker] Worker#3 handling pn:16
<2022-07-16 20:57:30.505> [DEBUG] [worker] Worker#1 handling pn:15
<2022-07-16 20:57:30.525> [DEBUG] [worker] Worker#4 handling pn:14
<2022-07-16 20:57:30.539> [DEBUG] [worker] Worker#2 handling pn:13
<2022-07-16 20:57:30.660> [DEBUG] [worker] Worker#6 handling pn:12
<2022-07-16 20:57:30.692> [DEBUG] [worker] Worker#0 handling pn:11
<2022-07-16 20:57:30.883> [DEBUG] [worker] Worker#5 handling pn:10
<2022-07-16 20:57:31.001> [DEBUG] [worker] Worker#1 handling pn:9
<2022-07-16 20:57:31.020> [DEBUG] [worker] Worker#3 handling pn:8
<2022-07-16 20:57:31.054> [DEBUG] [worker] Worker#4 handling pn:7
<2022-07-16 20:57:31.071> [DEBUG] [worker] Worker#7 handling pn:6
<2022-07-16 20:57:31.084> [DEBUG] [worker] Worker#2 handling pn:5
<2022-07-16 20:57:31.154> [DEBUG] [worker] Worker#0 handling pn:4
<2022-07-16 20:57:31.235> [DEBUG] [worker] Worker#6 handling pn:3
<2022-07-16 20:57:31.583> [DEBUG] [worker] Worker#5 handling pn:2
<2022-07-16 20:57:31.617> [DEBUG] [worker] Worker#4 handling pn:1
<2022-07-16 20:57:32.630> [DEBUG] [worker] Worker#2 quit
<2022-07-16 20:57:32.677> [DEBUG] [worker] Worker#7 quit
<2022-07-16 20:57:32.769> [DEBUG] [worker] Worker#0 quit
<2022-07-16 20:57:32.769> [DEBUG] [worker] Worker#1 quit
<2022-07-16 20:57:32.912> [DEBUG] [worker] Worker#3 quit
<2022-07-16 20:57:33.003> [DEBUG] [worker] Worker#6 quit
<2022-07-16 20:57:33.147> [DEBUG] [worker] Worker#5 quit
<2022-07-16 20:57:33.267> [DEBUG] [worker] Worker#4 quit
<2022-07-16 20:57:33.270> [INFO] [crawler] Spider complete. Time cost: 4.0417 secs
<2022-07-16 20:57:33.271> [INFO] [crawler] Rank#1 view_num:2527890 title:我真的想踹网线师傅
<2022-07-16 20:57:33.272> [INFO] [crawler] Rank#2 view_num:1677425 title:【重要更新】百度图拉丁吧吧规 20140329
<2022-07-16 20:57:33.272> [INFO] [crawler] Rank#3 view_num:649518 title:大佬们，这是真的吗？
<2022-07-16 20:57:33.273> [INFO] [crawler] Rank#4 view_num:363866 title:【圾佬乐园】图吧垃圾回收站(2021年冬季)
<2022-07-16 20:57:33.274> [INFO] [crawler] Rank#5 view_num:309239 title:第一次捡漏成功，拿着卡我就跑了
<2022-07-16 20:57:33.274> [INFO] [crawler] Rank#6 view_num:127988 title:刚签收的包装都没拆放衣服里直接洗了**
<2022-07-16 20:57:33.275> [INFO] [crawler] Rank#7 view_num:108095 title:pdd大事件 兄弟们加把劲
<2022-07-16 20:57:33.275> [INFO] [crawler] Rank#8 view_num:107064 title:一个同学帮我配的 要不要请他吃饭
<2022-07-16 20:57:33.276> [INFO] [crawler] Rank#9 view_num:91084 title:防坑指南之RX580
<2022-07-16 20:57:33.276> [INFO] [crawler] Rank#10 view_num:84287 title:350买的1660到啦
```

## 结语

使用异步请求相当于用更高的调度成本换取更高的并行度，提高请求频率，以充分利用服务端资源

在异步IO下，脚本的效率瓶颈大多来自于服务端的 rps (Request per Second) 限制
