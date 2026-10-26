# rank9 处理记录

- 下载: curl -sL -A "Mozilla/5.0" -o rank9_固收加.m4a <manifest audio_url>; 校验 70645753 字节一致
- 原生文件 lark-cli drive +upload 连续多次 multipart 上传后报 "parse temporary token from Authorization failed: temporary token expired"（5-7 分钟上传后失败，未成功落盘）
- 转码: ffmpeg -y -i rank9.m4a -ac 1 -ar 16000 -b:a 48k rank9_small.m4a (28707167 字节)
- 上传: lark-cli drive +upload --file rank9_small.m4a --name 听懂涨声_20260803_固收加.m4a
  -> file_token IH1JbbFjtoWVGDxumMrcxeUdnLb
- 建妙记: lark-cli minutes +upload --file-token IH1JbbFjtoWVGDxumMrcxeUdnLb
  -> minute_token obcntp774dzqpb8o3xfn317m
- 拉产物: lark-cli minutes +detail --minute-tokens obcntp774dzqpb8o3xfn317m --summary --chapter --keyword --transcript --overwrite --output-dir ...
- 说话人判定: Speaker1+Speaker2 均为主播杨天楠（串台双录制位被 ASR 拆分），Speaker3=嘉宾杨亚钊
- 逐字校验: 自写脚本对比 136/136 段 0 差异
- verifier-hub: rubric.check-file-format passed; text.must-contain 6/6

注意: 送入飞书妙记的是语音压缩副本，未开展原音频 vs 压缩音频的转写准确率对照；ASR 文字可能有误，原稿 transcript.txt 已保留。
