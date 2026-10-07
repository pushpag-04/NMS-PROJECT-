import pymupdf

doc = pymupdf.open('D:/nms_project/WIPRO REPORT ff.pdf')

for pno in [7, 10, 12, 15]:  # 0-indexed: pages 8, 11, 13, 16
    page = doc[pno]
    print(f"\n================ PAGE {pno+1} TABLE & DRAWINGS ================")
    drawings = page.get_drawings()
    print(f"Total drawings on page {pno+1}: {len(drawings)}")
    for d in drawings[:10]:
        print("Drawing:", d['type'], "rect:", d['rect'], "fill:", d.get('fill'), "color:", d.get('color'))
    
    # print text in table area
    for b in page.get_text('dict')['blocks']:
        if 'lines' in b:
            for line in b['lines']:
                for s in line['spans']:
                    if 'Table' in s['text'] or 'Class' in s['text'] or 'Technology' in s['text'] or 'Attack' in s['text'] or 'Criterion' in s['text']:
                        print(f"Text span: '{s['text']}' at y={s['origin'][1]:.1f}, x={s['origin'][0]:.1f}, font={s['font']}, size={s['size']:.1f}")
