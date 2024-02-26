import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3)
        self.conv4 = nn.Conv2d(128, 256, kernel_size=3)
        self.fc1 = nn.Linear(4096, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x), 2) # 28>26 | 1>3 | 1>1
        x = F.relu(F.max_pool2d(self.conv2(x), 2)) #26>24>12 | 3>5>6 | 1>1>2
        x = F.relu(self.conv3(x), 2) # 12>10 | 6>10 | 2>2
        x = F.relu(F.max_pool2d(self.conv4(x), 2)) # 10>8>4 | 10>14>16 | 2>2>4
        x = x.view(-1, 4096) # 4*4*256 = 4096
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

class Net6(nn.Module):
    def __init__(self):
        super(Net6, self).__init__()
        self.conv1 = nn.Conv2d(1, 4, 3) #input -? OUtput? RF
        self.bn1 = nn.BatchNorm2d(4)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.dp1 = nn.Dropout(0.25)
        self.conv2 = nn.Conv2d(4, 8, 3)
        self.bn2 = nn.BatchNorm2d(8)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.dp2 = nn.Dropout(0.25)
        self.conv3 = nn.Conv2d(8, 24, 3)
        self.bn3 = nn.BatchNorm2d(24)
        self.pool3 = nn.MaxPool2d(2, 2)
        self.dp3 = nn.Dropout(0.25)
        self.conv4 = nn.Conv2d(24, 48, 3)
        self.bn4 = nn.BatchNorm2d(48)
        self.pool4 = nn.MaxPool2d(2, 2)
        self.dp4 = nn.Dropout(0.25)
        self.conv5 = nn.Conv2d(48, 10, 3)
        self.bn5 = nn.BatchNorm2d(10)
        self.pool5 = nn.MaxPool2d(2, 2)
        self.dp5 = nn.Dropout(0.25)
        self.gap = nn.AvgPool2d(2)
        self.fc1 = nn.Linear(64, 10)

    def forward(self, x):
        # print(f"Start: {x.shape}")
        x = self.bn1(F.relu(self.conv1(x)))
        # print(f"Conv1: {x.shape}")
        x = self.pool2(self.bn2(F.relu(self.conv2(x))))
        # print(f"Conv2: {x.shape}")
        x = self.dp3(self.bn3(F.relu(self.conv3(x))))
        # print(f"Conv3: {x.shape}")
        x = self.pool4(self.bn4(F.relu(self.conv4(x))))
        # print(f"Conv4: {x.shape}")
        x = self.dp5(self.bn5(F.relu(self.conv5(x))))
        # print(f"Conv5: {x.shape}")
        x = self.gap(x)
        # print(f"GAP: {x.shape}")
        # x = torch.flatten(x, start_dim=1)
        x = x.view(-1, 10)
        # print(f"Flatten: {x.shape}")
        # x = self.fc1(x)
        # print(f"FC: {x.shape}")
        return F.log_softmax(x, dim=1)
