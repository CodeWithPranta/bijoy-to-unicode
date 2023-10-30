from bijoy2unicode import converter
from langdetect import detect
import unicodedata

def isLineEmpty(line):
    return len(line.strip()) == 0

try:
    with open("bijoy.txt", "r", encoding="utf-8") as read_file:
        with open('unicode.txt', 'w', encoding="utf-8") as write_file:
            for line in read_file:
                if not isLineEmpty(line):
                    nData = unicodedata.normalize('NFKD', line).encode('UTF-8', 'ignore')
                    new_line = nData.decode()
                    eng_text_checker = detect(new_line)
                    if eng_text_checker != 'en':
                        test = converter.Unicode()
                        bijoy_text = new_line
                        toPrint = test.convertBijoyToUnicode(bijoy_text)
                    else:
                        toPrint = new_line
                    write_file.write(toPrint)
except FileNotFoundError:
    print("Input file not found.")
except Exception as e:
    print("An error occurred:", e)
