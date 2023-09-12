### GRID eSports Analytics

GRID eSports Analytics generates real-time esports analytics for players, coaches, and even those interested in smart betting. It simplifies existing GRID datasets and uses ChatGPT to find insights.

View Demo: [grid.aenv.site](https://grid.aenv.site/)

CSGO Game Analytics Demo: [https://grid.aenv.site/game_stream/2578928](https://grid.aenv.site/game_stream/2578928)

Note: In current version login/registration is NOT required as all metrics are public, but in future we'll launch PRO features which will only be available for registered users. Sample user email: user1@web-app.test, user password: pass1234

### Project Structure

**app** contains Django web app that serves dashboards to show analytics, talk to ChatGPT APIs. Refer `../app/web_app/templates/web_app/game_stream.html` file which contains JavaScript code that generates insights & graphs.

**stream** contains websockets server streaming at port 8080 and test client.

**data_files** contains CSGO, DOTA datasets


### What it does

Provide real-time analytics to esports players, coaches, and those who do betting to track performance, learn from the best players, and improve their games.

It's "GRID Live Data" -> "Simplified & Contextual Data" -> "ChatGPT" to generate track metrics and get insights.

**Step 1: Getting Live Data**

Our platform consumes GRID livestream data using Websockets or GraphQL, and it starts converting that data into simpler and contextual versions. 

**Step 2: Simplified & Contextual Data**

We start clubbing or joining different contexts or similar events together, for example:
- clubbing together 100+ events in particular a game round to generate analytics
- clubbing together particular contexts like all "player-killed-player" events in one subset
- keeping track of the weapon purchase frequency of the entire team in one subset

**Step 3.1: Generate Analytics**

Some datasets make it easy to track particular metrics like K/D ratio of each player. So, we show them directly on our dashboard.

**Step 3.2: Generate Insights using ChatGPT**

Some datasets are complex or large, so we feed data into ChatGPT and ask questions directly. ChatGPT can provide quality insights in real-time as the game progresses.


### What's next for GRID eSports Analytics
- We'll add more games like DoTA
- We'll add more metrics to track game comprehensively
- Increase the context size ChatGPT
- Allow users to plug in their own games and make it easy for them to track any live-streams across GRID games.