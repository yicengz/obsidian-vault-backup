# -*- coding: utf-8 -*-
"""v2：在三张内页留白处排金句，沿用封面的宋体暖棕风格"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE = Path("/Users/yiceng/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/内容创作/小红书-异常值")
FONT = "/System/Library/Fonts/Songti.ttc"
INK = (74, 58, 44)          # 暖墨棕，与封面一致
INK_SOFT = (109, 90, 71)

def draw_tracked(draw, cx, y, text, font, fill, tracking=0):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + tracking

def add_quote(src, dst, lines, cx, y_top, size=62, tracking=8, line_gap=42):
    im = Image.open(src).convert("RGB")
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT, size)
    y = y_top
    for line in lines:
        draw_tracked(d, cx, y, line, font, INK, tracking=tracking)
        y += size + line_gap
    im.save(dst, quality=95)
    print("done ->", dst)

# 02 小桥流水：顶部天空留白，居中
add_quote(
    BASE / "发布-02-搭桥.png",
    BASE / "发布v2-02-搭桥.png",
    ["数仓不是搬砖，", "而是「搭桥」"],
    cx=624, y_top=170,
)

# 03 灯下笔记：枝叶与灯杆之间的素墙（原图坐标 x≈470~1000, y≈500~800）
add_quote(
    BASE / "发布-03-超纲思考.png",
    BASE / "发布v2-03-超纲思考.png",
    ["信任，始于一次", "「超纲」的思考"],
    cx=725, y_top=560, size=56, tracking=6, line_gap=36,
)

# 04 咖啡闲聊：右上大面积奶白墙面
add_quote(
    BASE / "发布-04-咖啡闲聊.png",
    BASE / "发布v2-04-咖啡闲聊.png",
    ["异常值，也是", "与人连接的姿态"],
    cx=790, y_top=180,
)
