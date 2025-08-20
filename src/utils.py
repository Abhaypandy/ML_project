import os
import sys

import pandas as pd
import numpy as np
import dill

from src.exception import CustomException

# def error_message_detail(error,error_detail):
#     _,_,exc_tb=error_detail.exc_info()
#     if exc_tb is not None:
#         file_name=exc_tb.tb_frame.f_code.co_filename
#         line_number=exc_tb.tb_lineno
#     else:
#         file_name="Unknown"
#         line_number="Unknown"
#     error_message="error occured in python scripit name [{0}] line number[{1}]".format(
#         file_name,line_number,str(error)
#     )
#     return error_message

# class CustomException(Exception):
#     def __init__(self,error_mesaage,error_detail):
#         super().__init__(error_mesaage)
#         self.error_message=error_message_detail(error_mesaage,error_detail=error_detail)
#     def __str__(self):
#         return self.error_message


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)