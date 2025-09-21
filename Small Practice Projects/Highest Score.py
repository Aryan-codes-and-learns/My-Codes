student_scores = [137, 5, 192, 84, 16, 73, 149, 38, 121, 66]
print(max(student_scores))
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    else:
        max_score = max_score
print(max_score)
