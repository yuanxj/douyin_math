from pdf2image import convert_from_path

#images = convert_from_path(file, poppler_path=r"C:\Python\poppler\poppler-23.07.0\Library\bin")
images = convert_from_path(r"./2024_1.pdf")

for i in range(len(images)):
    # Save pages as images in the pdf
    images[i].save(f'./image_converted_2024_1_{i+1}.png', 'PNG')


