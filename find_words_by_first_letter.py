DATA_FILE = 'DATA/words.txt'

LETTER = 'x'

output_file_name = f"{LETTER}_words.txt"

with open(DATA_FILE) as words_in:
    with open(output_file_name, 'w') as words_out:
        for raw_line in words_in:
            if raw_line.startswith(LETTER):
                words_out.write(raw_line)
