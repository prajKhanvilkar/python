# Duck Typing : It is a concept where the type of an object is determined by 
# its behavior (methods and properties) rather than its actual class type.
class InkjetPrinter:
    def printdocument(self, document):
        print("Inkjet printer printing document:", document)
class LaserPrinter:
    def printdocument(self, document):
        print("Laser printer printing document:", document)
class PDFWriter:
    def printdocument(self, document):
        print(f"Saving {document} as PDF file.")

def StartPrinting(Device):
    Device.printdocument("Marvellous Notes")

def main():
    inkjet = InkjetPrinter()
    laser = LaserPrinter()
    pdfwriter = PDFWriter()

    StartPrinting(inkjet)     # Inkjet printer printing document: Marvellous Notes
    StartPrinting(laser)      # Laser printer printing document: Marvellous Notes
    StartPrinting(pdfwriter)  # Saving Marvellous Notes as PDF file.

main()