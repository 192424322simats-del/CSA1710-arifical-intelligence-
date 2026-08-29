def alpha_beta(depth, node, maximizing, values, alpha, beta):

    # Leaf node
    if depth == 3:
        return values[node]

    if maximizing:
        best = -1000

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta pruning
            if beta <= alpha:
                break

        return best

    else:
        best = 1000

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

alpha = -1000
beta = 1000

result = alpha_beta(
    0, 0, True, values, alpha, beta
)

print("Optimal value:", result)
