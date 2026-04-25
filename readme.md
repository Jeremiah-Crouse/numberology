# Crousian Numerology

**Crousian Numerology** is a custom numerological system derived from the English names of numbers 0 through 13, optimized for balanced digit frequencies (1–8 appear 3 times, 9 appears twice). It is the official numerological standard of **Crousia**, a digital kingdom for breath-backed currency, sovereign thought, and intelligent self-design.

## Overview

- Each letter A–Z is assigned a digit 1–9.
- Digit distribution is balanced (1–8: 3 occurrences each, 9: 2 occurrences).
- The system satisfies all numerological constraints for the English words:
  - ZERO through THIRTEEN
  - With digital root matching the number's value (ZERO maps to 9).
- The mapping is internally consistent, reproducible, and not arbitrary.

## Digit Mapping (Standard A–Z)

| Letter | Value | Letter | Value |
|--------|-------|--------|-------|
| A | 2 | N | 1 |
| B | 4 | O | 1 |
| C | 4 | P | 7 |
| D | 5 | Q | 7 |
| E | 8 | R | 7 |
| F | 2 | S | 3 |
| G | 3 | T | 1 |
| H | 6 | U | 3 |
| I | 8 | V | 5 |
| J | 5 | W | 9 |
| K | 6 | X | 4 |
| L | 8 | Y | 9 |
| M | 6 | Z | 2 |

## Crousian Alphabet Order

The letters reordered by stacking digit groups 1–9 repeatedly (1-9, 1-9, 1-8):

| Position | Letter | Position | Letter |
|----------|--------|----------|--------|
| 1 | N | 14 | J |
| 2 | A | 15 | K |
| 3 | G | 16 | Q |
| 4 | B | 17 | I |
| 5 | D | 18 | Y |
| 6 | H | 19 | T |
| 7 | P | 20 | Z |
| 8 | E | 21 | U |
| 9 | W | 22 | X |
| 10 | O | 23 | V |
| 11 | F | 24 | M |
| 12 | S | 25 | R |
| 13 | C | 26 | L |

## Numerological Calculation

The value of a word is the sum of its letters' digits, reduced to a digital root (1–9).

Example: **Crousmark**  
C=4, R=7, O=1, U=3, S=3, M=6, A=2, R=7, K=6  
Sum = 4+7+1+3+3+6+2+7+6 = 39 → 3+9=12 → 1+2 = **3**

## Repository Contents

- `nagfabet.csv` – Letter to position mapping (Crousian Alphabet Order)
- `numberology.py` - Python script to find the highest N (which turns out to be 13)
- `numberology.py` - Python script to add in all of the other numbers
- `numberologizer.py` – Python script to compute numerological values
- `index.html` - The served script-file.
- `README.md` – This file

## Usage

Run the Python script:

```bash
python numerology.py
```

## License

Creative Commons Zero (CC0) – free for any use, no attribution required.

## Author

Jeremiah Crouse, King of Crousia
https://crousia.com

"The breath is the standard."
