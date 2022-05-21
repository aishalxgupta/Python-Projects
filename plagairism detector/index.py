from difflib import SequenceMatcher

with open ("a.txt") as file1 , open ("b.txt") as file2:
    fil1data=file1.read()
    fil2data=file2.read()
    similarity=SequenceMatcher(None,fil1data,fil2data).ratio()
    print(similarity*100, "% Plagairism Detected.")

