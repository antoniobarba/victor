def alfa_beta(node, depth, a, b, white):
    if depth == 0 or node.is_terminal_node():
        return node.static_evaluation(white), node.list_of_moves
    elif white:
        # White playing, maximize the score
        v = -1000000000
        list_of_moves = []
        for child in node.children(white):
            ab, list_of_moves = alfa_beta(child, depth - 1, a, b, False)
            v = max(v, ab)
            a = max(a, v)
            if b <= a:
                break
        return v, list_of_moves
    else:
        # Black playing, minimize the score
        v = 1000000000
        list_of_moves = []
        for child in node.children(white):
            ab, list_of_moves = alfa_beta(child, depth - 1, a, b, True)
            v = min(v, ab)
            b = min(b, v)
            if b <= a:
                break
        return v, list_of_moves
