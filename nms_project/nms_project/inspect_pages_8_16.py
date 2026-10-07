import pymupdf

doc = pymupdf.open('D:/nms_project/Report_nms.pdf')
print("Total pages:", len(doc))

for i in range(7, 16):  # pages 8 to 16
    page = doc[i]
    print(f"\n==================== PAGE {i+1} ====================")
    text = page.get_text()
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    print(f"Total lines: {len(lines)}")
    print("First 5 lines:", lines[:5])
    print("Last 5 lines:", lines[-5:])
