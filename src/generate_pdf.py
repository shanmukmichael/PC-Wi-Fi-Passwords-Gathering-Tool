from fpdf import FPDF


def generate_pdf(filename,data, SSID, passwords, easy_access, profile_errors):

    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times', 'B', 14.0)
    center = pdf.w - 2*pdf.l_margin
    col_width = center/2
    th = pdf.font_size
    pdf.ln(3*th)
    pdf.cell(center, 0.0, 'PC Wi-Fi Profiles Info', align='C')
    pdf.set_font('Times', '', 10)
    pdf.ln(0.5)
    pdf.cell(center, 0.0, 'Total Profiles : {} | Passwords : {} | Easy Access : {} | Profile Errors : {}'.format(
        SSID, passwords, easy_access, profile_errors), align='C')
    pdf.set_font('Times', '', 10)
    pdf.ln(0.2)
    for row in data:
        for info in row:
            pdf.cell(col_width, 2*th, str(info), border=1)
        pdf.ln(2*th)
    pdf.output(filename, 'F')

