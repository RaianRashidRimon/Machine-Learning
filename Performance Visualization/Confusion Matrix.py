import numpy as np
from sklearn.metrics import precision_score, recall_score, f1_score

# Define the confusion matrix
conf_matrix = np.array([
    [50, 2, 3],   # Predicted A (Actual A, B, C)
    [10, 60, 7],  # Predicted B (Actual A, B, C)
    [5, 8, 70]    # Predicted C (Actual A, B, C)
])

# Class labels
classes = ['A', 'B', 'C']

# Function to calculate binary confusion matrix for a class
def binary_confusion_matrix(conf_matrix, class_index):
    TP = conf_matrix[class_index, class_index]
    FP = np.sum(conf_matrix[:, class_index]) - TP
    FN = np.sum(conf_matrix[class_index, :]) - TP
    TN = np.sum(conf_matrix) - TP - FP - FN
    return np.array([[TP, FN], [FP, TN]])

# Function to calculate precision, recall, and F1-score
def calculate_metrics(TP, FP, FN):
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
    return precision, recall, f1

# Initialize lists to store metrics
precision_list, recall_list, f1_list = [], [], []

# Calculate metrics for each class
for i, class_name in enumerate(classes):
    binary_matrix = binary_confusion_matrix(conf_matrix, i)
    TP, FN, FP, TN = binary_matrix.ravel()
    precision, recall, f1 = calculate_metrics(TP, FP, FN)
    
    precision_list.append(precision)
    recall_list.append(recall)
    f1_list.append(f1)
    
    print(f"Class {class_name}:")
    print("Binary Confusion Matrix:")
    print(binary_matrix)
    print(f"  Precision = {precision:.3f}, Recall = {recall:.3f}, F1-Score = {f1:.3f}")
    print()

# Flatten the confusion matrix for micro-averaging
y_true = np.array([0]*65 + [1]*70 + [2]*80)  # Actual labels
y_pred = np.array([0]*50 + [1]*2 + [2]*3 +   # Predicted A
                  [0]*10 + [1]*60 + [2]*7 +   # Predicted B
                  [0]*5 + [1]*8 + [2]*70)    # Predicted C

# Micro-averaged metrics
micro_precision = precision_score(y_true, y_pred, average='micro')
micro_recall = recall_score(y_true, y_pred, average='micro')
micro_f1 = f1_score(y_true, y_pred, average='micro')

print("Micro-Averaged Metrics:")
print(f"  Micro Precision = {micro_precision:.3f}")
print(f"  Micro Recall = {micro_recall:.3f}")
print(f"  Micro F1-Score = {micro_f1:.3f}")
print()

# Macro-averaged metrics
macro_precision = precision_score(y_true, y_pred, average='macro')
macro_recall = recall_score(y_true, y_pred, average='macro')
macro_f1 = f1_score(y_true, y_pred, average='macro')

print("Macro-Averaged Metrics:")
print(f"  Macro Precision = {macro_precision:.3f}")
print(f"  Macro Recall = {macro_recall:.3f}")
print(f"  Macro F1-Score = {macro_f1:.3f}")
print()

# Weighted-averaged metrics
weighted_precision = precision_score(y_true, y_pred, average='weighted')
weighted_recall = recall_score(y_true, y_pred, average='weighted')
weighted_f1 = f1_score(y_true, y_pred, average='weighted')

print("Weighted-Averaged Metrics:")
print(f"  Weighted Precision = {weighted_precision:.3f}")
print(f"  Weighted Recall = {weighted_recall:.3f}")
print(f"  Weighted F1-Score = {weighted_f1:.3f}")
