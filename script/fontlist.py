#      |               |                                 |
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  |                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    |
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#      |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                      |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#           |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                  |                     |
#   |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#           |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#   |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                               |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#                |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#        |                         This software lets you list the typefaces 
                
#                              on your computer and generates a list in PDF format                     |                                           |               |                                           |               |                                           |                    |                                           |
                
#                           /                      |    v    |                    \
                
#                      with visuals. It could be useful for frontend programmers or for                |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |
#                                                                                                    |                                                                 |                      |                     |                       |                      |                     |                       |                      |                     |                            |
#               Artists who need this kind of information, or else,. . . random words to finish
#      |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                                |                                   |     |                  
#                   |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#              |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                 |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                         =)
                
#
#                                |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#              |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#      |                        |                                         |                                |
                
#
#                                                     !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#      |               |                                 !
                
#                  |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#           |                                  !                                     |
                
#                  |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#   |                          |                       |                    !
#           |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#      |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                      |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#           |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
                
#                  |                     |
#   |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |                                    |                       |                              |                                                                        |
#           |                               |                                         !                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
             
from PyQt5.QtWidgets import QApplication, QLabel, QProgressDialog
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap
from PyQt5.QtCore import Qt
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.pdfgen import canvas
import os,sys


#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


#function to make an exe file with py to exe
def ressource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path ,relative_path)
#to make it works, you have to rename all your path with ressource_path (/path/) WHEN YOU WILL TURN THE SCRIPT TO EXE
#Example : /icon/lol.png  BECOME  ressource_path(/icon/lol.png)




#Function to take picture of text in certain font in a label outside of the screen
def picturing_fonts(font_name, font_size=16, text="Dèc-45#ÉcRiRe C'èSt C0mpLèx£ ^^", output_dir="."):
    font = QFont(font_name, font_size)
    label = QLabel(text)
    label.setFont(font)
    label.adjustSize()
    label.setStyleSheet("""QLabel {background-color: white;}""")

    pixmap = QPixmap(label.size())
    pixmap.fill(Qt.transparent)
    label.render(pixmap)
    pixmap.save(os.path.join(output_dir, f"{font_name}.png"))


temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)


app = QApplication([])
font_database = QFontDatabase()
font_list = font_database.families()

app.processEvents()

#Set up  PDF file
pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ressource_path('font_samples.pdf'))
canv_fontlist = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

x, y = 50, height - 50

#Display the progress of PDF creation
on_process = QProgressDialog("Creating PDF...", None, 0, len(font_list))
on_process.setWindowTitle("Creating PDF")
on_process.setWindowModality(Qt.WindowModal)
on_process.show()

temp_dir = os.path.dirname(os.path.abspath(__file__))

#Loop over the font list to create images and add them to the PDF
for i, font_name in enumerate(font_list):
    # Call the capturer function to create an image with the current font
    picturing_fonts(font_name, output_dir=temp_dir)

    #Read the created image using ReportLab's ImageReader utility
    img = utils.ImageReader(os.path.join(temp_dir, f"{font_name}.png"))
    #Get dimensions of the image
    iw, ih = img.getSize()
    #Add the image to the canvas (PDF) at the current position (x, y)
    canv_fontlist.drawImage(os.path.join(temp_dir, f"{font_name}.png"), x, y - ih, iw, ih)
    #Remove the temporary image file as it's no longer needed
    os.remove(os.path.join(temp_dir, f"{font_name}.png"))

    #Set the font and size for the font name label in the PDF
    canv_fontlist.setFont("Helvetica", 20)
    #Draw the font name below the image of the font sample
    canv_fontlist.drawString(x, y - ih - 20, font_name)

    #Update the y position to move down to the next font sample
    y -= ih + 40

    #If the y position is too low (less than 50), move to a new page
    if y < 50:
        canv_fontlist.showPage()
        y = height - 50

    #Update the progress dialog to show the progress of PDF creation
    on_process.setValue(i + 1)
    #Process any pending events to keep the progress dialog responsive
    app.processEvents()


                
#____ ____ ____ _  _ ____ ___    _    ____ _  _ _  _ ____ _  _
#|__/ |  | |    |_/  |___  |     |    |__| |  | |\ | |    |__|
#|  \ |__| |___ | \_ |___  |     |___ |  | |__| | \| |___ |  |
                
#ENDING | https://www.youtube.com/watch?v=CgZVrvQZB6U&ab_channel=SECRETGUEST :3
    

canv_fontlist.save()
on_process.close()
os.startfile(pdf_path)
