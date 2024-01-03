![baseball picture](https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/af6e4f9b-58ac-4859-9406-7a76a56f1866)
<sup>Photo by Pixabay: https://www.pexels.com/photo/baseball-player-on-field-photo-163516/
# Best Lineup for the White Sox Baseball Team
The book and movie “Moneyball” tells the story of Billy Beane, the Oakland Athletics general manager who put together a competitive baseball team despite having a restricted budget. His “secret” was the strategic use of data-driven methodology. I was inspired by this movie, so I used it to propose a data analysis project for a “Business Modeling and Simulation” course.

## Problem Description
In the 2022 regular season, the Chicago White Sox team lost half of their series (win rate of 0.5) and failed to advance to the playoffs. Therefore, our project aims to improve its performance and provide the best lineup. By examining different lineup possibilities and using statistical analyses, we hope to identify the most effective combination of players for each position.

## Input Data Analyses & Modeling
Baseball teams and fans love statistics, so we had a large body of data to work with. Data was retrieved from https://www.mlb.com/whitesox/stats/. In the data set, the performance of the White Sox team batters was carried out by compiling their individual batting statistics from 2022 data, with each row of an individual batting probability sum equal to 1. Furthermore, the base salary of the batters for the year 2023 was incorporated into the data set which helps us to analyze how cost relates to win rate and expected run.

The dataset for the individual batting statistics of batters comprises several variables, plate appearances (PA) include at bat (AB), walk (BB), hit by a pitch (HBP), sacrifice fly (SF), and sacrifice bunt (SAC). However, the act of executing sacrifice bunt (SAC) is considered a strategic decision and not a reflection of the batter's ability, it has been excluded from our batting individual batting ability.

#### Figure 1: Classification of all batting outcomes
![3](https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/7a42747e-cdd0-4712-962b-af1c1e47acf3)

#### Table 1: Batters data <sup> 
| Name | Back_no | Position | Season | AB/PA | 1B/PA | 2B/PA | 3B/PA | HR/PA | GIDP/PA | GO/PA | AO/PA | SO/PA | BB/PA | HBP/PA | SF/PA | Base Salary |
| :--- | :---    | :---     | :---   | :---  | :---  | :---  | :---  | :---  | :---    | :---  | :---  | :---  | :---  | :---   | :---  | :---  |
|Yasmani Grandal|	24|	catchers|	2022|	0.87	0.14	0.02	0.00	0.01	0.04	0.18	0.27	0.21	0.12	0.01	0.01	$18,250,000
|Seby Zavala|	44	|catchers	|2022|	0.88	0.16	0.07	0.00	0.01	0.00	0.10	0.22	0.32	0.09	0.01	0.01	$732,000
|Hanser Alberto|	26|	infielders|	2022|	0.98	0.16	0.06	0.01	0.01	0.09	0.24	0.25	0.16	0.02	0.00	0.00	$1,300,000
|Tim Anderson|	7	|infielders	|2022|	0.95	0.23	0.04	0.00	0.02	0.08	0.24	0.18	0.16	0.04	0.01	0.00	$12,500,000
|Elvis Andrus|	1	|infielders	|2022|	0.93	0.15	0.06	0.00	0.03	0.07	0.31	0.16	0.16	0.07	0.01	0.00	$3,000,000
|Yoán Moncada|	10|	infielders|	2022|	0.92	0.12	0.04	0.00	0.03	0.02	0.19	0.25	0.26	0.07	0.00	0.00	$17,000,000
|Gavin Sheets|	32|	infielders|	2022|	0.92	0.14	0.05	0.00	0.04	0.04	0.17	0.28	0.21	0.07	0.01	0.01	$735,000
|Andrew Vaughn|	25|	infielders|	2022|	0.92	0.17	0.05	0.00	0.03	0.04	0.23	0.23	0.17	0.06	0.02	0.01	$760,000
|Romy González|	12|	infielders|	2022|	0.96	0.17	0.04	0.01	0.02	0.03	0.20	0.14	0.36	0.02	0.01	0.01	$723,000
|Andrew Benintendi|	23|	outfielders|	2022|	0.89	0.21	0.04	0.01	0.01	0.03	0.26	0.18	0.15	0.10	0.00	0.01	$8,000,000
|Oscar Colás|	22|	outfielders|	2022	0.91	0.19	0.05	0.01	0.04	0.04	0.26	0.10	0.23	0.07	0.01	0.00	$720,000
|Luis Robert Jr|	88|	outfielders|	2022	0.95	0.19	0.04	0.00	0.03	0.02	0.22	0.25	0.19	0.04	0.01	0.00	$9,500,000
|Eloy Jiménez|	74|	outfielders|	2022	0.89	0.18	0.04	0.00	0.05	0.04	0.19	0.18	0.22	0.09	0.01	0.01	$9,500,000


                                                                     


<sup>The numbers are rounded


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

## Output Analyses
### Analysis of the Best Lineup

After simulation, the best lineup for the Chicago White Sox team is identified. Table 1 shows the 9 batters who make up this lineup. 
#### Table 1: Batters in the Best Lineup
|Batting Order | Batters          | Position    |
| :---         | :---             | :---        |
| 1            | Andrew Benintendi| outfielders |
| 2            | Tim Anderson     | infielders  |
| 3            | Oscar Colás      | outfielders |
| 4            | Eloy Jiménez     | outfielders |
| 5            | Luis Robert Jr   | outfielders |
| 6            | Andrew Vaughn    | infielders  |
| 7            | Seby Zavala      | catchers    |
| 8            | Elvis Andrus     | infielders  |
| 9            | Gavin Sheets     | infielders  |

In the 2022 season, the average run score for 9 innings was 4.1111. On the other hand, in the simulated scenario using the best lineup, the average run score was 4.1849. This indicates that using the best lineup in the simulated scenario, without considering extra innings, led to a higher average run score of 0.07 points for 9 innings compared to the actual season. 
Among the 162 games in the 2022 season, the team won 81 games, resulting in a win rate of 0.5. By simulating the performance of the team using the best lineup, the win rate was found to be 0.5132. Multiplying this win rate by the total  number of games in a regular season (162 games) yielded an estimated number of 83 games (0.5132 x 162 = 83.1384) won using this lineup. These results suggest that using this lineup in the upcoming 2023 season could potentially increase the team’s wins by two games compared to the previous season in 2022. 

### Further Analysis
#### Standard Deviation Analysis
The relationship between the expected runs scored and the standard deviation for each lineup of the Chicago White Sox is illustrated in Figure 7. The various plots in the figure represent different lineups. A clear trend can be observed, indicating that higher expected runs scored are generally associated with higher standard deviation.

#### Figure 7: Relationship between Expected Runs Scored and Standard Deviation for Chicago White Sox Lineups
<img width="306" alt="7" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/87f64be1-4706-4c7f-a511-ab3308a8994d">

The relationship between expected runs scored and win rate is shown in Figure 8. The plots in the figure demonstrate a clear pattern, with the trend line indicating a positive slope. This suggests that as the expected runs scored increases, the win rate tends to increase as well. Hence, it implies that scoring more runs has a higher likelihood of winning games.

Figure 7: Relationship between Expected Runs Scored and Standard Deviation for Chicago White Sox Lineups
<img width="303" alt="8" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/78bc7807-9189-40c1-b406-e6599fce6bae">

#### Cost Analysis of Each Lineup
The downward trend exhibited in Figure 9 is clear, with the data points showing a noticeable decrease in expected runs scored as payroll increases. Similarly, Figure 10 also indicates a negative correlation between expected runs scored and win rate. An increase in payroll often corresponds with a decrease in win rate. 
Moreover, lineups with high win rate are typically found in the middle class of payroll, while a higher payroll does not necessarily lead to an increase in win rate. In fact, an increase in payroll beyond the middle class may even lead to a decline in win rate and drag down the bottom line.
Thus, the amount of money spent on players does not necessarily translate into higher expected runs scored and win rate. These findings suggest that there may be other factors that contribute to a team's success beyond simply spending money on players.

#### Figure 9: Relationship between Expected Runs Scored and Payroll of Each Lineup
<img width="218" alt="9" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/d9be6d1f-98cf-4b37-b6dc-ba94edf67b9e">

#### Figure 10: Relationship between Win Rate and Payroll of Each Lineup
<img width="216" alt="10" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/0621b736-9776-4518-ab40-147ab7c23edd">

#### Individual Player’s Performance Analysis
In Figure 11, it shows the proportion of each player's occurrence in the second half of the lineups among all lineups. Based on the findings from the frequency proportion of players in the second half of the lineup, it shows that Hanser Alberto has the highest frequency proportion of 61.25% among all the players. This suggests that he is underperforming. Therefore, providing extra training to Hanser may be beneficial to improve his performance and better fit in the team.

#### Figure 11: Proportion of player in Second Half of Lineup (total presence in second half/ total presence in all lineups)
<img width="377" alt="11" src="https://github.com/lin-jhe-yu/lin-jhe-yu-Best-Lineup-for-the-White-Sox-Baseball-Team/assets/121969452/cb3709ed-3faf-4b0c-900f-7d7a2738003c">

## Conclusion
In a nutshell, the Chicago White Sox team is recommended to use the best lineup in the coming season in 2023. Based on the findings of our analysis, using the best lineup can lead to a higher average run scored compared to the actual 2022 season. As a result, implementing the best lineup in the upcoming season could potentially result in an increase in the number of games won for the team. 
When pursuing higher run scored, the team should carefully consider how changes in standard deviation can affect their results. Our analysis revealed a significant positive correlation between expected runs scored and standard deviation. This implies that higher expected runs scored are generally associated with higher variability in the lineup’s performance. For this reason, the team should be mindful of the potential risks and uncertainties associated with pursuing higher runs scored and take those changes into account when making strategic decisions.
Relying solely on the most expensive players within a lineup to achieve the highest runs is not a prudent strategy for the Chicago White Sox team. Although high-priced players are often considered to be better, the team's success is not solely determined by individual talent or payroll. Instead, other factors such as team synergy, coordination, and collective effectiveness can also influence the team's ability to score runs and win games. Therefore, the team should focus on building a cohesive and effective team that can perform well together, rather than relying solely on spending more money on players.

## Takeaway
*
*
*

## Discussions
According to a previous study, when changing batting order with the same players, an increase in runs scored led to an increase in standard deviation. Our own simulation corroborated this finding, as we observed substituting players also resulted in an increase in standard deviation when there is an increase in runs scored. However, our simulation was conducted using a traditional batting order. Therefore, to gain a more comprehensive understanding of the impact of changing the batting order on standard deviation, further investigations can be conducted using different batting orders. By using this model, the Chicago White Sox team can determine whether substituting players or changing the batting order has a greater impact on standard deviation when aiming for higher runs scored.  This would provide valuable insights for the team to make informed decisions regarding their batter substitution strategy and optimize their performance on the field.

## Reference
* Bukiet, B., Harold, R., & Palacios, J. L. (n.d.). A Markov Chain Approach to Baseball. In Source: Operations Research (Vol. 45, Issue 1). https://about.jstor.org/terms
* Ursin, D. (2014). A MARKOV MODEL FOR BASEBALL WITH APPLICATIONS.
* Hirotsu, N. (2011). Reconsideration of the best batting order in baseball: Is the order to maximize the expected number of runs really the best? Journal of Quantitative Analysis in Sports, 7(2). doi:10.2202/1559-0410.1332
* 2023 Chicago White Sox White Sox Roster & Staff. (n.d.). Retrieved May 6, 2023, from https://www.mlb.com/whitesox/roster

