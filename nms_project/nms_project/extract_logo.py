import pymupdf

doc = pymupdf.open('D:/nms_project/WIPRO REPORT ff.pdf')
p1 = doc[0]
for img_info in p1.get_images():
    xref = img_info[0]
    base_img = doc.extract_image(xref)
    img_bytes = base_img['image']
    img_ext = base_img['ext']
    with open(f'D:/nms_project/college_logo.{img_ext}', 'wb') as f:
        f.write(img_bytes)
    print(f"Extracted logo: college_logo.{img_ext}, size: {base_img['width']}x{base_img['height']}")

for b in p1.get_text('dict')['blocks']:
    if 'image' in b:
        print("Image bbox on Page 1:", b['bbox'])
