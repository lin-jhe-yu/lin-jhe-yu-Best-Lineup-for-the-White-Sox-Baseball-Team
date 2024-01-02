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


### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

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
