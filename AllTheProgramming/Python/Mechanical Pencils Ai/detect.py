
#
from detecto import core, utils, visualize
from detecto.visualize import show_labeled_image, plot_prediction_grid
from torchvision import transforms
import matplotlib.pyplot as plt
import numpy as np



print("starting to train")

Train_dataset=core.Dataset('data/train/')#L1
Test_dataset = core.Dataset('data/test/')#L2
loader=core.DataLoader(Train_dataset, batch_size=10, shuffle=True)#L3
model = core.Model(['mechanical-pencils'])#L4
losses = model.fit(loader, Test_dataset, epochs=5, lr_step_size=3, learning_rate=0.001, verbose=True)#L5

plt.plot(losses)
plt.show()
model.save('new.pth')#holy shit this is going to take a while

print("done")