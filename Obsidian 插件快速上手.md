# 🎓 Obsidian 插件快速上手

> 针对你的复习备考场景，挑最实用的几个插件一步步教。

---

## 📌 写在前面

你装的 23 个插件里，我按 **优先级** 分成三档：

- 🔥 **马上学** — 你复习考试立刻用得上
- 👍 **有空学** — 锦上添花
- 🧊 **以后再说** — 特定场景才需要

---

# 🔥 第一梯队：马上能用

---

## 1. Spaced Repetition — 闪卡复习

> 最适合你的场景：把错题/知识点做成卡片，按遗忘曲线自动提醒复习

### 基础用法

在笔记里用 `::要记住的内容::` 或 `?::要记住的内容` 标记：

```markdown
问：WBS 最低层次的可交付成果是什么？
答::工作包
```

或者用问答题格式：

```markdown
软件项目区别于传统项目的特殊性有哪些？

?::变更频繁、渐进明细、逻辑实体、相互作用系统
```

### 实操：拿你的复习题试试

打开一份课堂检测，找到一道做错的题，改成闪卡格式：

```markdown
增量模型的每个增量都必须包含完整的软件功能。

?::错。增量是软件功能的一部分，逐步交付。
```

### 操作步骤

1. 在笔记里写好 `??::` 或 `::` 格式的内容
2. 按 `Ctrl+P` 打开命令面板
3. 搜索 **"Spaced Repetition: Review"** 回车
4. 卡片就会弹出来，选 **正确/错误/困难**
5. Obsidian 会自动安排下次复习时间

> ⚡ 快捷键：建议给 "Spaced Repetition: Review" 绑定一个快捷键（比如 `Ctrl+Shift+R`）

---

## 2. Kanban — 复习进度看板

> 把你的复习计划变成 Trello 风格看板

### 快速创建

1. 按 `Ctrl+P` → 输入 **"Kanban: Create New Board"**
2. 选个位置保存，比如 `软件项目管理复习题/复习看板.md`
3. 会生成一个文件，里面是 Markdown 格式，看板是自动渲染的

默认列：

```markdown
---

## 待复习

- [ ] 第三章：生存期模型
- [ ] 第四章：需求管理

## 进行中

- [ ] 第六章：成本估算

## 已掌握

- [x] 项目基础概念
- [x] WBS 分解

---
```

> 直接在 Obsidian 里拖拽卡片就能挪到不同列！

---

## 3. Dataview — 把笔记当数据库查

> 这是 Obsidian 最强大的插件之一，能**自动汇总**你的笔记

### 基础语法

在笔记里写一个代码块：

````markdown
```dataview
TABLE 出处, 得分
FROM "软件项目管理复习题"
WHERE 得分 < 60
SORT 得分 ASC
```
````

但这要求你的每篇笔记在 **frontmatter**（文件开头的 `---` 块）里写了 `得分:` 字段。

### 更实用的例子：列出所有作业

````markdown
```dataview
LIST
FROM "软件项目管理复习题"
WHERE contains(file.name, "作业")
SORT file.name ASC
```
````

### 给你的建议用法

在你的每份作业笔记开头的 `---` 里加上：

```yaml
---
章节: 第三章
类型: 作业
得分: 45.5
---
```

然后就能一键查所有低分章节了：

````markdown
```dataview
TABLE 章节, 得分
FROM "软件项目管理复习题"
WHERE 得分 < 60
SORT 得分 ASC
```
````

---

## 4. Obsidian Git — 自动备份

> 你已经手动 push 过了。这个插件可以**自动帮你做**这件事

### 设置

1. 打开 **设置 → Obsidian Git**
2. 找到 **"自动 Commit 和 Push"** 开关，打开
3. 设置间隔时间：**10 分钟**（默认）
4. 打开 **"拉取更新"**（如果你多设备用）

之后每隔 10 分钟，插件会自动帮你：
```
git add . → git commit → git push
```

再也不用担心笔记丢了！

---

## 5. Tasks — 任务管理

> 比 Obsidian 自带 `- [ ]` 强大多了

### 基础语法

```markdown
- [ ] 复习第六章成本估算 📅 2026-07-05 ⏫
- [ ] 做完课堂检测(3)错题整理 ✅ 2026-07-01
- [ ] 背完 WBS 相关考点 🔁 每3天
```

- `📅 2026-07-05` — 截止日期
- `⏫` — 优先级（🔺高 / ⏫中 / 🔽低）
- `✅ 2026-07-01` — 完成日期
- `🔁 每3天` — 循环任务

### 查看所有任务

````markdown
```tasks
not done
due before 2026-07-10
sort by priority
```
````

这个查询会列出所有未完成、7月10日前到期的任务，按优先级排序。

---

# 👍 第二梯队：有空学

---

## 6. Excalidraw — 手绘白板

> 画流程图、概念图、架构图

### 快速上手

1. 按 `Ctrl+P` → **"Excalidraw: New Drawing"**
2. 会自动创建一个 `.excalidraw.md` 文件
3. 左侧工具栏：
   - ✏️ 画笔画图
   - ⬜ 矩形/圆形/箭头
   - 📝 文字
   - 🎨 颜色
4. 画完后关掉，图片自动嵌入笔记

> 你的 WBS 分解、网络图、流程图都可以用它画

---

## 7. Charts + Tracker — 数据可视化

> 把你的得分数据画成图表

### Tracker 用法

如果你的笔记里有 `得分:: 45.5` 这样的字段：

````markdown
```tracker
searchType: frontmatter
searchTarget: 得分
folder: 软件项目管理复习题
datasetName: 作业得分
line:
    title: 得分趋势
    lineColor: blue
```
````

> 具体语法需要看 Tracker 的文档，但基本思路是：从笔记中提取数字 → 画出折线图/柱状图

---

## 8. Templater — 模板引擎

> 每次新建笔记时自动套用模板

### 快速创建模板

1. 创建一个文件夹 `_templates/`
2. 在里面新建 `作业模板.md`：

```markdown
---
章节: 
类型: 作业
得分: 
日期: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## 错题整理

1. 
2. 
```

3. 设置 **Templater → Template Folder Location** 为 `_templates`
4. 新建笔记时按 `Ctrl+P` → **"Templater: Insert Template"**

---

## 9. Calendar — 日记跳转

> 侧边栏日历，点日期直接打开或创建当天的日记

### 搭配

配合 **Templater** 使用效果最好：点击日历上的日期 → 自动用日记模板创建笔记。

---

## 10. Omnisearch — 超级搜索

> 比 Ctrl+Shift+F 快很多

- 按 `Ctrl+Shift+F` 打开 Omnisearch
- 支持模糊搜索、中文分词、PDF 内容搜索
- 还能搜图片里的文字（OCR）

---

# 🧊 第三梯队：以后再说

| 插件 | 什么时候用 |
|------|-----------|
| **Linter** | 笔记多了之后统一格式 |
| **Style Settings** | 想换主题/调颜色时 |
| **Icon Folder** | 想让文件夹更好看时 |
| **BRAT** | 装还在测试中的插件 |
| **Surfing** | 想在 Obsidian 里浏览网页 |
| **Citation** | 写论文引用文献时 |
| **Heatmap Calendar** | 想看学习热力图时 |

---

# 💡 我的建议学习顺序

```
第一周 → Spaced Repetition（立刻用起来复习）
       + Obsidian Git（设好自动备份）
       
第二周 → Kanban（建看板跟踪进度）
       + Tasks（管理待办）

第三周 → Dataview + Templater（笔记规范化）
       + Calendar（日记习惯）

之后 → Excalidraw + Charts + 其他
```

---

> 想学哪个插件，直接跟我说，我给你更详细的教程和实例！
