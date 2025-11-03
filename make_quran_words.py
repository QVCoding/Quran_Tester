import re

def main():
    input_file = "quran-simple-plain.sql"
    output_file = "quran_words.txt"

    # Regex pattern to extract (index, sura, ayah, text)
    pattern = re.compile(
        r"\((\d+),\s*(\d+),\s*(\d+),\s*'([^']+)'\)"
    )

    global_word_number = 1
    buffer = ""

    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:

        for line in infile:
            if line.strip().startswith("INSERT INTO"):
                buffer = line
            elif buffer:
                buffer += line
                if line.strip().endswith(";"):
                    # process complete INSERT block
                    for match in pattern.finditer(buffer):
                        _, sura, ayah, text = match.groups()
                        sura = int(sura)
                        ayah = int(ayah)
                        words = text.split()
                        for word_index, word in enumerate(words, start=1):
                            outfile.write(f"{global_word_number},{sura},{ayah},{word_index},{word}\n")
                            global_word_number += 1
                    buffer = ""

    print(f"✅ Done. Output written to {output_file}")

if __name__ == "__main__":
    main()
