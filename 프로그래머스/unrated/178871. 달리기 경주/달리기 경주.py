def solution(players, callings):
    player_dict = {}
    for i, player in enumerate(players):
        player_dict[player] = i
    
    for call in callings:
        p_index = player_dict[call]
        player_dict[players[p_index]] -= 1
        player_dict[players[p_index-1]] += 1
        
        players[p_index], players[p_index-1] = players[p_index-1], players[p_index]
        

    return players
        