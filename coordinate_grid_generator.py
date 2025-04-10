from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def create_coordinate_grid_pdf(filename="coordinate_grid.pdf"):
    width, height = A4
    c = canvas.Canvas(filename, pagesize=A4)
    
    c.setFont("Helvetica", 6)

    for x in range(0, int(width), 20):
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.line(x, 0, x, height)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawString(x + 2, 5, str(x))

    for y in range(0, int(height), 20):
        c.setStrokeColorRGB(0.8, 0.8, 0.8)
        c.line(0, y, width, y)
        c.setFillColorRGB(0.3, 0.3, 0.3)
        c.drawString(2, y + 2, str(y))

    c.save()

create_coordinate_grid_pdf()
