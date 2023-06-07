ALGS Overlay made using TAS(Twitch Apex Stats), may work with other Tournaments(eg: Oversite, etc).<br>
**Only URLs from TAS(Twitch Apex Stats) will work!!!**<br>
Site: https://tournaments.tas.gg/
>Refreshes every 10s

## Note
When using for Tournaments other than ALGS `showFullName` and `showLogo` may not work, in such cases the Short names are used.

## Documentation
- **matchUrl**<br>
    URL for the match<br>
    Examples:<br>
    - https://algs.tas.gg/api/match/<matchId><br>
    - https://oe.tas.gg/match/<matchId>
- **showFullName**<br>
  - false: Short names(Initials) from TAS is used for the overlay.
  - true: Uses Full Name from Battlefy.
- **showLogo**<br>
    Shows Logo of respective teams.
- **showRegion**<br>
    Highlight regions of respective teams. 
## Usage
1. Open `config.js` and set the `matchUrl` and other options per requirements.
2. Open OBS and Add new **Browser Source** [Sources > Add Source > Browser].
3. In Browser Properties use Local File option add the overlay file `overlay.html`.
4. Also set `height` and `width` as your display resolution
