import pymupdf

doc = pymupdf.open('D:/nms_project/Report_nms.pdf')
p3 = doc[2]

with open('D:/nms_project/p3_spans.txt', 'w', encoding='utf-8') as f:
    for b in p3.get_text('dict')['blocks']:
        if 'lines' in b:
            for line in b['lines']:
                for s in line['spans']:
                    f.write(f"x={s['origin'][0]:.2f}, y={s['origin'][1]:.2f}, font={s['font']}, size={s['size']:.2f}, text='{s['text']}'\n")

print("Dumped p3_spans.txt")
