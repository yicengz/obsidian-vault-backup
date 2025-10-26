> spark源码里，QueryExecution.scala文件里，val tracker: QueryPlanningTracker = new QueryPlanningTracker，是什么意思

```
SQL 查询提交
      │
      ▼
+-----------------------+
|  QueryExecution       |   // 一个查询生命周期的封装类
|  val tracker = new    |
|      QueryPlanningTracker
+-----------------------+
      │
      ▼
tracker.measurePhase(ANALYSIS) {
    analyze()  // 解析 + 分析
}
      │
      ▼
tracker.measurePhase(OPTIMIZATION) {
    optimizer.execute(logicalPlan) // 逻辑计划优化
}
      │
      ▼
tracker.measurePhase(PLANNING) {
    planner.plan(logicalPlan) // 生成物理计划
}
      │
      ▼
tracker.measurePhase(EXECUTION) {
    execute() // 执行物理计划，生成 RDD/Dataset
}
      │
      ▼
+---------------------------------------+
| tracker 记录每个阶段的耗时            |
| Map[Phase, Long] 例如:                 |
|   ANALYSIS -> 35 ms                   |
|   OPTIMIZATION -> 10 ms               |
|   PLANNING -> 5 ms                    |
|   EXECUTION -> 200 ms                 |
+---------------------------------------+
      │
      ▼
Spark UI / SQL Execution Listener
读取 tracker 里的耗时信息，展示在 UI
```




> spark源码中，有一个QueryPlanningTracker.scala文件。代码中有一个object QueryPlanningTracker {} 和 class QueryPlanningTracker {}，分别是什么含义

## **1.**  class QueryPlanningTracker
- **这是一个普通的类**
    用来描述一个具体的“查询计划跟踪器”的实例，里面定义了实例级别的字段、方法、状态。
- 你要用它，必须 new QueryPlanningTracker()（或者通过伴生对象提供的工厂方法）。
- 每一个执行计划可能会对应一个 QueryPlanningTracker 实例，用来记录分析、优化、执行等阶段的耗时信息。
## 2.object QueryPlanningTracker
- **这是一个单例对象**（全局唯一的实例，类似 Java 的 static 成员容器）。
- 不能用 new 创建，直接用名字访问。
- 主要用来放：
    - **全局常量**（例如 ANALYSIS、OPTIMIZATION 阶段名字）
    - **工具方法**（静态工具函数）
    - **工厂方法**（创建 QueryPlanningTracker 实例的便捷方法）
- 它和 class QueryPlanningTracker 之间是 **伴生关系**，可以互相访问对方的 private 成员。

```
用户 SQL

   │

   ▼

SparkSession.sql()

   │

   ▼

QueryExecution

   │

   │ 创建查询执行对象

   │ val tracker = new QueryPlanningTracker()  ←─── 用的是 class，生成实例

   │

   ├─── withTrackerPhase(QueryPlanningTracker.ANALYSIS)  ←─── 用的是 object 中的常量

   │        │

   │        ▼

   │   tracker.startPhase("analysis")   ←─── 记录开始时间

   │        │

   │        ▼

   │   Analyzer 分析逻辑...

   │        │

   │        ▼

   │   tracker.endPhase("analysis")     ←─── 记录结束时间

   │

   ├─── withTrackerPhase(QueryPlanningTracker.OPTIMIZATION)

   │        │

   │        ▼

   │   tracker.startPhase("optimization")

   │        │

   │        ▼

   │   Optimizer 优化逻辑...

   │        │

   │        ▼

   │   tracker.endPhase("optimization")

   │

   ├─── withTrackerPhase(QueryPlanningTracker.PLANNING)

   │        │

   │        ▼

   │   tracker.startPhase("planning")

   │        │

   │        ▼

   │   Physical Planning 逻辑...

   │        │

   │        ▼

   │   tracker.endPhase("planning")

   │

   ▼

执行计划生成完毕

   │

   ▼

可以通过 tracker.report() 输出各阶段耗时
```