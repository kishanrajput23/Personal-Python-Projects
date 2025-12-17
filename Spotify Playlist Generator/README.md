# Spotify Playlist Generator 🎧

## What is this?
A small script that creates and manages Spotify playlists using the Spotify Web API via the `spotipy` library. It demonstrates OAuth authentication, searching tracks, and creating playlists programmatically.

**Main script:** `Spotify playlist generator.py`

## How it works
- Uses the Spotify Web API through `spotipy` to authenticate a user (OAuth) and obtain access tokens.
- Searches for tracks or playlists by query and can create a new playlist or add tracks to an existing playlist.
- Handles pagination and rate limits lightly (for larger operations consider batching and retries).

## Requirements
- Python 3.x
- `spotipy` (`pip install spotipy`)

## How to set up & run
1. Register an app on the Spotify Developer Dashboard and get your **Client ID**, **Client Secret**, and set a **Redirect URI**.
2. Set environment variables (recommended):
	- `SPOTIPY_CLIENT_ID`
	- `SPOTIPY_CLIENT_SECRET`
	- `SPOTIPY_REDIRECT_URI`
3. Install dependencies: `pip install spotipy`
4. Run: `python "Spotify playlist generator.py"` and follow the browser-based OAuth flow to authorize the app.

### Example (conceptual)
```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public"))
results = sp.search(q='Nirvana Smells Like Teen Spirit', type='track', limit=1)
track_id = results['tracks']['items'][0]['id']
playlist = sp.user_playlist_create(user=sp.current_user()['id'], name='My Playlist')
sp.playlist_add_items(playlist['id'], [track_id])
```

## Notes & Security
- OAuth scopes: adjust scopes (e.g., `playlist-modify-public`, `playlist-modify-private`) according to what the script needs.
- Keep your client secret private; prefer environment variables over hard-coding credentials.
- Respect Spotify's Web API rate limits and Terms of Service when using the script.

## Summary
Practical project for learning API authentication flows and integrating with third-party services. Consider adding configuration options, error handling, and batching for large playlists.

