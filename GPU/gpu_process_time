"""
Reference:
  https://deci.ai/resources/blog/measure-inference-time-deep-neural-networks/
  https://pytorch.org/docs/master/_modules/torch/cuda/streams.html#Event.elapsed_time
"""


import torch
from torchvision.models import resnet50


model = resnet50()
device = torch.device("cuda:0")
model.to(device)

batch = 4
dummy_input = torch.randn((batch, 3, 224, 224), dtype=torch.float).to(device)

starter = torch.cuda.Event(enable_timing=True)
ender = torch.cuda.Event(enable_timing=True)

# WARM UP
for _ in range(10):
	x = model(dummy_input)

# MEASURE

with torch.no_grad():
	for i in range(10):
		starter.record()
		_ = model(dummy_input)
		ender.record()

		# GPU SYNC
		torch.cuda.synchronize()
		curr_time = starter.elapsed_time(ender)
		print(curr_time)        # millisecond

