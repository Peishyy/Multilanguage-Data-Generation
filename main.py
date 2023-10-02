from Functions.generate_excel import generate_excel_files_for_language 
from Functions.process_json import process_jsonl_files


def main():

    # This is the function of question 2
    input_folder = 'data'
    output_folder = 'data/output'
    languages_of_interest = ['en-US', 'sw-KE', 'de-DE']
    process_jsonl_files(input_folder, output_folder, languages_of_interest)

    # This is the function of question 1
    #folder_path = "data"
    #generate_excel_files_for_language(folder_path)


if __name__ == "__main__":
    main()

