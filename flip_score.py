def calculate_flip_score(raw_price, psa10_price, grading_fee=20.0):
    try:
        profit = psa10_price - raw_price - grading_fee
        score = max(0, min(100, int((profit / raw_price) * 100))) if raw_price else 0
        return score, profit
    except Exception:
        return 0, 0.0
