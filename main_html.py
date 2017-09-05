def start_thru_head():
    output_file = open("index.html","w")

    #opening tags
    output_file.write('<!DOCTYPE html>\n')
    output_file.write('<html>\n')
    output_file.write('<head>\n')

    #title
    output_file.write('<title>'+"need to implement functionality"+'</title>\n')

    #close the <head> don't forget to call the ending function to close the <html> tag
    output_file.write('</head>\n') 

    output_file.close()

def body_thru_end():
    output_file = open("index.html","a")
    
    #opening <body> tag
    output_file.write('<body>\n')

    output_file.write('<center><h1>Local River Log Entry ' + '' + ' how to do date?</h1></center>\n')
    output_file.write('<hr width="75%" />\n')

    output_file.write('<center><h2>'+"your first heading here"+'</h2></center>\n')
    import_body_text(output_file)

    output_file.write('<center><h2>Pictures, Maps, Et Cetera</h2></center>\n')
    #use the i&t shit here

    #close <body> and <html> tags
    output_file.write('</body>\n')
    output_file.write('</html>\n')
    
    output_file.close()

def import_body_text(working_file):
    #imports and parses paragraphs from body.txt
    body = open("body.txt","r")
    text_list = body.readlines()
    working_file.write('<p>\n')
    
    for i in text_list:
        if i == "\n":
            working_file.write('\n</p>\n')
            working_file.write('<p>\n')
        else:
            working_file.write(i[:-3] + " ")
    
    working_file.write('\n</p>\n')
    body.close()
    
def main():
    start_thru_head()
    body_thru_end()

if __name__ == "__main__":
    main()
