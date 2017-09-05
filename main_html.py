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

    import_body_text(output_file)

    #close <body> and <html> tags
    output_file.write('</body>\n')
    output_file.write('</html>\n')
    
    output_file.close()

def import_body_text(working_file):
    body = open("body.txt","r")
    text_list = body.readlines()
    for i in text_list:
        working_file.write(i[:-3] + " ")
    body.close()
    
def main():
    start_thru_head()
    body_thru_end()

if __name__ == "__main__":
    main()
