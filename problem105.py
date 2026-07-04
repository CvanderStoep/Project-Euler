from mathlib.number_theory import is_special_sum_set


# def read_file(filepath):
#     with open(filepath, "r", encoding="utf-8") as f:
#         lines = [{int(value) for value in line.strip().replace(",", " ").split()} for line in f if line.strip()]

#     return lines

def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [
            [int(v) for v in line.split(",")]
            for line in f if line.strip()
        ]

if __name__ == '__main__':
    all_sets = read_file('problem105.txt')
    total_sum = 0
    for s in all_sets:
        if is_special_sum_set(s):
            total_sum += sum(s)
    print(f"{total_sum= }")
          
