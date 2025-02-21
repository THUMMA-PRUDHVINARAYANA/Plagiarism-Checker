from difflib import SequenceMatcher

with open('demo1.txt') as first_file, open('demo2.txt') as second_file:
    data_file1 = first_file.read()
    data_file2 = second_file.read()

    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f"The Plagiarism content is {matches * 100:.2f}%")
