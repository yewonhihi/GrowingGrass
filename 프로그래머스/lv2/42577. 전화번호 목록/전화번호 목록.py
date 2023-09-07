def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()
    
    for i in range(n-1):
        if phone_book[i+1].find(phone_book[i]) == 0:
                return False
        
    return answer