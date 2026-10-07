import pymupdf, os

for fname in os.listdir('D:/nms_project'):
    if fname.endswith('.pdf'):
        doc = pymupdf.open(os.path.join('D:/nms_project', fname))
        print(f"=== {fname} ({len(doc)} pages) ===")
        for i, page in enumerate(doc):
            imgs = page.get_images()
            if imgs:
                print(f"  Page {i+1}: {len(imgs)} images: {imgs}")
