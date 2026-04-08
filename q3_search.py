# q3_search.py

def score(user, garment, weights=None):
    """
    Compute fit score using:
    - Asymmetric penalty (tight > loose)
    - Weighted importance (Chest > Waist > Hip)
    """

    if weights is None:
        weights = {"Chest": 2, "Waist": 1.5, "Hip": 1}

    total_penalty = 0

    for key in ["Chest", "Waist", "Hip"]:
        diff = garment[key] - user[key]

        # 🚨 Hard constraint (too tight = very bad)
        if diff < 0:
            penalty = abs(diff) * 3

        # ⚠ Soft constraint (too loose = still bad but less)
        else:
            penalty = diff * 2

        total_penalty += penalty * weights.get(key, 1)

    fit_score = max(0, 100 - total_penalty)

    return round(fit_score, 2)


def find_best(user, db, top_n=3):
    """
    Returns top N garments with:
    - ID
    - Score
    - Measurements (for UI display)
    """

    scored = []

    for garment in db:
        s = score(user, garment)

        scored.append({
            "id": garment["id"],
            "score": s,
            "Chest": garment["Chest"],
            "Waist": garment["Waist"],
            "Hip": garment["Hip"]
        })

    # Sort by highest score
    scored.sort(key=lambda x: x["score"], reverse=True)

    return scored[:top_n]