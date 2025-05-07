from pydantic import BaseModel
from typing import Union, List, Dict, Optional


class BaseResponse(BaseModel): 
    code : int 
    message : str

class DataResponse(BaseResponse):
    data : Optional[Union[Dict, List]] = None

class TokenResponse(BaseResponse): 
    token : str