import pymupdf

doc = pymupdf.open('D:/nms_project/Report_nms.pdf')
print("Total pages in Report_nms.pdf:", len(doc))

with open('D:/nms_project/report_nms_dump.txt', 'w', encoding='utf-8') as f:
    for i in range(len(doc)):
        page = doc[i]
        f.write(f"\n==================== PAGE {i+1} ====================\n")
        f.write(f"Page rect: {page.rect}\n")
        text = page.get_text()
        f.write(text)
        f.write("\n")

print("Dumped Report_nms.pdf text to report_nms_dump.txt")
