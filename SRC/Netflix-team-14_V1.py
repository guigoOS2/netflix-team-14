# PART 1: EXTRACT
def extract_data():
    logging.info("Extracting data...")
    return movies, users, history


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


# PART 3: LOAD REPORT
def load_report(data):
    logging.info("Loading report...")

    print("\n========== MOVIE REPORT ==========")
    print(f"Total Watch Events: {data['total_events']}")
    print(f"Average Rating: {data['average_rating']:.2f}")
    print(f"Most Watched Movie: {data['most_watched_movie']}")
    print(f"Most Active User: {data['most_active_user']}")

    print("\nMovie Popularity Ranking")
    print("------------------------")

    for position, (movie_id, views) in enumerate(data["ranking"], start=1):
        movie = next(
            movie for movie in data["movies"] if movie.id == movie_id
        )
        print(f"{position}. {movie.title} ({views} views)")


# PART 4: COMPLETE PIPELINE
def run_pipeline():
    logging.info("Starting pipeline...")

    extracted_data = extract_data()
    transformed_data = transform_data(*extracted_data)
    load_report(transformed_data)

    logging.info("Pipeline completed successfully.")


# Execute
run_pipeline()