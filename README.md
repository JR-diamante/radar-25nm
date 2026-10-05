# Radar 25 NM

A small web radar app that shows nearby aircraft and lets you center the display on your current location or custom coordinates.

## What it does

- Loads ADS-B data from multiple providers.
- Shows aircraft within 25 NM of the selected center point.
- Draws a sweep line, trail, aircraft details, and altitude filtering.
- Uses a local Python proxy to avoid CORS issues when served locally.

## Run it locally

1. Open a terminal in the project folder.
2. Start the local server:

```bash
python3 server.py
```

3. Open this URL in your browser:

```text
http://localhost:8000/radar.html
```

## How to use it

- Click `My location` to use your browser geolocation.
- Or enter latitude and longitude manually, then click `Use coordinates`.
- Adjust the controls:
  - Sweep: radar sweep speed
  - Trail: trail length
  - Max altitude: maximum displayed altitude
- Click any target marker to view the aircraft details.

## Files

- `radar.html`: frontend radar interface and drawing logic
- `server.py`: local proxy that retrieves ADS-B data from external sources

## Notes

- The app requires a local web server. Opening the HTML file directly may fail due to browser restrictions.
- If a data source is unavailable, it automatically tries the next one.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
