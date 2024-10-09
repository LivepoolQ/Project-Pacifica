"""
@Author: Ziqian Zou
@Date: 2024-10-09 20:22:54
@LastEditors: Ziqian Zou
@LastEditTime: 2024-10-09 20:37:33
@Description: file content
@Github: https://github.com/LivepoolQ
@Copyright 2024 Ziqian Zou, All Rights Reserved.
"""
import qpid

from .__args import AccelerationArgs
from .acceleration import AccelerationModel, AccelerationStructure

# Register new args and models
qpid.register_args(AccelerationArgs, 'Acceleration Args')
qpid.register(
    acceleration=[AccelerationStructure, AccelerationModel]
)