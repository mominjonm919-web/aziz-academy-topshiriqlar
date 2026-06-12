A = set(map(int, input().split()))
B = set(map(int, input().split()))
intersection_count = len(A & B)
union_count = len(A | B)
jaccard_index = intersection_count / union_count
print(f"{jaccard_index:.3f}")