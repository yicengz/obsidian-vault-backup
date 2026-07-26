---
title: "对话Vincent Koc：OpenClaw的反思与进化，中国的“小龙虾”狂热，与Agent的下一步"
author:
  - "硅谷101"
link: "https://www.youtube.com/watch?v=tnvyMcmtAiw"
publish_date: 2026-07-21
clip_date: 2026-07-26
description: "OpenClaw，这个在2026年初引爆全球AI圈的现象级项目，让Mac Mini卖到断货，也引发了关于AI安全与边界的全民讨论。当喧嚣褪去，这项技术真正为我们的生活带来了什么改变？在WAIC 2026现场，我们对话了OpenClaw基金会首席架构师Vincent Koc，从项目爆火背后的故事聊起，也深入讨论了Agent为什么在中国风靡、OpenClaw如何从开源项目成长为全球社区，以及“降温"
trigger:
  - "youtube.com/watch"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=tnvyMcmtAiw)

OpenClaw，这个在2026年初引爆全球AI圈的现象级项目，让Mac Mini卖到断货，也引发了关于AI安全与边界的全民讨论。当喧嚣褪去，这项技术真正为我们的生活带来了什么改变？  
  
在WAIC 2026现场，我们对话了OpenClaw基金会首席架构师Vincent Koc，从项目爆火背后的故事聊起，也深入讨论了Agent为什么在中国风靡、OpenClaw如何从开源项目成长为全球社区，以及“降温”之后，为什么真实下载量反而创下新高？作为项目的核心设计者，他也详细拆解了OpenClaw“中枢神经”的Gateway网关架构，并回应关于安全、成本、模型偏见等一系列核心争议。  
  
相比讨论模型能力，这期视频更关注Agent真正进入现实世界后的挑战与机会。“后Claw时代”，Agent的格局正在被重写，也许保持开源，才是“把它送给全世界”的唯一方式。  
  
时间轴：  
00:00 龙虾热的前夜  
02:15 疯狂  
03:41 与Peter共事  
04:26 13000个PR  
07:44 为什么OpenClaw在中国爆火？  
10:56 降温与“后Claw时代”  
14:28 大公司造Claw的成与败  
20:47 当前挑战  
23:23 Gateway  
24:45 安全边界  
28:33 Agent背后的模型与框架  
32:09 记忆难题  
34:34 多智能体协同  
35:41 康威定律  
40:09 智能体Aha时刻未到  
41:37 退潮的经验与教训  
43:09 企业与个人Agent：互相喂养的增长飞轮  
44:28 OpenClaw App的布局  
48:04 Hermes Agent  
51:00 OpenClaw基金会：让“小龙虾”公平活下来的唯一方式  
55:08 如何招人  
55:52 如何决策  
57:40 Peter去OpenAI后：消除个人依赖风险  
01:00:55 保持开源：“把它送给全世界”的唯一方式  
  
【关于硅谷101】  
我们是由海内外一线媒体记者/主持人创办的栏目，深度解析硅谷创新趋势，以轻松的风格分享科技行业的最新动态。我们采过顶级科技大佬，积累了数万小时的媒体经验，做过调查性报道，操盘过千万级传播量的知名深度稿，引发全国讨论和微博热搜；致力于将最专业的媒体素养和信息搜集能力转化为易传播的新媒体力量。  
  
旗下同名播客栏目：https://www.youtube.com/@valley101podcast  
  
关注我们，从这里驶向未来。  
  
联系我们：video@sv101.net  

## Transcript

### 龙虾热的前夜

**0:00** · Open agent. Open claw is the number one. It's the most popular.

**0:10** · The single most important release of software probably ever.

**0:13** · Lobster themed installation events have popped up around the globe, especially in China. \[music\] Peter Steinberg. \[music\] We had a lot of problems because the the existing tools out there just weren't designed for our scale, but now it's getting better.

**0:41** · A few weeks ago, we hit like 4 point something million downloads a week.

**0:44** · They are saying \[music\] only startups can make things happen faster during the AI era. Peter's wishes were like he thinks the only way the open claw survives and is fair to everyone is that it remains in the in the foundation.

**1:09** · Open.

**1:16** · Hi Vincent, thanks so much for your time to joining us here at WIC 2026 in Shanghai. Let's start by introducing yourself a bit and explain your current role at the Open Claw Foundation.

**1:27** · Yeah.

**1:27** · So my name is Vincent Cotch. I'm chief architect at OpenC Claw Foundation essentially looking after product and engineering. And how did you first become involved with the open cloud community?

**1:38** · So I've been a open-source contributor for basically the start of my career. I kind of noticed this project in early December and uh this was on on X on Twitter. A lot of I think poly market traders were using it and I got really excited. I was like what is this? Let me check out the project and then was like wow this is this is crazy. This is exciting. I started testing it and then I wanted to help.

**2:03** · So I started contributing back to the project in like late December, early January and then eventually that kind of snowballed, became a maintainer and then from maintainer to my current job now.

**2:14** · Do you still remember the day when open claw got really viral?

### 疯狂

**2:19** · I don't know if there was like a particular point. I think for me in San Francisco was in February where there was like a first clock on sort of event and I think there was like a few hundred people uh guest list but the event started at 7:00 but if you arrived at 5:00 you were late and the queue was like around the building.

**2:42** · Yeah, I remember that one my business partner was there.

**2:45** · Yeah, it was crazy.

**2:46** · Yeah, she told me the queue is like a few blocks away already. Yeah. And it was and we hadn't seen anything like that sort of viral everyone is there, everyone's listening in San Francisco in quite some time. It kind of had that magic to it like you felt like something is going to happen. So for me like that was like the the peak sort of hype cycle and I think after then it just started taking off quite a bit.

**3:08** · But did you guys expect that you know the open club would got really really crazy in China? No, I was uh obviously still a maintainer, but we're in the team on Discord and I'm seeing like the aunties using it outside Tencent's offices in Shenzhen. I'm seeing rap artists on Twitter talking about Open Claw. It's just crazy. And I'm just like everywhere. It's just going completely viral. China, but also outside of China, as China especially. And um a lot of people like this is fake. And I was like no, it's not fake.

**3:37** · It's definitely definitely real. tell us how it uh looks like to work with Peter Steinberger, the creator of Open Cloth.

### 与Peter共事

**3:46** · I think there's a only a few people I've had the chance to work with that have like a very special way of seeing the world and really seeing the possibilities of what you can do. I think his attitude to life around, you know, make sure you put fun and energy into everything that you do definitely comes across in the work like you look at the fun little lobster and all of this. So I think for me has been not only just about you know creating what's new, what's on the bleeding edge, but also like that process of discovering something exciting has to be fun. You have to think like a child.

**4:16** · You have to kind of like push yourself in your thinking a little bit. So I think for me it's um no no two days are different. Every day is kind of very exciting as well.

**4:25** · And you said you joined the community in December last year only half a year away. We saw open claw, you know, growing from like perhaps a small project into a global sensation, a global open source community. What were some of of the biggest challenges that you guys have been through?

### 13000个PR

**4:43** · I think the biggest challenge is like as with anything is like anything of this scale becomes quite hard not to manage but to grapple with. you've built some software that's designed for developers or tinkerers and now suddenly you have enterprise companies deploying this or trying to use it to build their businesses, right? So then you start getting people screaming like is it safe or um how do we deploy this at scale?

**5:08** · Why is this using so many tokens and things like that? So you start realizing there's other challenges and everyone's like expecting you to fix this when actually it's just an open source product and we need to sort of like educate people like hey look we're going to do our best. we're going to try and help and solve this. But the frustrations that we got and the challenges that we faced ended up becoming the things that we started building for as well.

**5:30** · So for example, we ended up with I don't know at one point we had like 13,000 PRs open pull requests like changes to openclaw and um we developed our own review using AI agents to like manage this workload. So then we started building the other agentic tools to help us with the scaling problems that we're having and I think that was like the unlock for us and that was like the more exciting part. So we had a lot of problems because the the existing tools out there just weren't designed for our scale.

**6:00** · Yeah.

**6:00** · Yeah. But now it's getting better.

**6:02** · Yeah.

**6:02** · Like we've had to essentially build entire infrastructure. So if you if you look on um the open core website there's a little link called ecosystem. We have over I think close to 100 repos.

**6:13** · Mhm.

**6:13** · So a lot of people know uh open claw the agent but also we have different libraries we have different automation tools testing infrastructure and we've had to build all of these and there's a joke that each one of these tools are basically like a startup in themselves that we manage and um enables us to build open claw at scale if you have to describe open claw in a few sentences today what would it be for us open claw and especially the open claw foundation is not is I think it's

**6:43** · more than just this AI agent or personal AI agent. For us, it's like how do we empower the whole AI ecosystem agentic use be open and accessible to everyone?

**6:54** · That could be for enterprises, that could be for small businesses, it could be for moms and dads, uh it could be people that want to run local models at home as well. So for us, the mission is to really empower humanity with AI.

**7:05** · Did that mission change at all during the past 6 months? I think the that was pretty clear um you know when it started growing legs of its own the foundation was already being set up in the background obviously it's been announced recently so the mission statement was I

**7:21** · think as a collective was somewhat already there and the idea has always been like we want to keep Peter's wishes were to like you know he wants to keep it an open and independent product and put it into a foundation and for the same reasons it's like we want to make sure it's accessible to everyone it's continues to remain open source continues to remain um in the hands of the community which was very important and before we dive into the technical uh

### 为什么OpenClaw在中国爆火？

**7:46** · questions let's talk about the China sensation in the first quarter as you described the open claw got extremely popular in China I would say even more popular than Silicon Valley and there were long cues of people lining up to install open claw Apple Macd was totally sold out back then so why in China though I think there's a mindset thing that I've noted Especially in China, it's like, hey, we see that there's this new thing. It's going to empower us. It's going to help us. Let's embrace it.

**8:13** · I think the the the western sort of tech ecosystem was like, "Wow, this is scary.

**8:23** · It can do so many things. Let's block this and let's understand what's happening." And we saw this sort of behavior like back in 2023 24 with like Chach as well where enterprises were like we have to block this AI because like it's too scary, it's too dangerous. And then eventually they opened up and adopt and adopted it. But I think for China has been very much like I want to adopt it at speed.

**8:43** · I think and some of the stories I was hearing was like uh employees were given like KPIs like you need to automate this many things with openclaw whereas if you install openclaw in some enterprises in in other markets like you get in trouble because it's like security risk right so I think the mindset is very different around like I want to experiment learn and and build fast but I think it's just a just a

**9:06** · difference in the technology culture and the sort of the speed in which China has been moving especially with open source is it possible Um because you know like a codeex or uncle code is not that popular in China.

**9:20** · That's actually a good point. Yeah, it's not something I really actually thought about cuz the market penetration of these other products uh you know they they can't be really used easily or used at all within within the China ecosystem. So I think having something that's open source and available that people can adopt could have been obviously one of the key catalysts as well for this. For people who are not familiar with the open claw, can you tell them the difference between open claw and the coding agent?

**9:47** · So a lot of these coding agents are starting to become like open claw as well. So it's kind of interesting. But if we rewind back to the start of the year, the coding agents were very much like hey I have like a terminal or an app. I want to build I don't know I want to build a website or something. So you have a conversation and it goes off and builds it. The difference between now and like openclaw, openclaw could yes build your website but the whole idea was that like it acts as your personal agent.

**10:12** · So it would learn it will have a memory it would start to build skills it would go and do things for you but the beauty is that like those things could also be it needs to create code. So oh can you buy my groceries from this website?

**10:26** · There's API it finds it. So then it creates the code to do it. Or for example, let's just say tomorrow one of the labs releases a new model and there's no support. So you ask open core, hey, can you add this feature? And it can change its own code and adapt itself and and add that feature for you. So I think the difference between the coding agents is like it's creating code and it's it's blocked like the harness or the tool whereas the open core agent can change its own code. The agent can modify itself which I think is the difference here.

**10:54** · Smarter.

**10:55** · Yeah.

**10:55** · with so many people had to uninstall open claw after a while setting number one it's not so easy to use number two security concerns how do you see the cool down of the interest so one of the two things with that that's actually interesting is that there was definitely a cool down of the hype cycle like the the craziness sort of died out a little bit which was kind of good but the second thing is like we did mess it up a little bit where we were trying

### 降温与“后Claw时代”

**11:20** · to build this thing really fast using agents you know really trying to push the frontier here and we learned some good lessons on like how not to build software with agents. So we did make some mistakes and we did lose a lot of users because it wasn't as stable. But ironically we overcame those challenges a couple months ago and if you look at our download numbers now they're actually better than they ever were. So before the at the craziness of the hype I think we were hitting like 2 and a half 3 million downloads a week on npm.

**11:47** · So obviously there's Chinese mirror websites there's all these other sources. So download numbers are probably way larger but just based on npm and a few weeks ago we hit like 4 point something million downloads a week. So um so yes it it did sort of die out a little bit the hype but actually the adoption is actually scaling even more now. So it's kind of interesting to see.

**12:08** · So from that perspective I'm like really excited to see that like you know users are like responding to the like the stability and the features that we're releasing into the market.

**12:18** · Can you give us a few examples? what are some of the really good use uh examples that you see across different industries?

**12:25** · So, one of the things here is that like I think we talk about industry specific use cases. I like to think of it as like it's just like having another employee or internal personal assistant. So yes, it can be vertical specific use cases, but realistically it's like a case of if a model is good at doing some code or has understand some task really well and it has the tools or it can create the tools. I think it can do a lot of things now. So it can now browse websites, it can have a phone number, it can connect to messaging app.

**12:55** · So really the the possibilities are kind of endless but depends on the task, right? So maybe some design tasks are really hard or video editing might be hard. But as people develop agentic tools for those, your agent can then use it. For example, our agent creates soundtracks for our team every every few days and it makes it kind of fun for us, right? Whereas AI for music was kind of not so good before, but now it's good. So then we can give that tool to our agent. So for us, it's like less about use case and I think it's more about you kind of discovering what's possible.

**13:25** · One thing I do see that's interesting inside of uh enterprises and large sort of small to mediumsiz enterprises is also like employees having open claws in their kind of day-to-day job or projects having them. And I think that's changing the way employees work with agents cuz previously if I was an employee like an engineer I would use my own AI coding assistants and I would work and then share that with the team. Whereas now the it's not a coding assistant anymore.

**13:52** · It's an agent but it lives with the team right? So it can talk to my colleagues and my colleagues can talk to my agent and it has like a different kind agent to their colleagues.

**14:00** · Yeah.

**14:00** · So I think that's creating like a different dynamic for us in terms of workplaces and and how we operate and I think some organizations here in China and globally are starting to experiment with this and some are kind of pushing the boundaries around that. Obviously, we internally use agents and part of our workflow and talk to agents on a regular basis, but it's \[snorts\] um I think that's where it get starts to get really interesting because it's less about use case, but it's changing the way we work.

**14:25** · Actually, back to the first quarter, um many Chinese companies released agent products on the top of the open claw framework including Tensson Qclaw, volcano engine, art claw, Alibaba, Wu, Dclaw, etc. So many. Do you think that's the right approach for the 2C consumers?

### 大公司造Claw的成与败

**14:44** · I mean like this big companies they actually launched their own claw products.

**14:49** · Yeah.

**14:49** · So a couple of things here for for especially for us like we we were just pushing this open source product. China was running at fast speed. They wanted to get into the market. They wanted to get it in the hands of users and their customers really quickly. So they developed on top of it. Right? We didn't have the capability to do it at the time.

**15:06** · Now fast forward a little bit. do we want to go straight to consumers with openclaw like we kind of do that at the moment but realistically like at the end of the day we we just want to empower the ecosystem right and if that means that other companies are building on top of openclaw and getting that in the hands of users and empowering their users I think that's a great outcome for us but also at the same time the the

**15:30** · other key thing here is that like if we wanted to build infrastructure and servers and host it for people it kind of feels like it's taking us away from like what we're trying to achieve which is actually building this software that works really well and helping the ecosystem sort of get that in the hands of everyone else. That might change in the future but that's kind of like where where we see things at the moment.

**15:49** · So you would have seen also recently in the US we've had Microsoft scout which is Microsoft's version of open claw that's sort of out there and other companies are going to continue to do this and for us it's like how do we support the ecosystem where they want to build on top of it that could be a large technology company but it could also be a small enterprise that wants to do something internally as well a lot of uh the products I mentioned unfortunately uh did not work out pretty well what's the reason in your opinion I haven't had a chance to actually experiment with them.

**16:20** · So, um, bit hard for me to sort of answer that question, but I would say that possibly, you know, I don't know if it was features or if it was cost or what those things were, but with anything, it's probably worth sort of digging into, but yeah, I haven't had a chance to really dig into those products in detail.

**16:38** · Now, China Tech companies later developed their own agent products. For example, Tensson workbody now very popular, but it's not directly built on open claw. However, it is fully compatible with open claw skills and frameworks. How does open core actually mean to these uh latest rounds of agent products?

**16:58** · So for us like I kind of see this is like this postclaw era. I believe that like open claw really ushered like this next generation of agentic frameworks into the ecosystem. It kind of created this explosion of uh model labs and token usage. So, you know, at the end of the day, in terms of what we're trying to achieve, I think it's good to have other solutions out there in the market and that kind of enables like a really good ecosystem. So, um I think it's a positive thing for the consumer and the the users and the ecosystem as a whole.

**17:29** · And uh how do you continue to work with the big corp partnerships? M that one's a a bit more interesting, but I think currently our model is very much the case of like on a case-by case basis, but realistically we try to create one solution that fits most people and that's where, you know, we have to bring a lot of differences of opinion. We have to bring a lot of different technological ideas into the same place and get everyone to sort of agree on like what's the right way to do something.

**17:56** · And I think as we solve these problems, it could be security or whatever it may be, we're kind of bringing the ecosystem together to like come up with like okay, this is how we should solve this problem and this is how it should be designed. And by doing so, we're kind of help propelling the industry forward as well.

**18:11** · I know you've been traveling a lot these days, Japan, Singapore and of course come to China a lot. So uh when you uh do the partnership with the big corpse in different countries, are the partnerships different? Are the requests demand different in your observation?

**18:28** · I would say less so partnerships, but the companies that I've spoken to, and this goes beyond just like talking partnerships specifically, but just I like to spend a lot of time with developers, with enterprises, with the ecosystem as a whole. I would say sometimes the challenges may seem different, but I noticed that as a whole, they're all pretty much the same, right? And for example, you know, if you're in a country that has a large financial sector, you might be worried about what happens if your financial sector starts adopting something like open claw. Is that going to be a risk?

**19:00** · Is there some security concerns? So a lot of the challenges a lot of organizations and governments and policy makers and other people are talking about are going to be relatively the same thing but depending on where they are with their digital maturity it's probably going to change the the lens of of the sort of the complexities of the questions but majority of it sort of revolves around um you know how do we get value out of this? How do we uh manage cost? Um how do we make sure this is safe? How do we scale this properly?

**19:30** · like I think this is not an open claw specific thing but just AI in general when you speak to anyone right so I think any enterprise right now or any sort of large organization or any anyone who's technical is sort of thinking through these things uh when it comes to the AI strategy what does the China market bring to the open core community is \[gasps\] it a lot of contributors a lot of users big core

**19:55** · partnerships or continuous feedback I think it's a combination of all of those benefit with the Chinese market is obviously it's been fast at adopting open core faster than anywhere else. So for us it's like it's kind of a window into what's going to happen next uh in a way as well but also there's large enterprises here that are using it right I know of many enterprises here that have like every employee is using an open claw the projects are running on open claw and it's just interesting to

**20:22** · see the dynamics and to work with those companies and just understand like what are some of their challenges what are their learnings how can we share some of those so I think that's definitely the case and um and we have some maintainers on the team that actually are situated here in China as well. So we have that kind of mix uh global mix when it comes to our team and our road map and the features that we work on and also the developers that we that we listen to as well.

**20:46** · And um next I want to spend a few minutes uh to walk through some of the architecture and the really important technology questions. It was open architecture that made it stand out. um the gateway, agent runtime, sessions, memory scale, plug-in models, messaging channels, and connected devices work together in order to um have the agent complete the task. So, if you look back half a year since the beginning of the sensation, uh what really made Open Claw work?

### 当前挑战

**21:16** · What is still the challenge and what needs to be improving uh to make open claw work better? I think what what was missing and you can ask anyone this is like there was this promise of AI agents that would do things for you that you could talk to and it would understand you and it can do things to an extent and that promise just never came to life right you know yeah we had coding agents but like a coding agent is not the same as like my personal AI everyone wants personal AI and Peter was just like frustrated that

**21:48** · it didn't happen so he started building for himself and eventually a community formed around it and then it became open call as you know now so I that the fundamental needs of the users were like what people wanted were just like missing. Um, so I think that's the critical difference I think that kind of came about and I think maybe it was a combination of timing, the community, maybe a different number of factors that sort of helped bring that to life. And when we think about some of the challenges now, I think for us specifically, it's we know that the models are getting better.

**22:17** · Uh, open- source frontier models are getting better. So knowing that the models are going to get better, what are some of the other challenges that we need to face? I think a lot of it comes down to things like scaling within an enterprise. There's going to be some specific technological requirements. So for example, recently we've rearchitected the way we store information in OpenClaw. Before we used to write everything into files. Um so all your session conversations that's now put into a database that's in a little file.

**22:46** · What that means is that if you're an enterprise building this at scale, you can replace that file with a database system. You can take backups.

**22:53** · It makes this a lot more scalable, right? And easier to deploy. So yes, it improves the the performance for consumer use for like personal use, but also at the same time it means that for enterprises like or technology companies like you mentioned that are like building on top of these makes it really easy to build on top of open claw. So a lot of what we're building now is like focused on functionality around like how do we build this thing in a way that enables more people to build on top of openclaw for whatever their use cases might be or their business challenges might be. Let's talk some of the tech details.

### Gateway

**23:24** · Um so first of all gateway gateway is the central part of open clause design appears to be the central nerve system of open claw connecting messaging channels models memory and tools. Why did open core choose this always on getaway uh architecture and what can it do that a conventional agent framework cannot.

**23:46** · So the difference with uh why did this happen you'd have to ask Peter this question. I think it was his design or maybe his agent came up with this design \[laughter\] or back and forth they came up with this design. I'm sure there's a story. I just can't remember off the top of my head.

**24:00** · But I would say the difference at the time was that existing coding agents were basically turnbased, right? You had a thread and they were turn based. The difference with this sort of gateway concept is that like it was always on.

**24:12** · So it's like working like a service essentially on your machine and it would connect to the messaging channels and then that's where the concept of the heartbeat came in. So it's like every 30 minutes or every 10 minutes it's going to trigger a conversation chain. It's going to check if it needs to do anything. If it needs to do anything, it'll go off and do that thing. So it kind of created this like human like sort of like I'm going to go and do things in the background for you and have a way to like schedule tasks and with the agent and do things. I think that's what started giving this open claw a little bit of its magic as well.

### 安全边界

**24:45** · And also the getaway may hold credentials and execute actions score across the user system. Right. It is also open cloud's biggest security boundary. So what has opencloud community done to uh enforce the protection layer.

**25:00** · Yeah.

**25:00** · So a few things there. Um when it comes to credential storage like we've we've implemented some some security features where the credentials are not stored plain text like they're in a sort of vault sort of concept. But essentially one of the key things that we are working towards is like containerization right so you can run open claw in a container now so you can say that open core the that agent this is it can only have access to these files this internet connection things like that but we're taking that a step further and we're sort of like working with industry partners to like bring

**25:32** · that as like a more native feature without sort of saying too much but um where if you say it can only access these files there's a way that the oper operating system and open clock can kind of know 100% it's only accessing these files and if it needs to it goes back to the user and

**25:49** · it asks for permission right we're creating these sort of security boundaries outside of open claw uh as well and working with industry to make that a reality so that's definitely definitely in place and parts of this already exist now but parts of this will roll out as other technologies around security also happen cuz you also got to remember right like open core is like one piece of the puzzle you have the models you have the operating system you have the you know, we have to work across industry to sort of like solve this problem. It's not like exclusively us, but then you would have the same security uh concerns with any other coding agent.

**26:21** · If you gave a coding agent like full admin access to your machine, it can also delete files and go to the internet and do all these things. So, I think a lot of times a lot of people direct towards us. uh we're more than happy to sort of help solve the problem as well but I would say it's like still a agent specific sort of challenge but we are solving this more from like a containerization perspective.

**26:41** · So working out ways that you can kind of put it in a box safely and say hey you can only do these things and when a user accepts it or doesn't accept it like it's very clear and we we know that that's actually happened.

**26:53** · Yeah.

**26:53** · Well, I think you briefly mentioned this before, but what actions should an agent be permitted to take um uh autonomously and what kind of actions actually require them to um ask for approval?

**27:08** · I think that's really hard to answer because like it's going to come down to what your intentions are, what use case you're working with. You know, you might decide, hey, deleting files on my machine is dangerous, right?

**27:20** · But you might be working on another project where it's just a test machine, whatever, and you're like, delete them.

**27:23** · don't care, but like they're not the same thing, but they are like your intentions of like what you're trying to achieve is like going to be quite important. So if you look at other coding agents, they've rolled out things like automatic sort of approval using large language model to understand the conversation thread and do this. So we've implemented a similar feature called auto mode. So instead of having on or off, we have like this in between where an agent will look at your conversation and then decide based on your intent is this safe or unsafe and then ask for approval.

**27:52** · So we've sort of implemented that at a at a at the open core level which means that if you're using an open source model or some other model, you still get this feature. Now the other benefit with this as well, I might be using an open source model that might not have maybe some of the security guardrails. the auto mode thing could come from like a a Frontier Lab model.

**28:14** · So I could pay for that access and just have like that safe keeping what my agent is doing, but then I could run all my inference on say like a local model. So then I kind of get a hybrid um of these two worlds as well.

**28:26** · Yeah.

**28:26** · M so looks like a lot can be done actually through like different layers and you talked about models and we're now experiencing another round of soda model racing that come up very in China also in China that's right how much does model update actually impact the agent

### Agent背后的模型与框架

**28:46** · uh framework or like if I have to reframe the question when an open claw agent performs well how much of that performance comes from the underlying foundation model and how much does that capability comes from open clause agent harness memory tools or execute

**29:02** · environment I think it's a combination of both um I would also say that some models have also been trained post-trained on openclaw I know of some open source models especially some of the ones in China have definitely been post-trained on openclaw which means that those models then perform better because they understand like the model just knows that it's inside of openclaw and the memory and the tools and things like that so there's definitely like a combination of the two but We also know that some models don't work that well.

**29:28** · So, which tells us that like the model needs to be at a certain level of intelligence or size. We're currently working through a process of running uh a benchmark and evaluation that we're going to make public about 120 tasks, 100 tasks. We're working with some research teams and some labs and we're going to release that over the next few weeks hopefully. It's been taking some time and that's going to help us understand where the gaps are and we're going to kind of release that to the market.

**29:53** · But then we're going to work on okay where we know that the certain models or certain tasks are failing what can we do to improve that like can we improve the context or can we change something with the memory when it's a smaller model to like make sure that that performance works really well.

**30:09** · So I think there's a combination of the model but also how the model works in the harness and we we're seeing this with the frontier model labs they're all releasing harnesses as well u to complement their model and I think it's the combination of the two right um because those harnesses come with tools and memory and other things and those models have been trained to explicitly use those tools and I think that's what making them powerful and open claw supports models from different providers correct how can you guarantee the model independence in what Okay.

**30:38** · So that you treat actually models uh fairly not to favor certain models.

**30:45** · Yeah.

**30:45** · So we support any model release that comes out. We try our best to like get zero day support. We work with all the different model providers and labs like that. And yeah, we we don't specifically push one company or another company. Um we make sure that feature par exists as well and we do testing as well. So I think it just comes down to the capability. Uh we're also kind of built some features in there which allows model companies when they release new models they don't need to run an update on our side. They can push some changes on their end.

**31:17** · So that makes it sort of fair and a little bit more easier for everyone else. Um but I think the benchmarking process and the tuning is going to help us like especially with some of the smaller models uh make sure that there's like a better experience for users as well in open core.

**31:32** · Are smaller models important for the agent work? I'd say more for the local like the local model open source sort of community um specific tasks people are obviously concerned around token usage so for us it's like how do we make sure that you get some experience it might not be the best but like you might be able to carry out some autonomous tasks with open claw so for us it's like a really good learning experience to sort of figure out how do we then architect parts of open claw to

**32:03** · then be fair for all of these models right small, large, medium. So that's kind of part of the process as well.

### 记忆难题

**32:09** · Memory, um, persistent memory is one of the features that can make a personal agent generally useful and personalized.

**32:16** · Um, but it can also introduce errors, um, privacy concerns and unwanted assumptions. How to balance these two sides?

**32:26** · I would say the interesting thing with memory is like a lot of people might say it's like a solved problem.

**32:30** · In my mind, this is like 100% not a solved problem. I think memory is like one of these things where it's like really complex space like you've even answered it right like for example let's just say I'm using one model and the memory files get created and then I switch to another model how do we know that that model understands there's all these like complicated factors right um other issues arise when

**32:50** · you use like multi-tenency like what happens if you're sharing one claw in a team which memories can be shared with which people and that's why we we for now basically say with multi-tenency is like that claw assume everything is interchange changeable like there's ways we're working on like solving this sort of multi-tenency thing at the moment but you know that's why it's like a not a solved problem and we're actively working on this and looking at different ways of solving it that's probably like one of the more interesting harder problem spaces right now for sure.

**33:22** · Yeah. Yeah.

**33:22** · Cuz I think that's what gives it the the capability to do what it needs to do.

**33:27** · Yeah. Yeah. Mhm.

**33:28** · And also long horizon tasks are pretty challenging but necessary correct for the next chapter or what's uh your approach for long horizon tasks I believe a lot of the newer soda models are like getting better at long horizon tasks in general we're also seeing that industry is building um just for context like pre

**33:47** · prior to my work on openclaw I was working on self-optimizing agents so essentially how do we get agents to like recursively improve themselves for like a particular long horizon task So I think the frameworks and approaches are going to come out from industry around that and I personally believe they're just going to become capabilities that we can just give to agents as like tools or some sort of features that we can build into it and let it manage it.

**34:12** · So I think best way to describe it is that open core could act as like an orchestrator and keep on top of your work and you know do all of that and use different models to like orchestrate that work but like I I don't see us solving long horizon as a problem right whereas like different model companies and systems might and then we find a way to kind of like bring that into the open claw system and for the multi- aent design within open claw uh when is it useful to route

### 多智能体协同

**34:40** · work to isolated agents or specialist agents And when does that adding more agents simply create additional cost uh latency as well as coordination problems?

**34:52** · I think it's less about cost and latency but more of a case of like context. Like most nine times out of 10 for most people one single agent is like more than sufficient to like handle a lot of complicated stuff where it happens is like oh there's this other very particular task I want to run every couple of days do a certain thing. It has its own system prompt. Once you start like carving that out, then you're like, "Okay, I can just make that a separate agent." The best way to think about it is like I have one person, one employee working for me. Now, their workload is a lot and I know certain workloads is like very repeatable.

**35:23** · Okay, how do I take that work off them and then give that to someone else?

**35:28** · So, kind of think more like I'm managing someone.

**35:31** · How do I break this workload up between people? Is like a better sort of mindset to sort of apply to this um when you're thinking about this. And we are seeing some agent systems are moving uh towards a more complex structure involving managers, planners, uh sub agents and nested team of agents. Uh however, open core actually continues to uh keep its like uh simple or so-called pragmatic approach. Why why is that?

### 康威定律

**36:01** · So in engineering we have this concept called Conway's law which basically means that like most organizations will their software code will map their internal organization structure.

**36:12** · What do I mean by this? Let's say my marketing team had a growth team and like a retention team. When I build the code, I might have a separate like promotion system and a separate like retention data system, right? Just because that's how my teams work. So I want one team to manage this code, manage another. I think complex organizations are like mirroring their internal organization design into their agents because they have a certain organizational structure. They create agents in that way.

**36:39** · It doesn't mean that that's the optimum way to solve things, right? So I think we're inherently taking on the past challenges and not thinking from like a clean piece of paper like what would be the ideal way and just building from the ground up.

**36:53** · And I think this is why some startups and some newer organizations are like able to like build agent first and like work at rapid speed versus some other organizations that have to go through a full change management process and like really understand what does this mean?

**37:09** · Um, I got a close friend of mine, she works in like transformation, AI transformation like like a global scale and we were having a conversation and she was saying to me, this is just me sharing some personal notes by the way was like you know CTO's have all these resources they've all this like agent designs and frameworks but if I'm a chief operating officer like what does the future of the workplace look like what does the team structure agents like what does that all look like and I think those are like the conversations that people need to have because they're just kind of taking what they have and then just putting into an agent expecting it to magic work is like I think where some of the challenges are.

**37:42** · So people need to have the right expectation of the agent or the way to get that expectation is through experimentation, right? Like start with a blank piece of paper. I'm going to redesign this team or this problem. Let's build some agents. Let's get it to let's build something in a day. Let's get it working. It's not going to work perfectly. What do we learn? And let's let's iterate on that.

**38:02** · Whereas instead of taking like small small pieces and like trying to solve this problem and make it perfect and I think it's more a case of like how do we increase the maturity of of like this agentic design and the way I keep saying to people is like 2026 of way of like agentic engineering is very different to like how AI and agents were being developed prior to that and I think a lot of organizations and individual developers and product people just haven't quite crossed to the other side. Yeah.

**38:32** · And realize that actually no the models like the SOT models we're speaking about have really good understanding of this problem and you can just talk to it and like work with it and and build the agent together right with the agent and get it to a point and then you can learn from that and you can apply the learnings instead.

**38:49** · It's like oh I'm going to build all these little skills and then see what happen just you know it's like a I think you can just like leaprog basically and learn from that experience.

**38:57** · Yeah.

**38:57** · as you said there's like a um a surge of skills and plugins and MCPS um so we can see like open core still maintains like a small and core uh framework um within this opensource community while the ecosystem is expanding. Do you see open core actually will keep that small core or it will slowly expand uh to do more like third party ecosystems by itself?

**39:24** · I think it's hard to say, but like we're definitely looking at ways that we can support the wider ecosystem um in different ways and some of our plug-in architecture has definitely been changing and shifting to like how do we move as the industry shifts. It's not like we have like a new concept like MCP or skills like I don't think we've had one of those in a while, but it's more how do we build on top of that, right?

**39:47** · Um like an example the other day that we're talking about internally like what happens if one skill is dependent on another skill. Right now the skill spec doesn't accept that like there's no such concept of this in the industry. So we're like do we adopt this and build this and then force the industry to do it. I think that's where we would work with the ecosystem and like figure out like where some of the challenges are and how do we sort of like think about what's next.

**40:08** · I think you mentioned that u uh Peter and other like core contributors were wondering uh why is like agents aha moment hasn't come yet. Um so is the technical uh bottleneck there's cost there's you you know there's how reliable is the model like there's there's all kinds of factors around this right so and again going back to my point it's like it's not just an open clause specific issue it's like also the models and other things that like encompass this ecosystem right and

### 智能体Aha时刻未到

**40:41** · like you might have all of the companies that you're using like the banks for example do the banks allow your agents to come in and transact and move your money around and do this thing so I think there's a lot of challenges with like the services that your agent wants to access and how do they access it and so I think like the whole industry is like sort of growing up as well. So I think we'll start to see that becoming more reality as services are like allow agents and they're safe and the models work and you know I think it's going to take a little bit of time but we are definitely seeing a lot of improvements.

**41:10** · The biggest unlock for me I've seen is the use of computer use models where you know like any one of the agents some agents support it and some of the harnesses. We're also looking at like some open source computer use um stuff on our harness so that you can use other models as well. And the idea is that like it can just take over a web browser, right? Start clicking things and doing things. So with your permission which might be like a way to sort of unlock the some of the challenges people are facing as well.

**41:36** · After the first wave of the excitement in the first quarter, we talked about the cool down right. Um did the team did the open call community actually learn something uh from the cool down?

### 退潮的经验与教训

**41:49** · I think for us it was like we just need to make sure that we build reliable software that works and works really well. But trying to do this in a way where agents are the main engineers and you're engineering the agents to do this is very very hard and we had to spend a lot of time building the tools for this right. So like one of them was building extensive testing tools.

**42:10** · So right now any one of our agents, any one of the maintainers can their agents can spin up any operating system on any type of hardware on most clouds in like 20 seconds and they can go inside, take screenshots, do video recording, click through and that's how the agents able to test and validate the changes and make sure that it's working and allow us as maintainers to go in and see for ourselves and see proof. Mhm.

**42:33** · So if I say hey attach proof to the P screenshot before after video recording or hey I want to access the machine it will say okay here boom I open a web browser I've logged you in you can now take over this test machine. So we had to build a lot of these things that didn't exist. And I think that's one of our learnings was that actually like to make aic engineering work at scale. We call it a factory. The factory needs all the other machines to work right. You can't just have one conveyor belt expecting it to work. You need the quality assurance. You need the lights.

**43:00** · you need all these other things to make a factory run and the water electricity right so for us it was like we had to build all this other mechanics and that were missing and uh we are now seeing the adoption of individual developers and doing like personal AI we also seeing the enterprise side that they're adopting a lot of open open call framework uh as well so um to see and to be these two

### 企业与个人Agent：互相喂养的增长飞轮

**43:24** · approach which one is now moving faster from your observation they're kind of one is feeding the other right So as consumers adopt it, some of those consumers work in enterprises and they're like, "Okay, how do I bring this into a business setting?" But then as enterprises adopt it, it's making the product better at scale for different use cases, which makes it better for consumers to adopt it because it's more reliable cuz enterprises can use it. So it's kind of creating this like really interesting flywheel for us. And it's very different because you know traditional software like if you build for an enterprise or a consumer, it's usually very different.

**43:54** · And the reason why it's very different is maybe from a go to market perspective, right? sales, promotion, pricing, and the feature set changes because we're not technically selling the product. It really comes down to feature differentiation. And because Open Claw is quite extendable, allows enterprises to like really make it and shape it into what they need.

**44:11** · So, I think we're kind of in this like really good sweet spot which kind of fits most people's needs uh currently, but the challenge is obviously working with industry and working with the ecosystem to like figure out what's you know, how to how to balance everyone's needs properly. You guys actually launched the mobile app for iOS and Android. Why did you do that?

### OpenClaw App的布局

**44:32** · So, we actually had the apps built for a long time. I think it was still in the codebase in like January, February. We hadn't registered an entity.

**44:40** · Yeah.

**44:40** · So, the foundation got stood up as an entity and because it was stood up, we could finally go to Apple and Google and go, "Hey, can you give us a developer account and and we'll publish it." Right. We didn't want to publish it under some contributor's name. We wanted to do it officially.

**44:54** · \[snorts\] Um, so we had them and we wanted to release them. Um, I think some people want a first party experience. Um, and some people really enjoy that first party experience and some people might not. So I think for us it's just giving people optionality on how they want to use it, right? So for us it's not any extra work cuz we've already done the work building these apps. It's just more a case of getting the hands in getting into the hands of people. And um I I saw some less positive feedback uh from some of the uh consumers. What is the biggest challenge there?

**45:26** · I think the thing with people is on especially on the internet is like very quick to criticize. I think for us has been we develop at speed and the beauty with all that criticism was like great we now have tons of feedback that we can incorporate. So since then we've made a number of releases and even within the

**45:43** · space of 2 weeks since we've released the apps if you look at what it where they are now versus where they were before they look totally different like it's like almost completely different product and the beauty with open source is that like other people could contribute so luckily we had people making contributions which was good but then a lot of designers were for example sending us nice designs that they created with AI possibly going implement this and you're like okay can you do a pull request can you like help us get this in they're I don't know how to do that.

**46:09** · So a lot of people are quite quick to like make comments about software but I think people forget that it's like you know the open core foundation like main engineering team is like five or six people you know yeah we have other contributors and people working across the ecosystem as well but like we're not some 200 person startup you know a large

**46:28** · enterprise but they're kind of expecting us so like quick quick can you do this but we took on all the feedback and we and we made some some quick changes and we'd rather get the product into hands of people get feed back then to try and make it perfect and spend months and it's not what people want.

**46:44** · I think this is what I was saying earlier about how enterprises need to think about agentic engineering is like we can move quickly. So if you can move quickly, you're better to just get it out there, get get some feedback and then iterate quickly. If people made bad comments and then we did nothing about it, then I'd be like, okay, that's bad.

**46:58** · But we were able to sort of like really change and shift and and make a lot of changes. the same time the websites got redesigned, our documentation got redesigned, like a whole bunch of stuff got redesigned. We're still hiring for product designers um as well onto the team.

**47:13** · But yeah.

**47:14** · Yeah. To be honest, I was a little bit surprised that you guys launched an app cuz I thought that's what a startup would do.

**47:21** · Yeah.

**47:21** · I mean, the testing tools have been pretty good. We have testing tools and they'll go and like launch it on phones and take screenshots and videos and maintainers would just kind of compare like, "Yep, this video looks good. It's like approved." So it does all the work, right?

**47:34** · We still need to drive it, but we can do a lot more than we could before. The apps aren't super complex, right? Like a lot of the features already exist in the web UI. So it's more a case of like the same feature set in Android and iOS. The other thing we've also done is we we're not using some framework. We've written it in fully native Android code, fully native iOS code. So we're not having to ch battle complex code because the AI agents can write native code really easily. So I think there's some architectural decisions we made that make it really easy to maintain as well.

### Hermes Agent

**48:04** · Do you guys see Manners or uh Jspark as competitor?

**48:09** · I haven't really used their products lately. So hard to answer but I don't know for us it's like I don't particularly see anyone as competitors in the industry. At the end of the day, we're trying to propel the agent industry forward um in this case and I would say like our adoption and growth is like just quite large and we're building more like a harness layer, right? We're building this sort of personal AI agent layer and now for enterprises as well and it's very different from some of these other products and services.

**48:40** · Some of these are closed source SAS products which is very different from having like an open source product that you can take internally into your organization and build a business on top of as well.

**48:51** · I have to mention another competitor of your yours. Um although you don't want to call anything competitor which is Hermas agent. A lot of developers they expressed a preference for Hermes agent describing it as linear or more coherent for certain user cases. Did open core team actually learn anything uh from the her?

**49:12** · I think for us like some of their memory they're very different and divergent from some of our features and the way our features work. So they kind of give you this like very out of the box sort of experience. I would say some of the stuff they've done around memory is very different and kind of interesting. Some of the onboarding is kind of very interesting as well. But um I would say we're we're quite fundamentally different in terms of products.

**49:33** · So although on the surface yes they're essentially personal agents you can connect them up to most messaging channels but some of the internal mechanics around is kind of very different as well and do you see like more uh open source uh agent frameworks coming out uh to the market and also do you expect the um the agent framework eventually to consolidate uh around a few dominant platforms which is you know similar to the operating systems.

**50:04** · Yeah, I mean you could argue, yeah, maybe we will see some consolidation, but like if we looked at any of the AI tooling out there in the market right now, like none of that's happened. We have like hundreds and thousands of like AI software companies, right? So, hard to say what the future's going to look like, but yeah, we're going to see more and more agent frameworks. I think it's just going to accelerate. Everyone's going to create like maybe there's going to be vertical specific ones or industry specific ones or whatever the needs are.

**50:29** · Uh there might be niche products obviously to tap into that specific market, but at the like larger scale there's only going to be room for like a small handful maybe, but we'll see. Like it's really hard to say. Like this industry literally changes by the hour.

**50:42** · Like I can open up my phone and look at my newsfeed. I'm sure some new release of something crazy is happening right now, right? like and but I think that's also exciting that there's a there's a lot of opportunity there for anyone who's building but also for us as well to be able to sort of support the community as well which I think is really good thing.

### OpenClaw基金会：让“小龙虾”公平活下来的唯一方式

**51:00** · Next let's talk about the foundation.

**51:02** · Can you explain to us how the open claw foundation operates in practice?

**51:07** · Essentially it's a 501c.

**51:10** · It's a nonprofit registered out of uh the US and because of that we obviously don't make revenue. um if we do make any sort of revenue, it's obviously going back into the community, back into the product and back into uh the ecosystem.

**51:25** · And our focus and our mission is essentially what I've been sort of focusing on around like making sure personal AI and AI agents is like available and accessible to everyone and empowering sort of uh everyone. uh the operating model uh it kind of we we we kind of work like a startup when it comes to our engineering.

**51:43** · Yeah.

**51:44** · But obviously being a nonprofit organization we have to sort of work in a certain way as well. So we have like governance and all these structures and stuff like that.

**51:53** · But predominantly we we get you know donations from the community we get donations from the tech ecosystem that then drives uh a lot of the hiring and different product initiatives that we're doing at the moment. So you would have seen we recently made an announcement of some of the partners that have um and some of the people in the industry that have been really grateful and sort of supporting our mission and that's usually the sort of the driving force behind it and it's very different from say like a venturebacked business that has to scale up to certain number multiple and hit a certain revenue number and things like that.

**52:24** · Ours is mostly focused on what impact are we doing into the ecosystem and what impact are we doing to enterprises, personal users, you know, the the whole AI community as a whole, which means that our mission is very different. We we're essentially want to become Switzerland for AI agents.

**52:44** · Yeah.

**52:44** · Is a donation enough to uh run the community or the the foundation where you actually need a a lot of talents?

**52:54** · It's hard to say what's enough or not enough. Like you could argue that there's unlimited work and it's never enough. But I would say that we're very grateful for everyone's support. Like we get support from people giving us small even $5 donations on GitHub down to, you know, supporting us with like, hey, we want to give you some tools to use for certain things. So I think support comes in many different shapes and forms. And I think we're very grateful for the community and the different partners out there and everyone that's kind of been supporting our mission.

**53:23** · Do you have the guidance of um what kind of money you can absolutely take?

**53:28** · I think internally we do have some you know we don't just take you know anything from anyone but that's something I'll have to check and come back to you if it's public or not. I'm not sure.

**53:37** · You are now the chief architect and minister of lobster affairs.

**53:41** · That's a bit of a joke.

**53:43** · Yeah, I like this. And you have five members of technical staff um for product and engineering. Dave is the chairperson and also you have four other people responsible for community partnerships, talent and finance. You have core maintainers and of course the global community behind you guys. Uh but are these people enough to handle today's uh open claw daily operation? I think as as we scale, we will continue to scale and we continue to sort of grow the team and continue to grow like our support system around that.

**54:14** · You'll notice like we have a number of job openings currently and we're going through a hiring process to continue to scale the team, but we're also cognizant that like we don't want to just explode and hire lots of people because we feel like we need to. I think there's like being mindful around what that looks like.

**54:30** · So for example, if we hire someone into a function, it's like okay, how does an agent first look like in this role like design or events like how do we build like an agent first version of this and sort of build that up with that with that individual and then see how far we can scale that and it's not about not hiring people but it's about creating efficiency and then also giving this back to the community as well. So like everything that we do internally and the way we operate we open source and we give back to the community as well.

**54:54** · So I think there's some some interesting things like yeah we'd love to hire like everyone we possibly can straight away but we also have to be mindful of like cost and like what does that look like and the impact that we need to drive from that as well.

**55:07** · So is it hard to hire people nowadays cuz there's apparently a talent war in Silicon Valley.

### 如何招人

**55:14** · I think for us it's very different. Yes, there's definitely a talent war, but I think our project is very unique uh in terms of its position and its mission as well. And I think that attracts a certain type of people um into this project which aligns with our mission and what we're trying to do. So, I think creates like a very unique sort of opportunity. I think people that work in open source do it for the love, you know. I think there's like a passion.

**55:42** · You want to give back to the community.

**55:43** · Yeah.

**55:44** · Um, and I think that, you know, we want to attract those sort of talent as well and sort of foster that sort of talent as much as we can.

**55:51** · Cool. And, uh, you don't always agree with each other, I guess, within the foundation. So, when there's a disagreement, who has the final say?

### 如何决策

**56:00** · We've never actually had to like put the hammer down and and and and get to a point, but I think eventually we'd work out like, you know, who said what. But we have enough people and enough differences of opinion that collectively we tend to we finalize and agree towards something.

**56:16** · And I think a project of this size and complexity, I think disagreement is a good thing.

**56:21** · It means we're thinking through the changes. We're thinking through our opinions and our differences. If we all agreed with everyone, I think we would just end up receiving product that just doesn't work well. Um, the fact that we have such a diverse mix of maintainers on the project and organizations we work with means that we get like very challenging opinions, right?

**56:40** · You know, for example, someone wants to put a feature in, you know, maybe for enterprises that helps in the in like a say US technology space, but then like maybe some Chinese maintainers like, hey, like this isn't going to work for us. Okay. So, how do we then create a feature that works for everyone or vice versa? It's just an example, right? So, it's like making sure that it's fair and and works well for everyone is like part of the part of the challenge. But I think disagreements are healthy.

**57:04** · We haven't had any sort of stalemate or any issues with that. I think open source communities tend to be open source projects tend to be I don't know have its own way of solving these problems. Sometimes they can get quite heated like we haven't anything had anything too crazy. um but they tend to have their own sort of rhythm and flow and way of dealing with these issues and they have done for quite some time. So a lot of the maintainers on the project have worked in large open source projects as well.

**57:33** · So for a lot of us it's like we're kind of used to dealing with these sort of situations.

**57:38** · I have another question I have to ask about Peter. Uh of course I know uh pe people at the open claw foundation uh also the community were happy for him uh after he announced that he will join open AI but openclaw's early development

### Peter去OpenAI后：消除个人依赖风险

**57:54** · tied closely to Peter and now the foundation per se how can you uh actually guarantee the mechanism that can work well uh and reduce the risk of relying too much on one person individually I'd say we don't have like a single person risk at the moment we have an entire our team of engineers. If you look at the commits, for example, it's like starting to smooth out a little bit more as well. You know, Peter's vision definitely matters a lot to us and the team as well.

**58:20** · But as we continue to scale the team, I think it's how do we take that vision of Peter, myself, and other people like how do we kind of bring that together into a cohesive like strategy road map and get everyone aligned to the end state that we're trying to go towards. So I think that's the sort of thing that we're working towards that reduces any sort of risk around like this is a oneperson team.

**58:37** · I think there was a big misconception like even when we had a huge maintainer group a lot of the community was still thinking hey it's just Peter right I mean fundamentally to to an extent a large percentage of the the commits are still coming from like a handful of people myself included but it's hard to

**58:56** · quantify because like just looking at commits is not enough because some of the changes can be quite fundamental let's say security related but there's only like a small volume but could have large impact so we have a mixture of people contributing in different ways is and it's hard to quantify what that looks like, but I would say that like it's it's now quite blended. Like I might not have the full picture on everything, but not every person on the team has like the full 360° view, but we're collectively owning parts of the problem and working together to solve it.

**59:25** · Yeah.

**59:26** · Cool. And looking ahead, what is the single biggest challenge facing the open claw community today? I wouldn't say so much challenge of the community, but I would say there's a lot of opportunity. There's a large percentage of users in the world that are still not haven't fully adopted AI yet.

**59:45** · For us, it's like how do we make this more accessible to the general public, to moms, dads, uncles, aunties, whatever. Like, how do we make AI easy to understand and work with?

**59:54** · Because I think if people can access it, they can use it, they can understand it, and it means that they can have a say in what their future looks like with artificial intelligence. whereas um if you don't get a chance to use it, I think that's like, you know, not fair.

**1:00:06** · So, we're trying to make sure that everyone can can get access to something like this technology. And I think there's still a huge percentage of population that still hasn't touched AI.

**1:00:15** · So, how do we how do we enable that? On top of that, I think one moment people are waiting for is Apple and people are really hoping that u the uh mobile agent can really work so that people you know billions of people who are having phones can most people's computer is their phone right they everyone has a phone but they don't have a computer so um having like that ondevice agent first experience is probably going to be quite critical you guys have any plan to perhaps work with Apple to make the AI experience better time will tell yeah But it's hard like

**1:00:48** · we want to integrate with every uh AI technology out there. But um yeah, we'll see.

**1:00:54** · And open source projects can be more difficult to sustain uh than the traditional software projects because um infrastructure talent, maintenance, operation or takes money, right? Why would you guys want to keep open claw as open source community? uh because we can see um some open source community for

### 保持开源：“把它送给全世界”的唯一方式

**1:01:17** · example VIM and SG lang the founders actually came out to start their own business own startup to raise money they have very impressive fundraising and uh um you know they they are saying only startups can make things happen faster during the AI era do you agree I mean

**1:01:39** · I don't know if there's a right or wrong answer for this but I would say Peter's wishes were like he thinks the only way the open clause survives and is fair to everyone is that it remains in the in a foundation and it's not controlled by one company or one country or one entity and that way it can be truly embraced by the community and I think by doing this we've been fully embraced by China the US tech companies moms dads like

**1:02:02** · everyone right and I think that's enabled everyone to go okay this is like a fair kind of like a Switzerland of AI we're happy to work with work with that and we've had people reach out to us that exclusively want to find a way to work with us because we're in a foundation model. So I think it brings benefit and yes it doesn't generate revenue or create sort of capital wealth but I think it gives back to the community. What we give back creates opportunity for the industry to then create more capital. So I think it's a positive sum game for everyone at the end of the day.

**1:02:34** · It's selfless I think in a way for Peter to go hey I want to give this to the world but I think it's a beautiful thing that's happened. Great to hear. How is your experience with WIC this year so far?

**1:02:46** · Yeah, I'm just hearing lots of crazy things so far. I haven't had a chance to go out yet this week, but I think it's going to be great. I'm giving a keynote about my journey through open source, which I think is going to be great, and I'm going to be like really excited to see a lot of technology companies here and get part in the conversation as well. I think it's going to be like a very invigorating week. I think by the time the conference is finished, I'm going to be like, "Yeah, I'm I'm done."

**1:03:13** · But really excited. I'm glad to be uh here back in Shanghai as well.

**1:03:17** · Okay, cool. Last question. So, for the next 12 months, uh if you can give us some predictions, you know, what are the most important three things that will happen? Uh whether it's agent related or not.

**1:03:31** · I don't want to give too much away. I think the thing that people need to watch out for, I think it's going to be interesting is like how do agents communicate and collaborate with other agents is going to be the next uh sort of interesting thing. If say a soda model company comes up with a solution, another model company comes up with a solution, how did these all coexist and work together? We're going to have like a world like phones, right?

**1:03:51** · Everyone's going to have a different phone, but they need to be able to call each other, right? It's going to be a very similar process. So, I think that's going to be one that's going to be really interesting to see what happens.

**1:03:59** · We're experimenting on some ideas around that. Um, but that's going to be really cool to see because I think there's that's going to be where we're going to start seeing some some really interesting unlock when I don't know my personal agent can call my work agent and share some information and get to work together and solve some problems, right?

**1:04:17** · Yeah, I already heard some scary uh stories saying like the AI agents actually invent their own language that humans don't understand.

**1:04:28** · We'll see. But um a lot of the uh mechanistic interpretability stuff is quite interesting around evaluation. Um the agents will find what's mathematically most optimal or like whatever's been trained into it. I think we just have to be careful of like seeing that because agents are doing some behavior that it becomes we don't want to kind of say because X is happening it's Y.

**1:04:51** · Um we need to understand like what's causing it. But I think safety is one aspect, but also like just even getting these agents to communicate with each other is going to be the the challenge, right? Like you've got enterprise, you got different software systems, you got different architectures. So I think a lot of those kind of challenges are like actually way more complicated than security for example.

**1:05:11** · Mhm.

**1:05:11** · Yeah.

**1:05:12** · Yeah. All right. Okay. Anything else you want to add? Anything?

**1:05:15** · No, I just want to say thank you for the opportunity to come and have this interview and this conversation. So excited to be here.

**1:05:22** · Okay. Thank you so much, Vincent. Hope you enjoy your time here in Shanghai.

**1:05:26** · Thank you.

**1:05:38** · Bye.