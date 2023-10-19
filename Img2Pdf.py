import cv2
from PIL import Image
from reportlab.pdfgen import canvas
pdf_path = ""

def Img2Pdf(filename:str,imgList:list):
    global pdf_path
    img_list = []
    for img in imgList:
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        img_list.append(img_pil)

    # 計算整體尺寸，我們使用最寬的圖片作為寬度，並將所有圖片的高度加在一起作為總高度
    width = max(img.size[0] for img in img_list)
    height = sum(img.size[1] for img in img_list)



    # 使用reportlab保存圖片為PDF
    c = canvas.Canvas(pdf_path, pagesize=(width, height))
    y_position = height  # 從頂部開始放置圖片

    for img in img_list:
        y_position -= img.size[1]
        c.drawInlineImage(img, 0, y_position)

    c.showPage()
    c.save()




