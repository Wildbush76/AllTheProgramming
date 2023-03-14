from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid

from torchvision import transforms
import numpy as np
import cv2

print("trying to load the thing")

model = core.Model.load('new.pth', ['mechanical-pencils'])


cap = cv2.VideoCapture(0)


while True:
    5

   # yea = model(frame)
    ret, frame = cap.read()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    predictions = model.predict(frame)


    labels, boxes, scores = predictions

    thresh=0.8

    filtered_indices=np.where(scores>=thresh)
    filtered_scores=scores[filtered_indices]

    filtered_boxes=boxes[filtered_indices]

    filtered_labels = [labels[i] for i in filtered_indices[0].tolist()]

    print("showing the image")
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
  
    for i, box in enumerate(list(filtered_boxes)):
        x, y, w, h = [int(e) for e in box]
        cv2.rectangle(frame, (x, y), (w,h), (0, 255, 0), 2)
        cv2.putText(frame, "mechancil pencil" + str(filtered_scores[i]).replace("tensor",""), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("frame",frame)
  
    #show_labeled_image(frame, filtered_boxes, filtered_labels)
	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()