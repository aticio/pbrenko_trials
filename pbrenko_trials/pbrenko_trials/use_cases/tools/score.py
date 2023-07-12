from numpy import log as ln


def calculate_score(bricks, raw_data_length):
    balance = 0
    sign_changes = 0
    for i, b in enumerate(bricks):
        if i != 0:
            if bricks[i].type == bricks[i - 1].type:
                balance = balance + 1
            else:
                balance = balance - 2
                sign_changes = sign_changes + 1

    price_ratio = raw_data_length / len(bricks)

    if sign_changes == 0:
        return -1.0
    score = balance / sign_changes
    if score >= 0 and price_ratio >= 1:
        score = ln(score + 1) * ln(price_ratio)
        return score
    else:
        score = -1.0
        return score
