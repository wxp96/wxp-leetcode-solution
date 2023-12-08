import math
def calculate_interest_prob(expo_cnt: int, click_cnt: int) -> float:
    p_click_interest=0.05*0.3/(0.95*0.05+0.05*0.3)
    p_notclick_interest=(0.05*0.7)/(0.95*0.95+0.05*0.7)
    comb=math.comb(expo_cnt, click_cnt)

    if expo_cnt == 0:
        return 0
    else:
        return comb*(p_click_interest**click_cnt)*(p_notclick_interest**(expo_cnt-click_cnt))

print(calculate_interest_prob(0, 0)) # 0%
print(calculate_interest_prob(1, 1)) # 24%
print(calculate_interest_prob(2, 1)) # 18.87%

