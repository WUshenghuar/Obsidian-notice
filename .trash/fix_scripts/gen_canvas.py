#!/usr/bin/env python3
"""Generate a beautiful .canvas knowledge map for 软件项目管理"""
import json, os

VAULT = r"D:\Users\雾盛华\Documents\Obsidian Vault"
OUTPUT = os.path.join(VAULT, "软件项目管理复习题", "软件项目管理·知识图谱.canvas")

def nid(n):
    """Generate a deterministic 16-char hex ID"""
    return f"n{n:04d}{'0'*12}"[:16]

def eid(n):
    return f"e{n:04d}{'0'*12}"[:16]

def gid(n):
    return f"g{n:04d}{'0'*12}"[:16]

# ====== COLOR PALETTE ======
# 1=Red, 2=Orange, 3=Yellow, 4=Green, 5=Cyan, 6=Purple
C_BASE = "1"       # 项目管理基础 - Red
C_LIFECYCLE = "2"  # 生存期模型 - Orange
C_REQ = "3"        # 需求管理 - Yellow
C_WBS = "4"        # WBS - Green
C_COST = "5"       # 成本估算 - Cyan
C_SCHED = "6"      # 进度管理 - Purple
C_QUAL = "1"       # 质量管理 - Red variant
C_RISK = "2"       # 风险与采购 - Orange
C_TEAM = "3"       # 团队与沟通 - Yellow
C_AGILE = "4"      # 敏捷方法 - Green
C_FILE = "5"       # 文件链接 - Cyan

nodes = []
edges = []
idx = 0
e_idx = 0

def add_text(x, y, w, h, text, color=None, group=None):
    global idx
    idx += 1
    node = {
        "id": nid(idx),
        "type": "text",
        "x": x, "y": y,
        "width": w, "height": h,
        "text": text
    }
    if color:
        node["color"] = color
    nodes.append(node)
    return node["id"]

def add_file(x, y, w, h, filepath, color=None):
    global idx
    idx += 1
    node = {
        "id": nid(idx),
        "type": "file",
        "x": x, "y": y,
        "width": w, "height": h,
        "file": filepath
    }
    if color:
        node["color"] = color
    nodes.append(node)
    return node["id"]

def add_group(x, y, w, h, label, color):
    global idx
    idx += 1
    node = {
        "id": gid(idx),
        "type": "group",
        "x": x, "y": y,
        "width": w, "height": h,
        "label": label,
        "color": color
    }
    nodes.append(node)
    return node["id"]

def add_edge(frm, to, label=None, color=None, fside=None, tside=None):
    global e_idx
    e_idx += 1
    edge = {
        "id": eid(e_idx),
        "fromNode": frm,
        "toNode": to,
        "toEnd": "arrow"
    }
    if label:
        edge["label"] = label
    if color:
        edge["color"] = color
    if fside:
        edge["fromSide"] = fside
    if tside:
        edge["toSide"] = tside
    edges.append(edge)

# ======================================================================
# LAYOUT
# Canvas size: ~2600 x 1800
# Column width: ~600, Row height: ~500
# ======================================================================

# ---- ROW 1: 项目管理基础 | 生存期模型 | 需求管理 | WBS ----

# Group 1: 项目管理基础 (x=20, y=20)
g1 = add_group(20, 20, 580, 440, "📌 项目管理基础", C_BASE)

add_text(40, 60, 540, 30, "## 项目的特征", C_BASE)
add_text(40, 95, 540, 25, "🔹 **临时性** — 明确起止")
add_text(40, 120, 540, 25, "🔹 **独特性** — 创造唯一产品")
add_text(40, 145, 540, 25, "🔹 **渐进明细** — 逐步细化")
add_text(40, 170, 540, 25, "🔹 ❌ 重复性（这是日常运作）")

add_text(40, 210, 540, 30, "## 软件项目特殊性", C_BASE)
add_text(40, 245, 540, 25, "⚡变更频繁 | 🔄渐进明细")
add_text(40, 270, 540, 25, "💿逻辑实体 | 🔗相互作用系统")

add_text(40, 310, 540, 30, "## 核心概念", C_BASE)
add_text(40, 345, 540, 25, "📦 **项目组合** → 战略目标")
add_text(40, 370, 540, 25, "📚 **项目集** → 相互关联项目")
add_text(40, 395, 540, 25, "🎯 **项目** → 临时·独特·渐进明细")


# Group 2: 生存期模型 (x=620, y=20)
g2 = add_group(620, 20, 640, 440, "🔄 生存期模型", C_LIFECYCLE)

add_text(640, 60, 300, 30, "## 预测型", C_LIFECYCLE)
add_text(640, 95, 300, 25, "🌊 **瀑布模型** — 线性顺序")
add_text(640, 120, 300, 25, "✅ 适合：需求明确·短期项目")
add_text(640, 145, 300, 25, "✅ V模型 — 测试对应开发")
add_text(640, 170, 300, 25, "✅ 适合：安全/性能严格项目")

add_text(950, 60, 300, 30, "## 迭代·增量", C_LIFECYCLE)
add_text(950, 95, 300, 25, "🔄 **迭代模型** — 逐步完善")
add_text(950, 120, 300, 25, "📦 **增量模型** — 分阶段交付")

add_text(640, 215, 600, 30, "## 敏捷型", C_LIFECYCLE)
add_text(640, 250, 290, 25, "🏃 **Scrum** — 冲刺迭代")
add_text(640, 275, 290, 25, "💻 **XP** — 结对编程/TDD")
add_text(640, 300, 290, 25, "📋 **看板** — 限制在制品")
add_text(640, 325, 290, 25, "🔧 **DevOps** — 开发运维一体")

add_text(950, 250, 290, 50, "**敏捷四大价值观：**\n个体互动 > 流程工具\n工作软件 > 详尽文档\n客户合作 > 合同谈判\n响应变化 > 遵循计划", C_LIFECYCLE)

add_text(640, 370, 600, 30, "## Scrum 三核心角色", C_LIFECYCLE)
add_text(640, 405, 600, 25, "👤 产品负责人(PO) → 👤 Scrum Master → 👥 开发团队")


# Group 3: 需求管理 (x=1280, y=20)
g3 = add_group(1280, 20, 580, 440, "📋 需求管理", C_REQ)

add_text(1300, 60, 540, 30, "## 需求管理5过程", C_REQ)
add_text(1300, 95, 540, 25, "① 需求获取 → ② 需求分析")
add_text(1300, 120, 540, 25, "③ 需求规格编写 → ④ 需求验证")
add_text(1300, 145, 540, 25, "⑤ 需求变更管理")

add_text(1300, 185, 540, 30, "## 变更控制流程", C_REQ)
add_text(1300, 220, 540, 25, "申请（需求方）→ 评估 → 审批")
add_text(1300, 245, 540, 25, "→ 实施 → 验证")
add_text(1300, 270, 540, 25, "❗ 非所有变更需CCB批准")

add_text(1300, 310, 540, 30, "## 建模方法", C_REQ)
add_text(1300, 345, 540, 25, "**传统：** 原型法 / DFD / UML")
add_text(1300, 370, 540, 25, "**敏捷：** Story / Backlog")
add_text(1300, 395, 540, 25, "**UML需求视图：** 用例+顺序+状态+活动")


# Group 4: WBS (x=1880, y=20)
g4 = add_group(1880, 20, 580, 440, "🧩 WBS 任务分解", C_WBS)

add_text(1900, 60, 540, 30, "## WBS = Work Breakdown Structure", C_WBS)
add_text(1900, 95, 540, 50, "对项目**由粗到细**的分解过程\n面向**交付成果**，定义**项目范围**")

add_text(1900, 160, 540, 30, "## 分解方法", C_WBS)
add_text(1900, 195, 540, 25, "📐 **自顶向下** — 整体→局部")
add_text(1900, 220, 540, 25, "📐 **自底向上** — 局部→整体")
add_text(1900, 245, 540, 25, "📐 **类比法 / 模板参照法**")

add_text(1900, 285, 540, 30, "## 关键要点", C_WBS)
add_text(1900, 320, 540, 25, "✅ 最低层 = **工作包**")
add_text(1900, 345, 540, 25, "✅ 工作包由**唯一主体**负责")
add_text(1900, 370, 540, 25, "✅ 表达式：图表/清单/树形")
add_text(1900, 395, 540, 25, "❌ 矩阵式不是WBS表达形式")


# ---- ROW 2: 成本估算 | 进度管理 | 质量管理 | 风险/采购 ----

# Group 5: 成本估算 (x=20, y=480)
g5 = add_group(20, 480, 640, 460, "💰 成本估算", C_COST)

add_text(40, 520, 300, 30, "## 估算方法", C_COST)
add_text(40, 555, 300, 25, "📊 **类比估算** — 自上而下")
add_text(40, 580, 300, 25, "📊 **自下而上** — 最细粒度汇总")
add_text(40, 605, 300, 25, "📊 **参数估算 / 专家估算**")
add_text(40, 630, 300, 25, "📊 **三点估算(PERT)**")

add_text(350, 520, 290, 30, "## 功能点 IFPUG", C_COST)
add_text(350, 555, 290, 50, "**FP = UFC × TCF**\nUFC=未调整功能点计数\nTCF=技术复杂度因子")
add_text(350, 615, 290, 50, "5类功能项：\nEI / EO / EQ / ILF / EIF")
add_text(350, 675, 290, 25, "✅ 与编程语言和技术**无关**")

add_text(40, 670, 290, 30, "## 关键公式", C_COST)
add_text(40, 705, 290, 50, "**定额估算：**\nT = Q / (R×S)")
add_text(40, 760, 290, 50, "**PERT期望值：**\nE = (O+4M+P) / 6\nδ = (P-O) / 6")

add_text(350, 720, 290, 50, "**单位换算：**\n1人月 = 22人天 = 176工时")
add_text(350, 780, 290, 50, "**自制vs购买：**\n平衡点=(自制-购买初始)\n÷(购买-自制月维护)")


# Group 6: 进度管理 (x=680, y=480)
g6 = add_group(680, 480, 620, 460, "📅 进度管理", C_SCHED)

add_text(700, 520, 580, 30, "## 网络图", C_SCHED)
add_text(700, 555, 280, 60, "**ADM（双代号）**\n箭线=活动\n节点=代号/事件", C_SCHED)
add_text(990, 555, 290, 60, "**PDM（单代号）**\n节点=活动\n箭线=逻辑关系", C_SCHED)

add_text(700, 630, 580, 30, "## 关键概念", C_SCHED)
add_text(700, 665, 580, 25, "⭐ **关键路径** — 决定最短工期")
add_text(700, 690, 580, 25, "⏳ **虚活动** — 不消耗资源/时间")
add_text(700, 715, 580, 25, "📈 **甘特图** — 条形图·显示起止时间")

add_text(700, 755, 580, 30, "## 时间压缩法", C_SCHED)
add_text(700, 790, 580, 25, "⚡ **赶工** — 增加资源")
add_text(700, 815, 580, 25, "⚡ **快速跟进** — 并行执行")
add_text(700, 840, 580, 25, "📊 **燃尽图** — 剩余工作量变化")


# Group 7: 质量管理 (x=1320, y=480)
g7 = add_group(1320, 480, 540, 460, "✅ 质量管理", C_QUAL)

add_text(1340, 520, 500, 30, "## 质量成本", C_QUAL)
add_text(1340, 555, 500, 25, "**质量成本 = 预防成本 + 缺陷成本**")
add_text(1340, 590, 500, 30, "## 两大过程", C_QUAL)
add_text(1340, 625, 500, 25, "🔍 **质量保证** — 产品审计+过程审计")
add_text(1340, 650, 500, 25, "🔍 **质量控制**")
add_text(1340, 685, 500, 30, "## 敏捷质量", C_QUAL)
add_text(1340, 720, 500, 25, "📌 **测试左移** — 早期介入测试")
add_text(1340, 745, 500, 25, "📌 **测试右移** — 生产环境测试")
add_text(1340, 780, 500, 30, "## 人员角色", C_QUAL)
add_text(1340, 815, 500, 25, "👤 **业务分析师(BA)** — 需求分析转化")
add_text(1340, 840, 500, 25, "👤 **产品负责人(PO)** — 定义需求优先级")
add_text(1340, 865, 500, 25, "👤 **项目经理(PM)** — 计划与执行")


# Group 8: 风险与采购 (x=1880, y=480)
g8 = add_group(1880, 480, 580, 460, "⚠️ 风险与采购", C_RISK)

add_text(1900, 520, 540, 30, "## 风险三要素", C_RISK)
add_text(1900, 555, 540, 25, "**风险事件 × 发生概率 × 影响**")
add_text(1900, 590, 540, 30, "## 风险评估", C_RISK)
add_text(1900, 625, 540, 25, "📊 **定性** — 主观评估")
add_text(1900, 650, 540, 60, "📊 **定量** — 盈亏平衡/模拟\n访谈/决策树/敏感性分析")

add_text(1900, 725, 540, 30, "## 应对策略", C_RISK)
add_text(1900, 760, 540, 25, "🛡️ **回避** — 放弃高风险方案")
add_text(1900, 790, 540, 25, "📦 **采购** — 从外部获取/服务")


# ---- ROW 3: 团队与沟通 + 敏捷 + 文件链接 ----

# Group 9: 团队与沟通 (x=20, y=960)
g9 = add_group(20, 960, 640, 400, "👥 团队与沟通", C_TEAM)

add_text(40, 1000, 300, 30, "## 组织结构", C_TEAM)
add_text(40, 1035, 300, 25, "🏢 **职能型** — 资源集中")
add_text(40, 1060, 300, 25, "🏗️ **项目型** — 项目为中心")
add_text(40, 1085, 300, 25, "🔀 **矩阵型** — 混合模式")

add_text(350, 1000, 290, 30, "## 沟通管理", C_TEAM)
add_text(350, 1035, 290, 25, "📢 渠道数 = n(n-1)/2")
add_text(350, 1060, 290, 25, "🔄 20人 → 190条渠道")
add_text(350, 1085, 290, 25, "💬 复杂问题→**口头沟通**")

add_text(40, 1130, 600, 30, "## 敏捷团队", C_TEAM)
add_text(40, 1165, 600, 25, "🏃 强调 **自组织** 形式团队")
add_text(40, 1190, 600, 25, "📋 **Epic → Story → Task** 分解层次")
add_text(40, 1215, 600, 25, "📖 **用户故事**：角色 + 功能 + 价值")
add_text(40, 1240, 600, 25, "📝 **验收标准**写在故事卡**背面**")
add_text(40, 1265, 600, 25, "📊 **Sprint Backlog** = 细化可完成Story")
add_text(40, 1290, 600, 25, "🤖 **AI赋能**：计划/估算/跟踪/控制")


# Group 10: 易错提醒 (x=680, y=960)
g10 = add_group(680, 960, 620, 400, "⚠️ 高频易错提醒", C_FILE)

add_text(700, 1000, 580, 25, "❌ 瀑布模型不适合短期项目 → ✅ **适合**")
add_text(700, 1030, 580, 25, "❌ 敏捷模型=预测+迭代混合 → ✅ 不是")
add_text(700, 1060, 580, 25, "❌ 功能点与编程语言有关 → ✅ **无关**")
add_text(700, 1090, 580, 25, "❌ 项目是为了创造重复产品 → ✅ **唯一**")
add_text(700, 1120, 580, 25, "❌ WBS是对项目由细到粗 → ✅ 由粗到细")
add_text(700, 1150, 580, 25, "❌ 所有变更需CCB批准 → ✅ 部分PM可定")
add_text(700, 1180, 580, 25, "❌ WBS最低层=分到个人 → ✅ **工作包**")
add_text(700, 1210, 580, 25, "❌ PDM箭线=活动 → ✅ ADM才是")
add_text(700, 1240, 580, 25, "❌ 类比估算=自下而上 → ✅ **自上而下**")
add_text(700, 1270, 580, 25, "❌ DevOps=自动化工具 → ✅ **文化+流程+工具**")
add_text(700, 1300, 580, 25, "❌ 甘特图显示关键路径 → ✅ 网络图显示")


# File links (bottom row)
g11 = add_group(1320, 960, 1140, 400, "📁 对应源文件", C_FILE)

files = [
    ("作业·第三章 生存期模型", "软件项目管理复习题/作业20260319第三章书后习题.md", 1340, 1000),
    ("作业·第四五章 需求/WBS", "软件项目管理复习题/作业20260402第四和五章书后习题.md", 1340, 1060),
    ("作业·第六章 成本估算", "软件项目管理复习题/作业20260416第六章书后习题.md", 1340, 1120),
    ("作业·第七章 进度管理", "软件项目管理复习题/作业20260514第七章书后习题.md", 1340, 1180),
    ("作业·八九章 质量管理", "软件项目管理复习题/作业20260609第八章和第九章书后习题.md", 1340, 1240),
    ("作业·第十章 团队沟通", "软件项目管理复习题/作业20260611第十章书后习题.md", 1340, 1300),
    ("作业·十一二章 风险采购", "软件项目管理复习题/作业20260618第十一章和第十二章书后习题.md", 1700, 1000),
    ("课堂检测(1) 综合", "软件项目管理复习题/课堂检测(1).md", 1700, 1060),
    ("课堂检测(2) 综合", "软件项目管理复习题/课堂检测(2).md", 1700, 1120),
    ("课堂检测(3) 综合", "软件项目管理复习题/课堂检测(3).md", 1700, 1180),
    ("简答题汇总", "软件项目管理复习题/软件项目管理简答题.md", 1700, 1240),
    ("重点知识图谱(文本版)", "软件项目管理复习题/软件项目管理·重点知识图谱.md", 1700, 1300),
]

for label, path, fx, fy in files:
    add_file(fx, fy, 310, 50, path, C_FILE)


# ====== EDGES ======

# Connect related concepts across groups
# 生存期模型 → 敏捷 → 团队
n_scrum = [n for n in nodes if "Scrum 三核心" in n.get("text","")][0]["id"]
n_agile_team = [n for n in nodes if "自组织" in n.get("text","")][0]["id"]
add_edge(n_scrum, n_agile_team, "关联", C_AGILE, "bottom", "top")

# 需求管理 → WBS
n_req_chg = [n for n in nodes if "变更控制" in n.get("text","")][0]["id"]
n_wbs = [n for n in nodes if "WBS = Work" in n.get("text","")][0]["id"]
add_edge(n_req_chg, n_wbs, "范围管理", "3", "bottom", "top")

# 成本估算 → 进度管理
n_pert = [n for n in nodes if "PERT期望" in n.get("text","")][0]["id"]
n_cpm = [n for n in nodes if "关键路径" in n.get("text","")][0]["id"]
add_edge(n_pert, n_cpm, "估算联动", C_COST, "bottom", "top")

# 成本估算中的 1人月=22人天 → 定额估算
n_unit = [n for n in nodes if "人月" in n.get("text","")][0]["id"]
n_quote = [n for n in nodes if "定额估算" in n.get("text","")][0]["id"]
add_edge(n_unit, n_quote, "关联", C_COST, "right", "left")

# ====== WRITE ======
canvas = {
    "nodes": nodes,
    "edges": edges
}

with open(OUTPUT, 'w', encoding='utf-8') as f:
    json.dump(canvas, f, ensure_ascii=False, indent=2)

print(f"✅ Canvas generated: {OUTPUT}")
print(f"   Nodes: {len(nodes)}, Edges: {len(edges)}")
