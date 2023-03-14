from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid

from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import torch

print("trying to load the thing")

model = core.Model.load('new.pth', ['mechanical-pencils'])
print("loaded")
cap = cv2.VideoCapture(0)


while True:
	ret, frame = cap.read()

	predictions = model.predict(frame)
	

	labels, boxes, scores = predictions
	print(boxes)
	thresh=0.6

	filtered_indices=np.where(scores>=thresh)
	filtered_scores=scores[filtered_indices]

	filtered_boxes=boxes[filtered_indices]
	num_list = filtered_indices[0].tolist()
	filtered_labels = [labels[i] for i in num_list]
	show_labeled_image(frame, filtered_boxes, filtered_labels)
	
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()

