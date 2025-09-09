def find_runner_up(scores):
    """
    Find the second highest unique score in the list.
    Return None if no runner-up exists.
    """

    if not scores:
        return None

    # Step 1: Find maximum score
    max_score = scores[0]
    for score in scores:
        if score > max_score:
            max_score = score

    # Step 2: Find the runner-up (second maximum)
    runner_up = None
    for score in scores:
        if score != max_score:  # skip the top score
            if runner_up is None or score > runner_up:
                runner_up = score

    return runner_up