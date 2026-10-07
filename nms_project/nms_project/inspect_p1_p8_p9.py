import pymupdf

doc = pymupdf.open('D:/nms_project/Report_nms.pdf')

print("=== PAGE 1 DETAIL ===")
p1 = doc[0]
for b in p1.get_text('dict')['blocks']:
    if 'lines' in b:
        for line in b['lines']:
            text = "".join([s['text'] for s in line['spans']]).strip()
            if text:
                s = line['spans'][0]
                print(f"y={s['origin'][1]:.1f}, x={s['origin'][0]:.1f}, font={s['font']}, size={s['size']:.1f}: '{text}'")
    elif 'image' in b:
        print("IMAGE:", b['bbox'])

print("\n=== PAGE 8 DETAIL ===")
p8 = doc[7]
for b in p8.get_text('dict')['blocks']:
    if 'lines' in b:
        for line in b['lines']:
            text = "".join([s['text'] for s in line['spans']]).strip()
            if text:
                s = line['spans'][0]
                print(f"y={s['origin'][1]:.1f}, x={s['origin'][0]:.1f}, font={s['font']}, size={s['size']:.1f}: '{text}'")
    elif 'image' in b:
        print("IMAGE:", b['bbox'])

print("\n=== PAGE 9 DETAIL ===")
p9 = doc[8]
for b in p9.get_text('dict')['blocks']:
    if 'lines' in b:
        for line in b['lines']:
            text = "".join([s['text'] for s in line['spans']]).strip()
            if text:
                s = line['spans'][0]
                print(f"y={s['origin'][1]:.1f}, x={s['origin'][0]:.1f}, font={s['font']}, size={s['size']:.1f}: '{text}'")
    elif 'image' in b:
        print("IMAGE:", b['bbox'])

print("\n=== ALL IMAGES IN REPORT_NMS.PDF ===")
for i, page in enumerate(doc):
    imgs = page.get_images()
    if imgs:
        print(f"Page {i+1} images: {imgs}")
