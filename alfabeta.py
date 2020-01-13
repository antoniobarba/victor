def alfa_beta(node, depth, a, b, white):
    if depth == 0 or node.is_terminal_node():
        return node.static_evaluation()
    elif white:
        # White playing, maximize the score
        v = -1000000000
        for child in node.children():
            v = max(v, alfa_beta(child, depth - 1, alfa, beta, False))
            a = max(a, v)
            if b <= a:
                break
        return v
    else:
        # Black playing, minimize the score
        v = 1000000000
        for child in node.children():
            v = min(v, alfa_beta(child, depth - 1, alfa, beta, True))
            b = min(b, v)
            if b <= a:
                break
        return v
