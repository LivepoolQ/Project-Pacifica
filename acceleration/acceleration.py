"""
@Author: Ziqian Zou
@Date: 2024-10-09 20:34:13
@LastEditors: Ziqian Zou
@LastEditTime: 2024-10-09 20:42:24
@Description: file content
@Github: https://github.com/LivepoolQ
@Copyright 2024 Ziqian Zou, All Rights Reserved.
"""
import numpy as np
import torch

from qpid.constant import INPUT_TYPES
from qpid.model import Model, layers, transformer
from qpid.training import Structure

from .__args import AccelerationArgs


class AccelerationModel(Model):

    def __init__(self, structure=None, *args, **kwargs):
        super().__init__(structure, *args, **kwargs)

        # Init args
        
    def forward(self, inputs: list[torch.Tensor], training=None, mask=None, *args, **kwargs):
        


class AccelerationStructure(Structure):
    MODEL_TYPE = AccelerationModel



