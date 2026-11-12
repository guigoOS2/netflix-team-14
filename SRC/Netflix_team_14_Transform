#Pre-code
import logging
from Netflix_team_14_Extract import extract_data

# PART 2: TRANSFORM
def transform_data(movies, users, history):
    logging.info("Transforming data...")

    total_events = len(history)

    average_rating = sum(item.rating for item in history) / total_events

    movie_views = {}
    user_activity = {}

    for item in history:
        movie_views[item.movie_id] = movie_views.get(item.movie_id, 0) + 1
        user_activity[item.user_id] = user_activity.get(item.user_id, 0) + 1

    most_watched_id = max(movie_views, key=movie_views.get)
    most_watched_movie = next(
        movie.title for movie in movies if movie.id == most_watched_id
    )

    most_active_id = max(user_activity, key=user_activity.get)
    most_active_user = next(
        user.name for user in users if user.id == most_active_id
    )

    ranking = sorted(
        movie_views.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return {
        "total_events": total_events,
        "average_rating": average_rating,
        "most_watched_movie": most_watched_movie,
        "most_active_user": most_active_user,
        "ranking": ranking,
        "movies": movies
    }

# Run it to test or debug the transformation (Main guard)
if __name__ == "__main__":
    movies, users, history = extract_data()
    results = transform_data(movies, users, history)
