import re, sys
sys.path.insert(0,'/tmp/podcast_upload')
from assemble import parse, fmt_ts

def verify(transcript, md_path, name_map):
    blocks = parse(transcript)
    md = open(md_path, encoding='utf-8').read()
    lines = md.split('\n')
    # collect ### blocks
    hdr = re.compile(r'^### (.+?) @ (\d\d:\d\d(?::\d\d)?)$')
    md_blocks = []
    i = 0
    while i < len(lines):
        m = hdr.match(lines[i])
        if m:
            # text until next ### or ## or EOF
            j = i+1
            buf = []
            while j < len(lines) and not lines[j].startswith('### ') and not lines[j].startswith('## '):
                buf.append(lines[j])
                j += 1
            text = '\n'.join(buf).strip()
            md_blocks.append((m.group(1), m.group(2), text))
            i = j
        else:
            i += 1

    print(f"ORIG blocks={len(blocks)}  MD ### blocks={len(md_blocks)}")
    assert len(blocks)==len(md_blocks), f"MISMATCH count {len(blocks)} vs {len(md_blocks)}"
    bad = 0
    for idx,(b,(name,ts,text)) in enumerate(zip(blocks, md_blocks)):
        exp_name = name_map[b['spk']]
        exp_ts = fmt_ts(b['start_ms'])
        if name != exp_name:
            print(f"[NAME] para{idx}: md={name} expect={exp_name}"); bad+=1
        if ts != exp_ts:
            print(f"[TS] para{idx}: md={ts} expect={exp_ts}"); bad+=1
        if text != b['text'].strip():
            print(f"[TEXT] para{idx} mismatch")
            print(f"  MD:  {text[:80]!r}")
            print(f"  ORIG:{b['text'].strip()[:80]!r}")
            bad+=1
    # chapters
    ch_body = re.findall(r'^## (\d\d:\d\d(?::\d\d)?) (.+)$', md, re.M)
    ch_toc = re.findall(r'^- \[\[#(\d\d:\d\d(?::\d\d)?) (.+?)\|', md, re.M)
    print(f"BODY chapters={len(ch_body)}  TOC links={len(ch_toc)}")
    assert ch_body == ch_toc, "chapter toc/body mismatch"
    # quote line present
    assert md.startswith('---\n'), "no frontmatter"
    print("BAD=",bad)
    return bad

if __name__=='__main__':
    t, m, nm = sys.argv[1], sys.argv[2], eval(sys.argv[3])
    sys.exit(1 if verify(t,m,nm) else 0)
