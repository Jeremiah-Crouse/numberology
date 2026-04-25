import csv

def load_nagfabet(csv_file):
    """Load the Crousian alphabet mapping from CSV."""
    mapping = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        # Skip header if present (adjust if needed)
        header = next(reader, None)
        if header and header[0].strip().lower() == 'letter':
            # header present, ok
            pass
        else:
            # no header, rewind
            f.seek(0)
            reader = csv.reader(f)
        for row in reader:
            if not row or len(row) < 2:
                continue
            letter = row[1].strip().upper()
            try:
                position = int(row[0].strip())
            except ValueError:
                continue
            mapping[letter] = position
    return mapping

def compute_crousmark(word, mapping):
    """Compute full sum and digital root for a word."""
    total = 0
    for ch in word.upper():
        if ch in mapping:
            total += mapping[ch]
        else:
            print(f"Warning: '{ch}' not found in mapping, skipping.")
    # Compute digital root
    dr = total
    while dr > 9:
        dr = sum(int(d) for d in str(dr))
    return total, dr

def main():
    # Load the Crousian alphabet order
    mapping = load_nagfabet('nagfabet.csv')
    if not mapping:
        print("Error: Could not load nagfabet.csv")
        return
    
    print("Crousian numerology calculator")
    print("Type 'quit' to exit.\n")
    
    while True:
        word = input("Enter a word: ").strip()
        if word.lower() in ('quit', 'exit', 'q'):
            break
        if not word:
            continue
        total, dr = compute_crousmark(word, mapping)
        print(f"{word.upper()}: sum = {total} → digital root = {dr}\n")

if __name__ == "__main__":
    main()
