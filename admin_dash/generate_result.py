from reportlab.pdfgen import canvas
from reportlab.lib.units import cm 
def design(pdf,date):
  pdf.setTitle("Exam Report dated-"+date)
  pdf.setFont("Courier-Bold",25)
  pdf.drawString(3.3*cm,28.5*cm,"Exam Report dated-"+date)
  pdf.line(1*cm,28.2*cm,20*cm,28.2*cm)
  pdf.line(1*cm,28.2*cm,1*cm,1*cm)
  pdf.line(20*cm,28.2*cm,20*cm,1*cm)
  pdf.line(1*cm,1*cm,20*cm,1*cm)
  pdf.line(1*cm,27.2*cm,20*cm,27.2*cm)
  pdf.setFont("Courier-Bold",7)
  pdf.line(2.5*cm,28.2*cm,2.5*cm,1*cm)
  pdf.drawString(1.2*cm,27.4*cm,"Roll")
  pdf.line(10*cm,28.2*cm,10*cm,1*cm)
  pdf.drawString(4*cm,27.4*cm,"Name")
  pdf.line(11.5*cm,28.2*cm,11.5*cm,1*cm)
  pdf.drawString(10.1*cm,27.4*cm,"Course")
  pdf.line(13*cm,28.2*cm,13*cm,1*cm)
  pdf.drawString(11.6*cm,27.4*cm,"Paper I")
  pdf.drawString(13.1*cm,27.4*cm,"Paper II")
  pdf.line(14.5*cm,28.2*cm,14.5*cm,1*cm)
  pdf.drawString(14.6*cm,27.4*cm,"Paper III")
  pdf.line(16*cm,28.2*cm,16*cm,1*cm)
  pdf.drawString(16.1*cm,27.4*cm,"Paper IV")
  pdf.line(17.5*cm,28.2*cm,17.5*cm,1*cm)
  pdf.drawString(17.6*cm,27.4*cm,"Paper V")
  pdf.line(18.7*cm,28.2*cm,18.7*cm,1*cm)
  pdf.drawString(18.8*cm,27.4*cm,"Paper VI")
def results(pdf,data):
  pdf.setFont("Courier-Bold",9)
  txt=26.9
  for d in data:
    pdf.drawString(1.2*cm,txt*cm,str(d['student'].roll))
    pdf.drawString(3.2*cm,txt*cm,str(d['student'].name))
    pdf.drawString(10.1*cm,txt*cm,str(d['student'].course))
    pdf.drawString(11.6*cm,txt*cm,str(d['paper'][0]))
    pdf.drawString(13.1*cm,txt*cm,str(d['paper'][1]))
    pdf.drawString(14.6*cm,txt*cm,str(d['paper'][2]))
    pdf.drawString(16.6*cm,txt*cm,str(d['paper'][3]))
    pdf.drawString(17.6*cm,txt*cm,str(d['paper'][4]))
    pdf.drawString(18.8*cm,txt*cm,str(d['paper'][5]))
   
    pdf.line(1*cm,(txt+0.3)*cm,20*cm,(txt+0.3)*cm)
    txt=txt-0.7
    if txt<2:
      pdf.showPage()
      txt=26.9 
      design(pdf,"") 
    

  
  