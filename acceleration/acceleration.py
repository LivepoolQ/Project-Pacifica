"""
@Author: Ziqian Zou
@Date: 2024-10-09 20:34:13
@LastEditors: Ziqian Zou
@LastEditTime: 2024-10-09 20:48:06
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
        self.args._set_default('K', 1)
        self.args._set_default('K_train', 1)
        self.ac_args = self.args.register_subargs(AccelerationArgs, 'ac_args')

        #Set model inputs
        self.set_inputs(INPUT_TYPES.OBSERVED_TRAJ,
                        INPUT_TYPES.NEIGHBOR_TRAJ)
        
        #Layers
        
        
    def forward(self, inputs: list[torch.Tensor], training=None, mask=None, *args, **kwargs):
        


class AccelerationStructure(Structure):
    MODEL_TYPE = AccelerationModel



