import numpy as np
# Task 1: Generate and Inspect
# Set random seed
np.random.seed(42)
# Generate 5x4 array (5 students, 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))
print("Original Scores:\n", scores)
print()
# 1. Score of 3rd student in 2nd subject
print("3rd student, 2nd subject:",
      scores[2, 1])
# 2. Scores of last 2 students
print("\nLast 2 students' scores:\n",
      scores[-2:, :])
# 3. First 3 students, subjects 2 and 3
print("\nFirst 3 students (subjects 2 & 3):\n",
      scores[:3, 1:3])

# Task 2: Analyze with Broadcasting

# Column-wise mean (rounded to 2 decimals)
column_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise Mean:", column_mean)

# Add curve using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no value exceeds 100
curved_scores = np.clip(curved_scores, None, 100)
print("\nCurved Scores:\n", curved_scores)

# Row-wise max (best subject per student)
row_max = curved_scores.max(axis=1)
print("\nRow-wise Max (Best per student):", row_max)

# Task 3: Normalize and Identify

# Min-max normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)
normalized = (curved_scores - row_min) / (row_max - row_min)
print("\nNormalized Scores:\n", normalized)

# Find index of highest value
max_index = np.unravel_index(
    np.argmax(normalized),
    normalized.shape
)

print("\nHighest normalized value at (student, subject):",
      max_index)

# Extract scores strictly above 90
above_90 = curved_scores[curved_scores > 90]
print("\nCurved scores above 90:\n", above_90)