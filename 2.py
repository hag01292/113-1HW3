def knight_tour(N, startX, startY):
    # 騎士的所有移動方向
    moves = [
        (-2, -1), (-2, +1), (-1, +2), (+1, +2),
        (+2, +1), (+2, -1), (+1, -2), (-1, -2)
    ]
    
    # 棋盤和stack
    visited = [[False] * N for _ in range(N)]  # 標記已造訪的儲存格
    stack = [(startX, startY)]  # 儲存步驟
    visited[startX][startY] = True
    steps = 1  # 通過的儲存格數量

    def count_valid_moves(x, y):
        """計算從位置 (x, y) 開始的合法移動次數。"""
        count = 0
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                count += 1
        return count

    while stack:
        x, y = stack[-1]  # 從堆疊頂部取得目前位置

        # 選擇一個有效的動作
        next_move = None
        min_degree = float('inf')  # 找出有效移動次數最少的方格

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                degree = count_valid_moves(nx, ny)
                if degree < min_degree:
                    min_degree = degree
                    next_move = (nx, ny)

        # 如果你找到了行動，就行動吧
        if next_move:
            nx, ny = next_move
            stack.append((nx, ny))
            visited[nx][ny] = True
            steps += 1
        else:
            # 如果沒有更多有效的動作，則回溯
            stack.pop()

    # 檢查是否所有儲存格都已通過
    return steps == N * N

# Test
N, startX, startY = map(int, input(" N, startX, startY = ").split())
print(f"結果：{knight_tour(N, startX, startY)}")