user_input = int(input("구구단 몇 단을 계산할까요(1~9)? "))

while user_input !=0: 
    if not(1 <= user_input <= 9):
        print("잘못 입력했습니다")
        user_input = int(input("구구단 몇 단을 계산할까요(1~9)? "))
        continue
    
    else:
        print("구구단 "+str(user_input)+"을 계산합니다.")
        for i in range(1, 10):
            print(user_input, "X", i, "=", user_input * i)
        user_input = int(input("구구단 몇 단을 계산할까요(1~9)? "))
            
print("구구단 게임을 종료합니다")   