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
	output_file = open("index.html","a")
	output_file.write('<center>\n')
	for img in image_list:
		output_file.write('<a target="_blank" href="' + img + '">\n')
		output_file.write('<img src="' + img + '" alt="' + img + '">\n')
		output_file.write('</a>\n')
	output_file.write('</center>\n')

def main():
    print("")
    imgs = images_list()
    write_file(imgs)
    print("")

if __name__ == "__main__":
    main()
