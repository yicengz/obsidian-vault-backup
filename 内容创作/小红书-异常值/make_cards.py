# -*- coding: utf-8 -*-
"""裁剪 AI 水印 + 封面排字"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE = Path("/Users/yiceng/Library/Mobile Documents/iCloud~md~obsidian/Documents/yiceng/内容创作/小红书-异常值")
W, H = 1248, 1664
CROP_BOTTOM = 80  # 去掉左下角「AI生成」水印

FONT = "/System/Library/Fonts/Songti.ttc"

def clean(src: Path, dst: Path):
    im = Image.open(src).convert("RGB")
    im = im.crop((0, 0, im.width, im.height - CROP_BOTTOM))
    im = im.resize((W, H), Image.LANCZOS)
    im.save(dst, quality=95)
    return im

def draw_tracked(draw, cx, y, text, font, fill, tracking=0):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + tracking

# 1) 四张图去水印
files = {
    "01-封面-窗边书桌.png": "发布-01-封面.png",
    "02-内页-小桥流水.png": "发布-02-搭桥.png",
    "03-内页-灯下笔记.png": "发布-03-超纲思考.png",
    "04-内页-咖啡闲聊.png": "发布-04-咖啡闲聊.png",
}
imgs = {}
for src, dst in files.items():
    imgs[dst] = clean(BASE / src, BASE / dst)
    print("cleaned ->", dst)

# 2) 封面排字
cover = imgs["发布-01-封面.png"].copy()
d = ImageDraw.Draw(cover)
ink = (74, 58, 44)        # 暖墨棕
ink_soft = (109, 90, 71)

title_font = ImageFont.truetype(FONT, 84)
sub_font = ImageFont.truetype(FONT, 40)
quote_font = ImageFont.truetype(FONT, 34)

draw_tracked(d, W / 2, 150, "别怕做一点「不正」的事", title_font, ink, tracking=10)
# 分隔小短线
d.line([(W / 2 - 40, 300), (W / 2 + 40, 300)], fill=ink_soft, width=3)
draw_tracked(d, W / 2, 330, "一个数仓工程师的成长笔记", sub_font, ink_soft, tracking=6)

cover.save(BASE / "发布-01-封面.png", quality=95)
print("cover titled -> 发布-01-封面.png")
