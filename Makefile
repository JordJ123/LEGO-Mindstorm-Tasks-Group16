.DEFAULT_GOAL := topdf

OUTPUT_DIR = submission
OUTPUT_FILE = labs
FILES = README.md
FLAGS = -s -f markdown
FLAGS_PDF = 

topdf:
	pandoc -o $(OUTPUT_DIR)/$(OUTPUT_FILE).pdf $(FLAGS) $(FLAGS_PDF) $(FILES)

clean:
	rm -rf $(OUTPUT)/*
