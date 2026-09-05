def get_parking_status(available_spaces, total_spaces):
    if available_spaces == 0:
        return "Full"
    elif available_spaces / total_spaces <= 0.20:
        return "Getting Full"
    else:
        return "Available"
