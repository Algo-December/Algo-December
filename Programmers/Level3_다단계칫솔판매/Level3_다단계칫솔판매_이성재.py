def solution(enroll, referral, seller, amount):  
    def get_money(name, price):
        if name == '-':
            return
        my_index = name_index[name]
        
        parent_money = price // 10
        my_money = price - parent_money
        
        answer[my_index] += my_money
                
        if parent_money > 0:
            parent_name = referral[my_index]
            get_money(parent_name, parent_money)
    
    answer = [0] * len(enroll)
    name_index = {enroll[i]: i for i in range(len(enroll))}
    
    for name, price in zip(seller, amount):
        get_money(name, price * 100)
    
    return answer