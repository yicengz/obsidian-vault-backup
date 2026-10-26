# rank5 处理记录

- 下载: curl -sL -A "Mozilla/5.0" -o rank5_金钱心理学.m4a <manifest audio_url>; 校验 65964041 字节一致
- 原生文件 drive +upload 同样因 multipart 临时 token TTL 过期失败
- 转码: ffmpeg -y -i rank5.m4a -ac 1 -ar 16000 -b:a 48k rank5_small.m4a (26841047 字节)
- 上传: lark-cli drive +upload --file rank5_small.m4a --name 听懂涨声_20260903_金钱心理学.m4a
  -> file_token NCDHbrHyxoPMR1xM0rdcrel4nsd
- 建妙记: lark-cli minutes +upload --file-token NCDHbrHyxoPMR1xM0rdcrel4nsd
  -> minute_token obcntp84z2de947r1475xcz8
- 拉产物: lark-cli minutes +detail --minute-tokens obcntp84z2de947r1475xcz8 --summary --chapter --keyword --transcript --overwrite --output-dir ...
- 说话人判定: Speaker1=主播杨天楠，Speaker2=嘉宾茱莉亚
- 逐字校验: 自写脚本对比 157/157 段 0 差异
- verifier-hub: rubric.check-file-format passed; text.must-contain 6/6

注意: 送入飞书妙记的是语音压缩副本，未开展原音频 vs 压缩音频的转写准确率对照；ASR 文字可能有误，原稿 transcript.txt 已保留。
