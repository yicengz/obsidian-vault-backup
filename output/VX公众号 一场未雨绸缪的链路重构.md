---
title: 【数仓工作分享】一场未雨绸缪的链路重构
description:
tags:
is_diary: false
is_essay: false
is_wx_article: true
is_yiceng_public: true
link: https://mp.weixin.qq.com/s/qWlEviAzrnxeL8qxKRrdYg
---
> 你想要生活的那一刻，生命的火花就已经点亮了
> 
> —— 电影《心灵奇旅》

## 一、凌晨告警与链路重构

---

  

端午假期前最后一个工作日，凌晨，我被值班伙伴的加急电话叫醒 —— 核心链路的核心表执行失败了。

报错卡在执行的最后一步，错误信息我也从没见过。我醒来之前，大家已经慌了一阵，很可能要大面积破线。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/37X2DwwWHLjRXtnrSXRaZPGaVES1X7NWIia7OW7GbmWgwAzp8Mg7XP0ycUSNCYHia8b8ichl2TCukib9GuAicgaRbMQf90mnMN2B9CeOibafwz8Yg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

Matt Hearne | from unsplash

但我其实不太慌，甚至有点窃喜。

今年初我刚转到这个方向，Q1 就发现了这条链路的隐患：单任务 shuffle 多、数据量大，执行时间从早期的 1 小时涨到了 2.5 小时，下游的启动也跟着越拖越晚。所以整个 Q2 需求再紧，我也每周挤一点时间做这条链路的重构，上周刚做完新老链路的数据比对。

所以告警响起来时，我第一反应甚至有点“阴暗”：终于有这么一件事，能证明我当初决定重构是对的 —— **我太聪明了🐶**。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/37X2DwwWHLg9NwmAicjaFkBjmer78UTMfibAdeicB89GQufuXsmic7omUWNlj7dwGKD0LWFALbEq2fRWAWvc5gibVfd0OneeW7gOXxVqicMrZGWMQ/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

Jamie Street | from unsplash

二、如何解决眼下的危机

---

  

窃喜归窃喜，眼前的问题还得先解决。我看了下新链路的数据产出正常，就把新链路 Hive 表的结果直接覆盖到老链路的 Hive 表里，下游就都能照常恢复。又赶上端午前发布封版，正式切换正好挪到节后再做。

值班的伙伴、数据治理负责人、几个核心下游，那天都松了口气。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/37X2DwwWHLhrd6gMsFkpc8bQ8ZfiaWYiaiapgMIbviaB3h4FpZQUmOicicNTx6JiahAuKxvkevkR0h8Tiav3FBgytUYEPSwiclFanIP9Zwy8l7p0aYVM/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

Jamie Street | from unsplash

平时业务团队对数仓了解不多。前几周出差开一个专项会，文档里数仓被归到了"其他协作方"，真的有把我气到，我马上私信质问了写文档的人。所以除了把活干好，我一直还想着另一件事：怎么让业务团队“看见”数仓 —— 比如这次重构，如何让他们知道我们用自己“未雨绸缪”的经验和付出，悄悄挡掉了一场数据危机。

三、和统计局朋友的一次聊天

---

  

端午假期里，一个在统计局工作的朋友找我聊数据仓库的设计思路：怎么整理核心宽表、怎么不用每次都花好几周重复拼统计表、怎么用离线的 AI 小模型解决一些痛点，是否可以根据他们的现状对数仓经验进行一些借鉴。没有 KPI，也没什么物质上的好处，我们却聊得很起劲。不过她后来说，同事们其实并不看好她的想法。

我自己内心猜测，她们的工作环境可能是被太多落不了地的务虚项目消磨过 —— 把事情推进一些的那点热情被逐渐消磨完了。

四、心灵奇旅

---

  

端午期间我在 B 站看了《心灵奇旅》，是听了有知有行创始人孟岩在播客《无人知晓》里推荐才去看的。

电影里有个设定叫"忘我之境"（the zone）：一个人彻底投入自己热爱的事时，比如主角 Joe 弹钢琴的那一刻，会忘记时间，那一刻他最像他自己。

![图片](https://mmbiz.qpic.cn/mmbiz_png/37X2DwwWHLhmHkt6orc5f6a8iatEYFqZElxy632Iiat8SPXeGUEApiaO2qoibSzbtibk4GwAr1ib9CbwslQNX3rPlx9ex1vPc6qV7EKRWCzvJCpTg/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

我忽然觉得，Q2 我挤出来的重构时间，就是我自己的忘我之境。我不为赶 deadline，也不为晋升，更多是觉得这条链路就应该要被修好。

我觉得《心灵奇旅》真正想说的，不是"找到你伟大的人生目标"。Joe 拼命想登台，真站上去才发现，并没有想象中那么天翻地覆。打动他的并非登台目标，而是热爱一件事、认真活着本身。

![图片](https://mmbiz.qpic.cn/mmbiz_png/37X2DwwWHLj2owicDAYKiclRg70tqWeX5J551oxaibkraQwkBtaGeMcibxG3FotPsljoibB4L1tRPBdPz17NqormEm9JZuZ6vExbaAG4PPoww75k/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

工作也是生活的一部分，顺心与否更多取决于自己的心态 —— 如何看待他它。升职加薪固然很重要，但我不觉得人只为了这些工作，人生是一场无限的游戏。

- Matt Hearne | https://unsplash.com/photos/burning-grey-sedan-near-trees-and-signboard-at-night-LA0NPeHdp5A
    
- Jamie Street | https://unsplash.com/photos/dog-sitting-in-front-of-book-Zqy-x7K5Qcg
    
- kike vega | https://unsplash.com/photos/silhouette-photography-of-woman-doing-yoga-F2qh3yjz6Jk