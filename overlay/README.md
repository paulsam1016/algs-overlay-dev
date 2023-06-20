ALGS Overlay made using TAS(Twitch Apex Stats), may work with other Tournaments(eg: Oversite, etc).<br>
**Only URLs from TAS(Twitch Apex Stats) will work!!!**<br>
Site: https://tournaments.tas.gg/

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
- **showPoweredby**<br>
    Shows `Powered by TAS.gg` as a footer.
- **refreshInterval**<br>
    Refresh Interval in milliseconds
    - Default: 10s [10000ms]
    - Minimum: 5s [5000ms]
    - Maximum: 60s [60000ms]
