![baseball picture](https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/af6e4f9b-58ac-4859-9406-7a76a56f1866)
<sup>Photo by Pixabay: https://www.pexels.com/photo/baseball-player-on-field-photo-163516/
# Best Lineup for the White Sox Baseball Team
The book and movie “Moneyball” tells the story of Billy Beane, the Oakland Athletics general manager who put together a competitive baseball team despite having a restricted budget. His “secret” was the strategic use of data-driven methodology. I was inspired by this movie, so I used it to propose a data analysis project for a “Business Modeling and Simulation” course.

## Problem Description
In the 2022 regular season, the Chicago White Sox team lost half of their series (win rate of 0.5) and failed to advance to the playoffs. Therefore, our project aims to improve its performance and provide the best lineup. By examining different lineup possibilities and using statistical analysis, we hope to identify the most effective combination of players for each position.

## Input Data Analysis & Modeling
Baseball teams and fans love statistics, so we had a large body of data to work with. Data is retrived from https://www.mlb.com/whitesox/stats/. In the data set, the performance of the batters belonging to the White Sox team was carried out by compiling their individual batting statistics from 2022 data, with each row of an individual batting probability sum equal to 1. Furthermore, the base salary of the batters for the year 2023 was incorporated into the data set which helps us to analyze how cost relates to win rate and expected run.

The dataset for the individual batting statistics of batters comprises several variables, plate appearances (PA) include at bat (AB), walk (BB), hit by a pitch (HBP), sacrifice fly (SF), and sacrifice bunt (SAC). However, the act of executing sacrifice bunt (SAC) is considered a strategic decision and not a reflection of the batter's ability, it has been excluded from our batting individual batting ability.

#### Figure 1: Classification of all batting outcomes
![3](https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/7a42747e-cdd0-4712-962b-af1c1e47acf3)

### Run Allowed Analyses
In 2022, the White Sox team played 162 games in the AL Central, and the data includes information about Runs Allowed (RA) and Innings (Inn). Runs Allowed indicates the amount of runs that score against a team. Assessing RA performance reflects the team's collective effort, making it challenging to attribute losses to a specific individual. Additionally, the composition of pitchers in 2022 and 2023 has stayed relatively constant. Thus, we assume there are no significant changes in fielding performance this year.

The histogram of the density function for Runs Allowed (RA) of 9 innings in 2022 was plotted in Figure 2. The results indicated that the distribution of RA is approximately exponential. The original dataset comprised the RA values for 9 innings in 2022. To generate random numbers that conform to the exponential distribution, we used the previous year's data to set the lambda. Moreover, the histogram of RA in extra innings, which is displayed in Figure 3, also demonstrated an exponential distribution, the simulation of extra innings was performed in the same way as RA for 9 innings.

#### Figure 2: Histogram and Density Function of Runs Allowed of 9 innings in 2022 with Random Numbers
<img src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/df80e8e4-5f16-4d9a-a118-5f7c9d858401.type" width="471" height="354">

#### Figure 3: Histogram and Density Function of Runs Allowed of Extra inning in 2022 with Random Numbers
<img src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/1add8eb0-76b1-452a-a2b8-276caefd4ca0.type" width="471" height="354">


## Simulation and Programming
### Batting outcome with respect of different base situations
We assume the following rule:
1. Any type of hit (1B hit, 2B hit, 3B hit, HR) can occur in any base situation.
2.	A groundout (1 out), an air out (AO), and a strikeout (SO) can occur in any base situation.
3.	A Ground into double play (GIDP) can only occur when a runner is on first base.
4.	A sacrifice fly (SF) can only occur when a runner is on third base.

### Runner Advancing Rule
We assume the following base advancing rule:
1.	A single hit (1B hit) advances all runners one base and the batter to first base.
2.	A double hit (2B hit) advances all runners two bases and the batter to second base.
3.	A triple hit (3B hit) advances all runners three bases and the batter to third base.
4.	A homerun (HR) advances all runners and the batter to home base.
5.	A groundout (1 out) counts the batter as one out and advances runners if it is a force play (A force play happens when a baserunner must try to reach the next base because a runner behind him is approaching his current base).
6.	A ground into double play (GIDP) counts 2 outs for the batter and the runner on first base. The runners are advanced if it is a force play.
7.	Both an air out (AO) and a strikeout (SO) count the batter as one out, and all runners remain unchanged.
8.	Both a walk (BB) and a hit-by-pitch (HBP) advance the batter to first base, and advance other runners if it is a force play.
9.	Sacrifice bunts (SAC) are not counted at all.
10.	A sacrifice fly (SF) advances a runner on third base to home base, while the other runner remains unchanged.

### Algorithms of Program 
#### Figure 4: Overview of the program 
<img width="416" alt="4" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/23afbd93-c5b0-42ab-a0e5-8b4e9de4b16e">

#### Algorithm 1: List out all the lineup combinations and their batting order.
In 2022, designated hitters were adopted universally in MLB, meaning that pitchers are no longer required to hit the ball. This rule change allows teams to have a designated hitter in place of the pitcher, who is often not as skilled at batting as the other players. There are 13 players in the white sox team in 2023, including 2 catchers, 7 infielders, 4 outfielders. Except for pitchers, players in the batting lineup and fielding positions should be consistent, which means that each batting combination would consist of 1 catcher, 4 infielders, 3 outfielders, and 1 designated hitter. Thus, the amount of batting combinations is <img width="211" alt="9" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/6a4f1183-cdd1-431a-85a3-c373170fc59b">

In 1997, Bukiet et al. proposed ten criteria for arranging optimal batting orders for a team. However, the possible batting orders for all of our 387 combinations (987 batting orders for each combination, resulting in a total of 381,969 possibilities) makes it challenging and time-consuming to compute. To address this issue, the project adopted an adjusted version of the traditional batting order proposed by Ursin (2014) to reduce computation time.
Under the adjusted approach, the best batter (highest slugging ability) is positioned at 4th in the batting order, with the second-best batter (second highest slugging ability) at 3rd. The player with the highest on-base percentage is placed at 1st, while the remaining batters are placed at 5th to 9th based on their decreasing order of batting ability. This approach simplifies the task of arranging an optimal batting order by considering a smaller subset of possibilities, thereby making the computation more manageable within the given time constraints.

#### Figure 5: Algorithm 1
<img width="173" alt="5" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/c19ecd26-3b5d-4612-b60a-44c60976b7ac">

#### Algorithm 2.1: Simulate run for n innings
In algorithm 2, we have to first simulate a run for the first 9 innings, which executes the algorithm 2.1 for 9 times. There is a for loop to control the time that the simulation executes. The program generates the batting outcome according to the probabilities, changes the base situation correspondingly, and records the outs if applicable. The run will only be recorded if the inning does not end (3 outs). Same process is applied to extra innings except the simulation only runs for 1 time this time. The algorithm 2.1 (simulate run for n innings) is shown below.

#### Figure 6: Algorithm 2
<img width="360" alt="6" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/2155071c-d5a9-427b-a471-e6cdd055110d">

The possible batting outcomes of a player depend on the base situation, and the probabilities of these outcomes are determined by the player's historical data in the 2022 regular season. If there is no runner on third base, there is no chance for batter to hit a sacrifice fly. Similarly, if there is no runner on first base, there is no chance for batter to hit a groundout into double play. The first batting order combination in the list is Andrew Benintendi, Luis Robert Jr, Oscar Colás, Eloy Jiménez, Andrew Vaughn, Seby Zavala, Gavin Sheets, Romy González, Yoán Moncada. We visualize the simulation of 9 innings run and run allowed for it as an example (see appendix A). In case of a tie (where the total number of runs scored in the first 9 innings is equal to the number of runs allowed), the game will continue with an extra inning until a winner is determined. To ensure accuracy, we simulate 10,000 games for each batting order combination (lineup) in this project.


ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
