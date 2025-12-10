def positive_feedback(ratings):
    count = 0
    for rating in ratings:
        if rating == 4 or rating == 5:
            count += 1

    return f'Positive Feedback: {count / len(ratings) * 100}%' if ratings else f'0%'

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(positive_feedback(ratings))