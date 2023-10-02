from Functions.generate_excel import generate_excel_files_for_language 
from Functions.process_json import process_jsonl_files


def main():
    input_folder = 'data'
    output_folder = 'data/output'
    languages_of_interest = ['en-US', 'sw-KE', 'de-DE']
    process_jsonl_files(input_folder, output_folder, languages_of_interest)
    #folder_path = "data"
    #generate_excel_files_for_language(folder_path)
#generate execl files for language
if __name__ == "__main__":
    main()

