from pdfminer.high_level import exract_text
from collections import Counter
import re

# Function to extract text from PDF

def extract_text_from_pdf(pdf_path):
	text = exract_text(pdf_path)
	return text

# Function to analyze words and their frequency

def analyze_text(text):

	#Removing punctuation and onverting to lowercase
	words = re.findall(r'\w+', text.lower())
	word_count = Counter(words)
	return word_count

#Path to the PDF file
pdf_path = "/mnt/c/Users/Paul Sr/My Drive (paul.tyler.jones@gmail.com)/Career Information/Resumes/Public/GPT Test Copy of 20230509 Paul Tyler Jones.pdf"

#Extracting text from PDF
text = extract_text_from_pdf(pdf_path)

#Analyzing text
word_count = analyze_text(text)

#Printing to table
print("Word\Frequency")
for word, count in word_count.items():
	print(f"(word)\t(count)")
