## /NFL Data Mining & Game Analytics Project/

This project applies data‑mining and statistical modeling techniques to historical NFL play‑by‑play and game‑level data to uncover the factors that most strongly influence game outcomes. The analysis focuses on offensive efficiency, defensive performance, turnovers, environmental conditions, and situational metrics, with the goal of understanding how these variables shape scoring and win probability.
The work combines exploratory data analysis, feature engineering, visual storytelling, and predictive modeling to build a comprehensive, data‑driven perspective on what drives success in professional football.

*Project Objectives* - 

The project investigates ten core questions that span performance, environment, scheduling, and predictive modeling:
- Can we predict the winner of an NFL game?
Models are built using offensive efficiency, defensive metrics, turnovers, and situational features to classify game outcomes.
- Which game variables have the strongest correlation with winning?
Correlation analysis and feature‑importance scoring highlight key drivers such as turnover differential, third‑down conversion rate, red‑zone efficiency, yards per play, and time of possession.
- Do cold‑weather teams perform better in snow games?
Snow‑game subsets are analyzed to compare win rates, offensive efficiency, and turnover patterns between cold‑weather and warm‑weather teams.
- Does a team with a better record have a better chance of winning?
Season‑to‑date performance and momentum effects are examined to understand whether strong records translate into higher win probability.
- What is the average number of points scored by winning vs losing teams?
Scoring distributions provide baseline expectations for offensive output in wins and losses.
- How do turnovers affect game outcomes?
Turnover counts and turnover differential are evaluated as predictors of scoring suppression and win probability.
- Do certain teams win more than others?
Team‑level summaries identify consistently high‑performing franchises and quantify win margins.
- Does time and date affect game outcomes, and when are most games played?
Scheduling patterns, travel effects, fatigue, and historical timing conventions are analyzed.
- When during games are most points scored, and does this influence victory?
Quarter‑level scoring patterns reveal whether early, mid‑game, or late scoring is most predictive of winning.
- Do total yards contribute to victory, and does the type of yardage matter?
Total yards, rushing vs passing splits, and opponent yardage allowed are compared to understand offensive production’s role in winning.
Together, these questions form a complete analytical framework for understanding NFL performance from multiple angles.

*Analysis & Visualizations* -

The notebook includes a full suite of visual analyses:
- Home vs Away performance
Points, penalty yards, average gain, total yards.
- Environmental effects
Temperature vs total points, roof type vs scoring, snow‑game comparisons (KDE + swarm plots).
- Predictive metrics
Turnovers, possession time, rush/pass efficiency, logistic‑style win‑probability curves.
- Season‑level trends
Average total points by year.
These plots help reveal how conditions, efficiency, and discipline shape game outcomes.
Jupyter Notebook - NFL_DM_GRP09_2021_2025NFL_PlayByPlayDataMining+Visualization.ipynb (- in scripts). 

*Modeling Approach* - 

A logistic‑style model is used to estimate win probability using:
- Total yards
- Turnovers
- Possession time
- Penalty yards
- Temperature
- Roof type
- Snow indicator
- Situational metrics
Feature curves visualize how each predictor shifts the probability of winning, helping identify the most influential variables.

 *Key Insights* - 
 
- Turnovers are one of the strongest negative predictors of winning.
- Total yards strongly correlate with victory and appear consistently in top feature rankings.
- Cold‑weather teams show measurable advantages in snow games.
- Indoor/closed‑roof stadiums produce higher and more stable scoring.
- Possession time correlates with winning but is not decisive alone.
- Scoring trends vary across seasons, reflecting changes in league style and rules.

*Future Extensions* - 

- Incorporate EPA/WPA metrics from play‑by‑play data
- Build a full win‑probability model
- Add player‑level features (QB efficiency, rushing success rate)
- Deploy an interactive dashboard (Plotly/Streamlit)
- Automate data pipelines for continuous updates

*Reproducibility* - 

To run the project:
- Clone the repository
git clone https://github.com/albo8953/nfl-data-mining-project
- Install dependencies
pip install -r requirements.txt
- Open the notebook, present in "scripts".
- Run all cells to reproduce the analysis and visualizations.



