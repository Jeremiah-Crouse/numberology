from collections import Counter

# Current mapping from solver
current = {
    'E': 8, 'F': 2, 'G': 3, 'H': 6, 'I': 8, 'L': 8, 'N': 1,
    'O': 1, 'R': 7, 'S': 3, 'T': 1, 'U': 3, 'V': 5, 'W': 9,
    'X': 4, 'Z': 2
}

# Digits left and their remaining capacity
caps = {1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 2}
used = Counter(current.values())
remaining_cap = {d: caps[d] - used.get(d, 0) for d in caps}
print("Remaining capacity:", {d: remaining_cap[d] for d in remaining_cap if remaining_cap[d] > 0})

# Missing letters in alphabetical order
missing = sorted(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - set(current.keys()))
print(f"\nMissing letters ({len(missing)}): {missing}")

# Assign in order to available digits (lowest digit first)
available_digits = sorted([d for d in caps if remaining_cap[d] > 0])
full = current.copy()
idx = 0
for ch in missing:
    if idx >= len(available_digits):
        # Should not happen if capacities sum to >= missing count
        print("Error: not enough capacity")
        break
    d = available_digits[idx]
    full[ch] = d
    remaining_cap[d] -= 1
    if remaining_cap[d] == 0:
        idx += 1

print("\nFull A–Z Crousian Numerology (sorted by letter):")
for ch in sorted(full.keys()):
    print(f"{ch}: {full[ch]}")

# Final frequency check
final_counts = Counter(full.values())
print(f"\nFinal digit frequencies: {dict(sorted(final_counts.items()))}")
