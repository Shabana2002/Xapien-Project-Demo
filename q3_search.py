# q3_search.py
"""
Best-Fit Multi-Constraint Search Algorithm
-----------------------------------------------------
Handles asymmetric penalties, weighting, and returns
Top 3 garments with a fit confidence score (0-100).
"""

def score(user, garment, weights=None):
    """
    Calculate fit score for a single garment.
    Asymmetric penalties:
      - Too small → high penalty
      - Too large → low penalty
    Weights applied to different body measurements.
    """
    if weights is None:
        weights = {"Chest": 2, "Waist": 1, "Hip": 1}

    total_penalty = 0
    for key in ["Chest", "Waist", "Hip"]:
        diff = garment[key] - user[key]
        if diff < 0:
            # Too tight → hard constraint
            penalty = abs(diff) * 10
        else:
            # Too loose → soft constraint
            penalty = diff
        total_penalty += penalty * weights.get(key, 1)

    fit_score = max(0, 100 - total_penalty)
    return fit_score

def find_best(user, db, top_n=3):
    """
    Find top N garments for the user.
    Returns list of dictionaries: [{"id": id, "score": score}, ...]
    """
    scored = []
    for garment in db:
        s = score(user, garment)
        scored.append({"id": garment["id"], "score": int(s)})

    # Sort descending by score
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_n]

if __name__ == "__main__":
    # Demo database for local testing
    db = [
        {"id": 1, "Chest": 90, "Waist": 80, "Hip": 95},   # perfect match
        {"id": 2, "Chest": 92, "Waist": 82, "Hip": 96},   # very close
        {"id": 3, "Chest": 88, "Waist": 78, "Hip": 94},   # very close
    ] + [{"id": i, "Chest": 100+i%5, "Waist": 80+i%3, "Hip": 90+i%4} for i in range(4, 100)]

    user = {"Chest": 90, "Waist": 80, "Hip": 95}
    print(find_best(user, db))