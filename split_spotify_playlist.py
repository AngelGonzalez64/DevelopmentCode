# Importamos las bibliotecas necesarias
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_all_tracks_from_playlist(sp, playlist_id):
    offset = 0
    limit = 100
    tracks = []

    # Recuperamos todas las pistas de la lista de reproducción
    while True:
        response = sp.playlist_tracks(playlist_id, offset=offset, limit=limit)
        tracks.extend(response['items'])

        if response['next'] is None:
            break

        offset += limit

    return tracks

def create_and_populate_playlists(sp, source_playlist_id, track_limit):
    # Obtenemos información de la lista de reproducción de origen
    source_playlist = sp.playlist(source_playlist_id)
    tracks = get_all_tracks_from_playlist(sp, source_playlist_id)
    playlist_name = source_playlist['name']
    
    num_playlists = (len(tracks) + track_limit - 1) // track_limit
    
    # Creamos y poblamos nuevas listas de reproducción con las pistas de la lista de reproducción de origen
    for i in range(num_playlists):
        start = i * track_limit
        end = min(len(tracks), start + track_limit)
        new_playlist_name = f"{playlist_name} - Parte {i+1}"
        
        new_playlist = sp.user_playlist_create(sp.me()['id'], new_playlist_name)
        new_playlist_id = new_playlist['id']
        
        track_ids = [tracks[j]['track']['id'] for j in range(start, end)]
        sp.playlist_add_items(new_playlist_id, track_ids)

# Reemplaza los siguientes valores con tus propios datos
client_id = 'TuIDdeClienteDeSpotify'
client_secret = 'TuSecretoDeClienteDeSpotify'
redirect_uri = 'TuURIdeRedirección'
username = 'TuNombreDeUsuarioDeSpotify'
source_playlist_id = 'TuIDdePlaylistDeSpotify'


# Configuración de la autenticación de Spotipy
scope = 'playlist-modify-public playlist-read-private'
auth_manager = SpotifyOAuth(client_id=client_id,
                            client_secret=client_secret,
                            redirect_uri=redirect_uri,
                            scope=scope,
                            username=username)

sp = spotipy.Spotify(auth_manager=auth_manager)

# Número de canciones por lista de reproducción
track_limit = 50

# Llamando a la función para crear y poblar las listas de reproducción
create_and_populate_playlists(sp, source_playlist_id, track_limit)
