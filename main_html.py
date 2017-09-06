from datetime import date
from prompts import user_questions
import images_and_thumbnails

def start_thru_head(title):
    output_file = open("index.html","w")

    #opening tags
    output_file.write('<!DOCTYPE html>\n')
    output_file.write('<html>\n')
    output_file.write('<head>\n')

    #title
    output_file.write('<title>'+ title +'</title>\n')

    #css
    output_file.write('<link rel="stylesheet" href="style.css">\n')

    #close the <head> don't forget to call the ending function to close the <html> tag
    output_file.write('</head>\n') 

    output_file.close()

def body_thru_end(heading):
    output_file = open("index.html","a")
    
    #opening <body> tag
    output_file.write('<body>\n')

    #get the current date for the entry and write it
    d = date.today()
    
    output_file.write('<center><h1>Local River Log Entry ' + d.strftime("%m/%d/%y") + ' </h1></center>\n')
    output_file.write('<hr width="61.8%" />\n')

    output_file.write('<center><h2>'+ heading +'</h2></center>\n')
    import_body_text(output_file)
    output_file.write('<br />\n')
    output_file.write('<hr width="61.8%" />\n')

    output_file.write('<center><h2>Pictures, Maps, Et Cetera</h2></center>\n')
    #close the file b/c i&t will open it
    output_file.close()
    images_and_thumbnails.main()
    #reopen the file because i&t closed it
    output_file = open("index.html","a")
    output_file.write('<br />\n')
    output_file.write('<hr width="61.8%" />\n')

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
    input = user_questions()
    start_thru_head(input[0])
    body_thru_end(input[1])

if __name__ == "__main__":
    main()
