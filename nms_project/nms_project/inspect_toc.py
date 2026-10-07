import pymupdf

doc = pymupdf.open('D:/nms_project/Report_nms.pdf')

for pno in [2, 3]:  # pages 3 and 4
    page = doc[pno]
    print(f"\n==================== PAGE {pno+1} DETAIL ====================")
    for b in page.get_text('dict')['blocks']:
        if 'lines' in b:
            for line in b['lines']:
                for s in line['spans']:
                    print(f"y={s['origin'][1]:.1f}, x={s['origin'][0]:.1f}, font={s['font']}, size={s['size']:.1f}: '{s['text']}'")
