import pandas as 
import numpy as np
import scipy.stats as stats


chat_id = 257689856 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.04
    z_a = stats.norm.ppf(1 - alpha)
    
    p1 = x_success / x_cnt # cont
    p2 = y_success / y_cnt # test
    p = (x_success + y_success) / (x_cnt + y_cnt) # all
    
    z = (p1 - p2) / np.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return z > z_a # Ваш ответ, True или False
