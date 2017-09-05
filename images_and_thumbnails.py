import os

def images_list():
	img_exts = [".gif",".jpg",".png"]
	imgs = []
	for i in os.listdir("./"):
		if i[-4:] in img_exts:
			imgs.append(i)
			print(i+" added to HTML file")
	return(imgs)

def write_file(image_list):
	output_file = open("index.html","w")
	for img in image_list:
		output_file.write('<a target="_blank" href="' + img + '">\n')
		output_file.write('<img src="' + img + '" alt="' + img + '">\n')
		output_file.write('</a>\n')
imgs = images_list()
print(imgs)
write_file(imgs)
