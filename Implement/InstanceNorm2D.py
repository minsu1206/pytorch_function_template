import torch
import torch.nn as nn
import numpy as np

### Instance Norm2D - handmade
m = nn.InstanceNorm2d(10, affine=False, track_running_stats=False)
input = torch.randn(2, 10, 3, 4)
in_mean = input.mean(dim=(2, 3))
in_std = torch.var(input, dim=(2, 3), unbiased=False)
in_mean_expand = in_mean.unsqueeze(-1).unsqueeze(-1).repeat(1, 1, 3, 4)
in_std_expand = in_std.unsqueeze(-1).unsqueeze(-1).repeat(1, 1, 3, 4)
output_hand = (input - in_mean_expand) / torch.sqrt(in_std_expand + 1e-5)
output = m(input)
diff = output - output_hand
diff = diff.detach().numpy()

max_diff = np.abs(diff).max()
sum_diff = np.abs(diff).sum()

print(max_diff, sum_diff)
