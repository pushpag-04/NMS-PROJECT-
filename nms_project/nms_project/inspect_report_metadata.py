import pymupdf

doc = pymupdf.open('D:/nms_project/Report_nms.pdf')
print("Metadata:", doc.metadata)

for i in range(len(doc)):
    page = doc[i]
    fonts = set()
    for b in page.get_text('dict')['blocks']:
        if 'lines' in b:
            for line in b['lines']:
                for s in line['spans']:
                    fonts.add((s['font'], s['size']))
    print(f"Page {i+1} rect: {page.rect}, fonts: {fonts}")
