import pymupdf

doc = pymupdf.open('D:/nms_project/WIPRO REPORT ff.pdf')
print("Total pages in WIPRO REPORT ff.pdf:", len(doc))

for i in range(len(doc)):
    page = doc[i]
    print(f"\n================ PAGE {i+1} ================")
    print("Page rect:", page.rect)
    blocks = page.get_text('dict')['blocks']
    for b in blocks:
        if 'lines' in b:
            for line in b['lines']:
                line_text = "".join([s['text'] for s in line['spans']]).strip()
                if line_text:
                    s0 = line['spans'][0]
                    print(f"[{s0['origin'][0]:.1f}, {s0['origin'][1]:.1f}] ({s0['font']}, {s0['size']:.1f}pt, col:{s0['color']}): {line_text[:80]}")
        elif 'image' in b:
            print(f"IMAGE: bbox={b['bbox']}, width={b['width']}, height={b['height']}")
