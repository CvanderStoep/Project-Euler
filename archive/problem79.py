from collections import defaultdict

def derive_passcode(attempts):
    # Build graph: for each digit, track which digits must come after it
    after = defaultdict(set)
    digits = set()

    for attempt in attempts:
        a, b, c = attempt.strip()
        digits.update([a, b, c])
        after[a].add(b)
        after[b].add(c)

    # Ensure all digits appear as keys
    for d in digits:
        after.setdefault(d, set())

    passcode = ""

    # Repeatedly pick a digit that has no predecessors
    while after:
        # A digit has no predecessors if it never appears in any "after" set
        candidates = [d for d in after
                      if all(d not in succs for succs in after.values())]

        if not candidates:
            raise ValueError("Inconsistent constraints")

        # For this problem there should be exactly one candidate each step
        d = sorted(candidates)[0]
        passcode += d

        # Remove it from the graph
        del after[d]

    return passcode


if __name__ == "__main__":
    # Read keylog.txt (each line is a 3-digit attempt, e.g. "319")
    with open("problem79.txt") as f:
        attempts = [line.strip() for line in f if line.strip()]
    
    # attempts = ["345", "456", "454"]
    print(derive_passcode(attempts))
