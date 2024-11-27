def eliminate(n, k):
    players = list(range(1, n + 1))  # 列出從 1 到 n
    idx = 0  # 計數起始位置
    
    while len(players) > 1:
        idx = (idx + k - 1) % len(players)  # 確定誰被淘汰
        players.pop(idx)  # 從清單中刪除該人
    
    return players[0]  #    最後留下一個人

# Test
n, k = map(int, input(" n , k = ").split())
print(f"結果：{eliminate(n, k)}")