from constraint import Problem
from collections import Counter

def digital_root(n):
    return (n - 1) % 9 + 1 if n else 0

def number_word(n):
    if n == 0:
        return "ZERO"
    words = [
        "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE",
        "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN",
        "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN", "TWENTY"
    ]
    return words[n-1]

def solve_with_frequency_limit(max_n, include_zero=False, freq_limits=None):
    if freq_limits is None:
        freq_limits = {d: 3 for d in range(1, 9)}
        freq_limits[9] = 2

    letters = set()
    equations = []

    if include_zero:
        equations.append(("ZERO", 9))
        for ch in "ZERO":
            letters.add(ch)

    for n in range(1, max_n+1):
        word = number_word(n)
        target = digital_root(n)
        equations.append((word, target))
        for ch in word:
            letters.add(ch)

    letters = sorted(letters)
    problem = Problem()

    for ch in letters:
        problem.addVariable(ch, range(1, 10))

    # Frequency constraint across all assigned letters
    def freq_constraint(*values):
        counts = Counter(values)
        for d, limit in freq_limits.items():
            if counts.get(d, 0) > limit:
                return False
        return True
    problem.addConstraint(freq_constraint, letters)

    for word, target in equations:
        def eq_constraint(*values, w=word, t=target):
            total = sum(values)
            return digital_root(total) == t
        problem.addConstraint(eq_constraint, word)

    print(f"Solving for max_n={max_n} (ZERO: {include_zero})...")
    solution = problem.getSolution()
    return solution

# Search for highest N with ZERO included
for N in range(20, 0, -1):
    sol = solve_with_frequency_limit(N, include_zero=True)
    if sol:
        print(f"✅ N={N} works with ZERO and frequency limits")
        print("Mapping:")
        for ch in sorted(sol.keys()):
            print(f"  {ch}: {sol[ch]}")
        counts = Counter(sol.values())
        print(f"\nDigit frequencies: {dict(counts)}")
        break
    else:
        print(f"❌ N={N} fails")
