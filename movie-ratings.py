movie_ratings = {}
movie_ratings['Dune Part 1'] = 9.5
movie_ratings['Godillz Minus One'] = 9
movie_ratings['Boys in the Boat'] = 7.5
movie_ratings['The Martian'] = 10
movie_ratings['Thor Love and Thunder'] = 4.5

movie_title = input('What movie do you want to watch? ')

def recommend_movie(movie_title,movie_ratings):

    if movie_title in movie_ratings:              
        if movie_ratings[movie_title] >= 8:
            print(f'Movie title:{movie_title} Movie Rating: {movie_ratings[movie_title]}')
        if movie_ratings[movie_title] < 8:
             print('we dont recommend that movie')
        for i in movie_ratings:
            if movie_ratings[i] >= 8:
                print(f'Other suggstions you might like {i}') 
    else:
        print('we dont recommend that movie')
        for i in movie_ratings:
            if movie_ratings[i] >= 8:
                print(f'Other suggstions you might like {i}')
recommend_movie(movie_title,movie_ratings)
    


