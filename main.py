from fpdf import FPDF
import os

# --- Constants ---
FONT_SIZE = 10
FONT_FAMILY = "JetBrainsMono"
# Ensure the path is absolute to avoid file not found errors
FONT_PATH = os.path.abspath("./fonts/JetBrainsMono-SemiBold.ttf")
WIDTH = 170
LINE_SPACING = 4
MARGIN_WIDTH = 20
OUTPUT_FILE_NAME = "output.pdf"

# --- Custom PDF Class ---
class PDF(FPDF):
    def footer(self):
        # Position 1.5 cm from bottom
        self.set_y(-15)
        # Use the same font family. 
        # Note: style "I" (Italic) requires the italic version of the font to be added too, 
        # otherwise use "" or "B" if you only added SemiBold.
        self.set_font(FONT_FAMILY, size=10) 
        # Print centered page number
        self.cell(0, 10, f"{self.page_no()}", 0, 0, "C")

# --- User Input ---
file_path = input("Enter file path: ")

# --- Read Text File ---
try:
    with open(file_path, "r", encoding='utf-8') as file:
        file_content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()

# --- Convert to PDF ---
pdf = PDF() # Instantiate the CUSTOM class, not FPDF
pdf.alias_nb_pages()
pdf.add_page()

# Add the font. 'uni=True' is crucial for UTF-8 support in fpdf2
pdf.add_font(family=FONT_FAMILY, fname=FONT_PATH, uni=True)
pdf.set_font(FONT_FAMILY, size=FONT_SIZE)

# Set margins and auto page break
pdf.set_margins(left=MARGIN_WIDTH, top=MARGIN_WIDTH, right=MARGIN_WIDTH)
pdf.set_auto_page_break(auto=True, margin=MARGIN_WIDTH)

# Write content
pdf.multi_cell(w=WIDTH, h=LINE_SPACING, text=file_content, border=0, align='L')

# Output
pdf.output(OUTPUT_FILE_NAME)
print("done")
