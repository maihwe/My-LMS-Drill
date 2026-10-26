""" Implement passing_scores(scores, minimum). Return a new list containing only the scores that are greater than or equal to minimum. Preserve the original order. Do not modify the original list"""
def passing_scores(scores, minimum):
    passing = []

    for score in scores:
        if score >= minimum:
            passing.append(score)
        return passing

scores = [45, 80, 60, 90, 50]

print(passing_scores(scores, 60))
print(passing_scores(scores, 90))

print(passing_scores(scores, 100))
print(scores)
