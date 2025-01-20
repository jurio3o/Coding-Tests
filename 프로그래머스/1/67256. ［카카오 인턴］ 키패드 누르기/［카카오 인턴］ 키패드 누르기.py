def solution(numbers, hand):
    answer = ''
    left_loc = 10 
    right_loc = 12
    for x in numbers:
        if x in [1, 4, 7]:
            answer += 'L'
            left_loc = x
            
        elif x in [3, 6, 9]:
            answer += 'R'
            right_loc = x
            
        else: 
            if x==0:
                x = 11
            
            move_lst = []
            for loc in [left_loc, right_loc]:
                diff = abs(loc-x)
                move = diff//3

                if x>=loc:
                    move += abs(x-(loc+move*3))
                else:
                    move += abs(x-(loc-move*3))
                                
                move_lst.append(move)

            left_move, right_move = move_lst[0], move_lst[1]
            if left_move == right_move:
                
                if hand == 'left':
                    answer += 'L'
                    left_loc = x
                    
                elif hand == 'right':
                    answer += 'R'
                    right_loc = x

            elif left_move < right_move:
                answer += 'L'
                left_loc = x

            else:
                answer += 'R'
                right_loc = x


    return answer