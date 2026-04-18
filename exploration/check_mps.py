import torch
import os
print(torch.__version__)
print(torch.device("mps"))
print("METAL ENV VARIABLE: ", os.environ['PYTORCH_METAL'])
if torch.backends.mps.is_available():
    print('mps available, checking ...')
    mps_device = torch.device("mps")
    x = torch.ones(1, device=mps_device)
    print (x)
else:
    print ("MPS device not found.")