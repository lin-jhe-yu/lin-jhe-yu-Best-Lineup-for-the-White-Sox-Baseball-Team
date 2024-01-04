![baseball picture](https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/af6e4f9b-58ac-4859-9406-7a76a56f1866)
<sup>Photo by Pixabay: https://www.pexels.com/photo/baseball-player-on-field-photo-163516/
# Best Lineup for the White Sox Baseball Team
The book and movie “Moneyball” tells the story of Billy Beane, the Oakland Athletics general manager who put together a competitive baseball team despite having a restricted budget. His “secret” was the strategic use of data-driven methodology. I was inspired by this movie, so I used it to propose a data analysis project for a “Business Modeling and Simulation” course.

## Problem Description
In the 2022 regular season, the Chicago White Sox team lost half of their series (win rate of 0.5) and failed to advance to the playoffs. Therefore, our project aims to improve its performance and provide the best lineup. By examining different lineup possibilities and using statistical analyses, we hope to identify the most effective combination of players for each position.

## Input Data Analyses & Modeling
Baseball teams and fans love statistics, so we had a large body of data to work with. Batter data was retrieved from https://www.mlb.com/whitesox/stats/. In the data set, the performance of the White Sox team batters was carried out by compiling their individual batting statistics from 2022 data, with each row of an individual batting probability sum equal to 1. 

The dataset for the individual batting statistics of batters comprises several variables, plate appearances (PA) include at bat (AB), walk (BB), hit by a pitch (HBP), sacrifice fly (SF), and sacrifice bunt (SAC). However, the act of executing sacrifice bunt (SAC) is considered a strategic decision and not a reflection of the batter's ability, it has been excluded from our batting individual batting ability.

#### Figure 1: Classification of all batting outcomes
![3](https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/7a42747e-cdd0-4712-962b-af1c1e47acf3)

#### Table 1: Batters data <sup> 
<img width="905" alt="Screen Shot 2024-01-02 at 6 37 26 PM" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/b56088db-d73b-4809-b4c1-579da3624fe1">

<sup>The numbers are rounded

### Run Allowed Analyses
In 2022, the White Sox team played 162 games in the AL Central. Runs allowed (RA) data was retrieved from https://www.baseball-reference.com/teams/CHW/2022-schedule-scores.shtml. RA indicates the amount of runs that score against a team. RA performance reflects the team's effort, making it challenging to attribute to a specific individual. Additionally, the composition of pitchers in 2022 and 2023 has stayed relatively constant. Thus, we assume there are no significant changes in fielding performance this year.

The distribution of 9 innings RA in 2022 is approximately exponential (see Figure 2). To generate random numbers that conform to the exponential distribution, we used the previous year's data to set the lambda. Moreover, the distribution of RA in extra innings also demonstrated an exponential distribution (see Figure 3). The simulation of extra innings was performed in the same way as RA for 9 innings.

#### Figure 2: Histogram and density function of runs allowed of 9 innings in 2022 with random numbers
<img src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/df80e8e4-5f16-4d9a-a118-5f7c9d858401.type" width="471" height="354">

#### Figure 3: Histogram and density function of runs allowed of extra inning in 2022 with random numbers
<img src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/1add8eb0-76b1-452a-a2b8-276caefd4ca0.type" width="471" height="354">


## Simulation and Programming
### Batting outcome with respect of different base situations
We assume the following rule:
1. Any type of hit (1B hit, 2B hit, 3B hit, HR) can occur in any base situation.
2.	A groundout (1 out), an air out (AO), and a strikeout (SO) can occur in any base situation.
3.	A Ground into double play (GIDP) can only occur when a runner is on first base.
4.	A sacrifice fly (SF) can only occur when a runner is on third base.

### Runner advancing rule
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

### Algorithms of program 
#### Figure 4: Overview of the program 
<img width="500" alt="20" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/7360307c-080d-4015-aa12-62ee66b027ed">

#### Algorithm 1: List out all the lineup combinations and their batting order.
#### Figure 5: Algorithm 1
<img width="200" alt="8" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/c19ecd26-3b5d-4612-b60a-44c60976b7ac">

There are 13 players in the white sox team in 2023, including 2 catchers, 7 infielders, 4 outfielders. Players in the batting lineup and fielding positions should be consistent, which means that each batting combination would consist of 1 catcher, 4 infielders, 3 outfielders, and 1 designated hitter. Thus, the amount of batting combinations is <img width="230" alt="15" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/6a4f1183-cdd1-431a-85a3-c373170fc59b">

Trying all the possible batting orders is computationally time-consuming. To address this issue, the project adopted an adjusted version of the traditional batting order proposed by Ursin (2014) to reduce computation time (see Figure 6 for modified batting order strategy).

#### Figure 6: Modified batting order strategy
<img width="700" alt="13" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/67835543-312a-4c2b-860f-9b4fa60bc0c3">

#### Algorithm 2.1: Simulate run for n innings
#### Figure 7: Algorithm 2.1
<img width="580" alt="20" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/e16f86e9-6ccb-497a-b05b-2dcdc2550d22">

In algorithm 2, we have to first simulate a run for the first 9 innings (executes the algorithm 2.1 for 9 times). The program generates the batting outcome according to the probabilities, changes the base situation correspondingly, and records the outs if applicable. The run will only be recorded if the inning does not end (3 outs). Same process is applied to extra innings except the simulation only runs for 1 time this time. To ensure accuracy, we simulate 10,000 games for each batting order combination (lineup) in this project.

<sup>(The possible batting outcomes of a player depend on the base situation. For example, If there is no runner on third base, there is no chance for batter to hit a sacrifice fly.)

## Output Analyses
### Best lineup
After simulation, the best lineup for the Chicago White Sox team is identified. See Table 2 for the list of the best lineup. See Table 3 for a comparison between the optimal lineup and the 2022 season lineup.

#### Table 2: Batters in the best lineup
|Batting Order | Batters          | Position    |
| :---         | :---             | :---        |
| 1            | Andrew Benintendi| Outfielders |
| 2            | Tim Anderson     | Infielders  |
| 3            | Oscar Colás      | Outfielders |
| 4            | Eloy Jiménez     | Outfielders |
| 5            | Luis Robert Jr   | Outfielders |
| 6            | Andrew Vaughn    | Infielders  |
| 7            | Seby Zavala      | Catchers    |
| 8            | Elvis Andrus     | Infielders  |
| 9            | Gavin Sheets     | Infielders  |

#### Table 3: Comparison between optimal lineup and 2022 season lineup
|                  | 9 inning score   | Win rate  | Game Win|
| :---             | :---             | :---      |:---     |
|Best lineup       | 4.1849           |0.5132     |81       |
|2022 season lineup| 4.1111           |0.5        |83       |
|Improvement       | 0.07             |0.0132     |2        |

### Further Analyses
#### Standard Ddviation analyses
* Higher expected runs scored are generally associated with higher standard deviation.
#### Figure 7: Relationship between Expected Runs Scored and Standard Deviation for Chicago White Sox Lineups
<img width="306" alt="7" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/87f64be1-4706-4c7f-a511-ab3308a8994d">

* As expected runs scored increases, the win rate tends to increase.
#### Figure 8: Relationship between Expected Runs Scored and Standard Deviation for Chicago White Sox Lineups
<img width="306" alt="7" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/78bc7807-9189-40c1-b406-e6599fce6bae">

#### Cost Analyses of Each Lineup
* Higher lineup payrolls are generally associated with lower expected runs.
#### Figure 9: Relationship between Expected Runs Scored and Payroll of Each Lineup
<img width="306" alt="7" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/d9be6d1f-98cf-4b37-b6dc-ba94edf67b9e">

* As linup payroll increases, the win rate tends to decrease.
#### Figure 10: Relationship between Win Rate and Payroll of Each Lineup
<img width="306" alt="7" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/0621b736-9776-4518-ab40-147ab7c23edd">

#### Individual Player’s Performance Analysis
Figure shows that Hanser Alberto has the highest frequency proportion of 61.25% among all the players. This suggests that he is underperforming. Therefore, providing extra training to Hanser may be beneficial to improve his performance and better fit in the team.

#### Figure 11: Proportion of player in Second Half of Lineup (total presence in second half/ total presence in all lineups)
<img width="550" alt="Picture1" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/b5b2b683-4ada-4f37-8e6b-de7a979f5114">

## Conclusion
In a nutshell, the Chicago White Sox team is recommended to use the best lineup in the coming season in 2023. Based on the findings of our analysis, using the best lineup can lead to a higher average run scored compared to the actual 2022 season. 

Higher expected runs scored are generally associated with higher variability (standard deviation) in the lineup’s performance. For this reason, the team should be mindful of the potential risks and uncertainties associated with pursuing higher runs scored and take those changes into account when making strategic decisions.

Relying solely on the most expensive players within a lineup to achieve the highest runs is not a prudent strategy for the Chicago White Sox team. Although high-priced players are often considered to be better, the team's success is not solely determined by individual talent or payroll. Instead, other factors such as team synergy, coordination, and collective effectiveness can also influence the team's ability to score runs and win games. Therefore, the team should focus on building a cohesive and effective team that can perform well together, rather than relying solely on spending more money on players.

## Takeaways
* Lineups with high win rate are typically found in the middle class of payroll.
* Higher payrolls are not generally associated with higher win rate.
* When pursuing higher run scored, the team should carefully consider how changes in standard deviation can affect their results.

## Discussions
Hirotsu, N. (2011) indicated that when changing batting order with the same players, an increase in runs scored led to an increase in standard deviation. Our own simulation corroborated this finding, as we observed substituting players also resulted in an increase in standard deviation when there is an increase in runs scored. However, our simulation was conducted using a modified batting order strategy. Therefore, to gain a more comprehensive understanding of the impact of changing the batting order on standard deviation, further investigations can be conducted using different batting orders. By using this model, the Chicago White Sox team can determine whether substituting players or changing the batting order has a greater impact on standard deviation when aiming for higher runs scored.  This would provide valuable insights for the team to make informed decisions regarding their batter substitution strategy and optimize their performance on the field.

## Reference
* Ursin, D. (2014). A MARKOV MODEL FOR BASEBALL WITH APPLICATIONS.
* Hirotsu, N. (2011). Reconsideration of the best batting order in baseball: Is the order to maximize the expected number of runs really the best? Journal of Quantitative Analysis in Sports, 7(2). doi:10.2202/1559-0410.1332
* 2023 Chicago White Sox White Sox Roster & Staff. (n.d.). Retrieved May 6, 2023, from https://www.mlb.com/whitesox/roster

## Project Team
* Jhe Yu (Lawrence) Lin
* Lok I (Minnie) Lou 
* HOI KEI (Joanne) TANG
