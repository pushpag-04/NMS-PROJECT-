import pymupdf

doc = pymupdf.open('D:/nms_project/WIPRO REPORT ff.pdf')

print("=== PAGE 1 DETAIL ===")
p1 = doc[0]
for b in p1.get_text('dict')['blocks']:
    if 'lines' in b:
        for line in b['lines']:
            text = "".join([s['text'] for s in line['spans']]).strip()
            if text:
                s = line['spans'][0]
                print(f"Text: '{text}' at y={s['origin'][1]:.1f}, x={s['origin'][0]:.1f}, font={s['font']}, size={s['size']:.1f}")
    elif 'image' in b:
        print(f"IMAGE bbox: {b['bbox']}")

print("\n=== PAGE NUMBERS ACROSS PAGES ===")
for i in range(len(doc)):
    page = doc[i]
    # Check top and bottom 100 points
    top_texts = []
    bottom_texts = []
    for b in page.get_text('dict')['blocks']:
        if 'lines' in b:
            for line in b['lines']:
                for s in line['spans']:
                    y = s['origin'][1]
                    t = s['text'].strip()
                    if t:
                        if y < 100:
                            top_texts.append((t, s['origin'][0], y))
                        elif y > 750:
                            bottom_texts.append((t, s['origin'][0], y))
    print(f"Page {i+1}: Top={top_texts}, Bottom={bottom_texts}")
