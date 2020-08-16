from PIL import Image

image = Image.open("C:\\Users\\srcLegend\\Desktop\\PDF\\06.jpg")
#appendList = [Image.open("C:\\Users\\srcLegend\\Desktop\\PDF1.jpg"),
#			  Image.open("C:\\Users\\srcLegend\\Desktop\\PDF1.jpg"),
#			  Image.open("C:\\Users\\srcLegend\\Desktop\\PDF1.jpg"),
#			  Image.open("C:\\Users\\srcLegend\\Desktop\\PDF1.jpg"),]
pdf = "C:\\Users\\srcLegend\\Desktop\\PDF\\06.pdf"

#image.save(pdf, "PDF", resolution = 100.0, save_all = True, append_images = appendList)
image.save(pdf, "PDF", resolution = 100.0, save_all = True)
