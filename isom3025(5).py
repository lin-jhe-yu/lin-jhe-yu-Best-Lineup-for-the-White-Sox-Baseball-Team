import pandas as pd
import itertools 
import random
from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


class batter:
    def create_batter_info():
        
        # read the data
        data = pd.read_excel('data10.xlsx')
        batter_info = {}
        
        # create a dictionary that contains player's info for each player, and append them to the batter_info dictionary
        for i in range(len(data)):
            tem = {}
            for y in data:
                if y != 'Name':
                    tem[y] = data[y][i]
            batter_info[data['Name'][i]] = tem
        return(batter_info)

    def create_player_list_for_each_position(position):
        catchers = []
        infielders = []
        outfielders = []

        if position == 'catchers':
            for i in batter_info:
                if batter_info[i]['Position'] == 'catchers':
                    catchers.append(i)
            return(catchers)
        
        elif position == 'infielders':
            for i in batter_info:  
                if batter_info[i]['Position'] == 'infielders':
                    infielders.append(i)
            return(infielders)
        
        elif position == 'outfielders':
            for i in batter_info: 
                if batter_info[i]['Position'] == 'outfielders':
                    outfielders.append(i)
            return(outfielders)

    def create_combination_for_each_position(i, j, k, catchers_combination, infielders_combination, outfielders_combination):
        catchers_combination.clear()
        infielders_combination.clear()
        outfielders_combination.clear()

        # i number of catchers in a game
        catchers_combination.extend(list(itertools.combinations(catchers,i)))

        # j number of infielders in a game
        infielders_combination.extend(list(itertools.combinations(infielders,j)))
                
        # k number of outfielders in a game
        outfielders_combination.extend(list(itertools.combinations(outfielders,k)))

    # create combination of 9 batters
    def create_combination(all_combination,catchers_combination,infielders_combination,outfielders_combination):
        for i in catchers_combination:
            for y in infielders_combination:
                for j in outfielders_combination:
                    temp = i + y + j
                    all_combination.append(temp)
    
    def remove_selected_player_from_the_pool(player_index, player_not_selected_yet, slugging_percentage_list, on_base_percentage_list, base_advance_ability_list,batting_average_list):
        player_not_selected_yet.pop(player_index)
        slugging_percentage_list.pop(player_index)
        on_base_percentage_list.pop(player_index)
        base_advance_ability_list.pop(player_index)
        batting_average_list.pop(player_index)

    def arrange_batting_order(combination):
        player_not_selected_yet = list(combination).copy()
        temp = ['none']*9
        on_base_percentage_list = []
        base_advance_ability_list = []
        slugging_percentage_list = []
        batting_average_list = []

        #calculate the statistic needed in the batting order arrangement
        for i in combination:
            AB_PA = batter_info[i]['AB/PA']
            Hit_PA = batter_info[i]['1B/PA'] + batter_info[i]['2B/PA'] + batter_info[i]['3B/PA'] + batter_info[i]['HR/PA']
            slugging_percentage = (batter_info[i]['1B/PA'] + 2*batter_info[i]['2B/PA'] + 3*batter_info[i]['3B/PA'] + 4*batter_info[i]['HR/PA'])/AB_PA
            on_base_percentage = (Hit_PA + batter_info[i]['BB/PA'] + batter_info[i]['HBP/PA'])/(AB_PA + batter_info[i]['BB/PA'] + batter_info[i]['HBP/PA'] + batter_info[i]['SF/PA'])
            base_advance_ability = Hit_PA + batter_info[i]['SF/PA']
            batting_average = Hit_PA / AB_PA

            slugging_percentage_list.append(slugging_percentage)
            on_base_percentage_list.append(on_base_percentage)
            base_advance_ability_list.append(base_advance_ability)
            batting_average_list.append(batting_average)
        
        print('player', player_not_selected_yet)
        print('slugging_percentage_list1',slugging_percentage_list)
        print('on_base_percentage_list1', on_base_percentage_list)
        print('base_advance_ability_list1', base_advance_ability_list)
        print('batting_average_list1', batting_average_list)

        # the player in the selection pool with highest slugging_percentage are arranged to be 3rd batter
        selected_player_index = slugging_percentage_list.index(max(slugging_percentage_list))
        temp[2] = player_not_selected_yet[selected_player_index]
        batter.remove_selected_player_from_the_pool(selected_player_index,player_not_selected_yet, slugging_percentage_list, on_base_percentage_list, base_advance_ability_list, batting_average_list)


        # the player in the selection pool with second highest slugging_percentage are arranged to be 4rd batter
        selected_player_index = slugging_percentage_list.index(max(slugging_percentage_list))
        temp[3] = player_not_selected_yet[selected_player_index]
        batter.remove_selected_player_from_the_pool(selected_player_index,player_not_selected_yet, slugging_percentage_list, on_base_percentage_list, base_advance_ability_list, batting_average_list)

        # the player in the selection pool with highest on_base_percentage are arranged to be 1rd batter
        selected_player_index = on_base_percentage_list.index(max(on_base_percentage_list))
        temp[0] = player_not_selected_yet[selected_player_index]
        batter.remove_selected_player_from_the_pool(selected_player_index,player_not_selected_yet, slugging_percentage_list, on_base_percentage_list, base_advance_ability_list, batting_average_list)

        # the player in the selection pool with highest base_advance_ability are arranged to be 2rd batter
        selected_player_index = base_advance_ability_list.index(max(base_advance_ability_list))
        temp[1] = player_not_selected_yet[selected_player_index]
        batter.remove_selected_player_from_the_pool(selected_player_index,player_not_selected_yet, slugging_percentage_list, on_base_percentage_list, base_advance_ability_list, batting_average_list)

        # player_not_selected_yet are arranged to the 5th to 9th batter in descending order of batting average
        n = 4
        for i in range(5):
            for j in player_not_selected_yet:
                selected_player_index = batting_average_list.index(max(batting_average_list))
                temp[n] = player_not_selected_yet[selected_player_index]
                batter.remove_selected_player_from_the_pool(selected_player_index,player_not_selected_yet, slugging_percentage_list, on_base_percentage_list, base_advance_ability_list, batting_average_list)
                n = n + 1
        
        print(temp)
        return(temp)

    # create_batting_order of 9 batters
    def create_batting_order_for_each_combination():
        all_combination = []

        catchers_combination = []
        infielders_combination = []
        outfielders_combination =[]

        # add up the combination of 2 catchers (1 is designated hitter), 4 infielders, 3 outfielders
        batter.create_combination_for_each_position(2, 4, 3, catchers_combination, infielders_combination, outfielders_combination)
        batter.create_combination(all_combination, catchers_combination,infielders_combination,outfielders_combination)
        #print('com',len(all_combination))

        # add up the combination of 1 catchers, 5 infielders (1 is designated hitter), 3 outfielders
        batter.create_combination_for_each_position(1, 5, 3, catchers_combination, infielders_combination, outfielders_combination)
        batter.create_combination(all_combination, catchers_combination,infielders_combination,outfielders_combination)
        #print('com2',len(all_combination))

        # add up the combination of 1 catchers, 4 infielders, 4 outfielders (1 is designated hitter)
        batter.create_combination_for_each_position(1, 4, 4, catchers_combination, infielders_combination, outfielders_combination)
        batter.create_combination(all_combination, catchers_combination,infielders_combination,outfielders_combination)
        #print('com3',len(all_combination))

        print(len(all_combination))

        batting_order_for_each_combination =[]

        for i in all_combination:
            batting_order_for_each_combination.append(batter.arrange_batting_order(i))

        print('done')
        return(batting_order_for_each_combination)


class simulate_game:
    def batting_outcome(batter, base_situation, out):

        batting_outcome = []
        weight_of_batting_outcome = []
        data_that_should_not_be_appended = ['Back_no', 'Position', 'Season','AB/PA','2023 Base Salary']
        
        # runner on 1B and less than 2 outs
        if not((base_situation[0]== 1) and (out < 2)):
            data_that_should_not_be_appended.append('GIDP/PA')
        
        # runner on 3B and less than 2 outs
        if not((base_situation[2]== 1) and (out < 2)):
            data_that_should_not_be_appended.append('SF/PA')

        for i in batter_info[batter]:
            if i in data_that_should_not_be_appended:
                continue
            batting_outcome.append(i)

        if 'GIDP/PA' in data_that_should_not_be_appended:
            for i in batting_outcome:
                if i == 'GO/PA':
                    weight_of_batting_outcome.append(batter_info[batter]['GO/PA']+batter_info[batter]['GIDP/PA'])
                else:
                    weight_of_batting_outcome.append(batter_info[batter][i])

        else:
            for i in batting_outcome:
                weight_of_batting_outcome.append(batter_info[batter][i])

        batting_outcome = random.choices(batting_outcome, weights=weight_of_batting_outcome, k =1)
        return(batting_outcome[0])
        
    def run_and_base_situation_changes(batting_outcome, base_situation):
        run_changes = 0

        # batting_outcome is 1B
        if batting_outcome == '1B/PA':
            # if there is a runner on 3B
            if base_situation[2] == 1:
                run_changes = 1
                base_situation[2] = 0
            
            for i in [-1,-2]:
                base_situation[i] = base_situation[i-1]
            base_situation[-3] = 1

        # batting_outcome is 2B
        elif batting_outcome == '2B/PA':
            # if there is a runner on 2B or 3B
            for i in base_situation[1:3]:
                run_changes = run_changes + i
            for i in [1, 2]:
                base_situation[i]= 0
            base_situation[2] = base_situation[0]
            base_situation[0] = 0
            base_situation[1] = 1

        # batting_outcome is 3B
        elif batting_outcome == '3B/PA':
            # if there is a runner on 1B or 2B or 3B
            for i in base_situation[0:3]:
                run_changes = run_changes + i
            for i in [0,1, 2]:
                base_situation[i]= 0
            base_situation[2] = 1
        
        # batting_outcome is HR
        elif batting_outcome == 'HR/PA':
            for i in base_situation[0:3]:
                run_changes = run_changes + i
            for i in [0,1, 2]:
                base_situation[i]= 0
            run_changes = run_changes + 1
        
        # if batting_outcome is GIDP (Ground Into Double Play)
        elif batting_outcome == 'GIDP/PA':
            third_base_remain_unchanged = False
            # for base_situation of [1,1,1], the runner on third base should run the home base
            if base_situation[0]==1 and base_situation[1]==1 and base_situation[2]==1:
                run_changes = 1
            
            # for base_situation of [1,0,1], the runner on third base should stay on third base
            if base_situation[0]==1 and base_situation[1]==0 and base_situation[2]==1:
                third_base_remain_unchanged = True
            
            # the runner move one base advance, and runners on first and second bases are out
            for i in [-1,-2]:
                base_situation[i] = base_situation[i-1]
            base_situation[-3] = 0
            base_situation[-2] = 0
            
            if third_base_remain_unchanged == True:
                base_situation[-1] = 1
        
        # batting_outcome is GO (Groundout)
        elif batting_outcome == 'GO/PA':
            third_base_remain_unchanged = False
            
            # for base_situation of no runner on first base, the base_situation does not change

            # for base_situation of a runner on first base 
            if base_situation[0] == 1:
                if base_situation[1] == 1 and base_situation[2] == 1:
                    run_changes = 1
                if base_situation[1] == 0 and base_situation[2] == 1:
                    third_base_remain_unchanged = True
                for i in [-1,-2]:
                    base_situation[i] = base_situation[i-1]
                base_situation[-3] = 0
                if third_base_remain_unchanged == True:
                    base_situation[-1] = 1

        # if AO (Air out) or SO (Strike out) the base situation does not change but out increase by 1

        # if BB (bases on balls) or HBP (hit by pitch)
        elif (batting_outcome == 'BB/PA' or batting_outcome == 'HBP/PA'):
            third_base_remain_unchanged = False
            
            # for base_situation of a runner on first base 
            if base_situation[0] == 1:
                if base_situation[1] == 1 and base_situation[2] == 1:
                    run_changes = 1
                if base_situation[1] == 0 and base_situation[2] == 1:
                    third_base_remain_unchanged = True
                for i in [-1,-2]:
                    base_situation[i] = base_situation[i-1]

                if third_base_remain_unchanged == True:
                    base_situation[-1] = 1
                    
            # for base_situation of no runner on first base 
            elif base_situation[0] == 0:
                base_situation[0] = 1

        # if SF (sacrifice fly)
        elif batting_outcome == 'SF/PA':
            run_changes = 1
            base_situation[2] = 0
            for i in [-1,-2]:
                base_situation[i] = base_situation[i-1]
            base_situation[-3] = 0

        # return run changes
        return(run_changes)

    def run_for_n_innings(n, current_batter_index):
        run = 0
        for inning in range(n):
            out = 0
            base_situation = [0,0,0]

            # a inning ends with 3 outs
            while (out < 3):

                # simulate the batting outcome for the batter
                batting_outcome = simulate_game.batting_outcome(batting_order[current_batter_index[0]], base_situation,out)

                # batter in the next inning
                current_batter_index[0] = current_batter_index[0] + 1
                
                # if the ninth batter finishes, it's the turn of the first batter
                if current_batter_index[0] == 9:
                    current_batter_index[0] = 0

                # the temporary run changes will only realize if the out is not 3
                temp = simulate_game.run_and_base_situation_changes(batting_outcome, base_situation)
          
                if (batting_outcome in ['GO/PA', 'AO/PA', 'SO/PA', 'SF/PA']):
                    out = out+1
                if (batting_outcome == 'GIDP/PA'):
                    out = out+2


                # if the out is 3, the inning end and the run chnages won't realize
                if out == 3:
                    break

                run = run + temp

        return(run)
    
    def calculate_lambda_for_data_n(n):

        data = pd.read_excel('RA&INN2.xlsx')

        # Extract the column named n
        inning_RA = data[n]

        # Calculate the lambda parameter
        lambda_parameter = 1 / inning_RA.mean()

        return lambda_parameter

    def generate_run_allowed_for_inning(lambda_parameter,n):

        # Generate 1000 random numbers from the exponential distribution
        random_numbers = expon.rvs(scale=1/lambda_parameter, size=n)

        # round up the run allowed
        for i in range(n):
            random_numbers[i] = round(random_numbers[i])

        return random_numbers

    def calculate_lineup_win_rate_and_average_run(sample_size):

        run_allowed_for_each_game = simulate_game.generate_run_allowed_for_inning(nine_innings_lambda,sample_size)
        win = 0
        total_run_for_n_games = 0
        average_run__allowed_for_9_innings_list.append(run_allowed_for_each_game.mean())

        for games in range(sample_size):

            current_batter_index = [0]

            # a baseball game has 9 innings
            run = simulate_game.run_for_n_innings(9, current_batter_index)
            total_run_for_n_games = total_run_for_n_games +run


            # append run for 9 innings to run_list
            run_list.append(run)

            # if there is a tie continue to simulate the extra inning situation
            while (run == run_allowed_for_each_game[games]):

                # delete2
                #print('extra inning')

                run = run + simulate_game.run_for_n_innings(1, current_batter_index)
                run_allowed_for_each_game[games] = run_allowed_for_each_game[games] + simulate_game.generate_run_allowed_for_inning(extra_inning_lambda,1)
       

            if run > run_allowed_for_each_game[games]:
                win = win +1

        
         # Calculate the standard deviation and append all the results to the corresponding lists
        std_dev = np.std(run_list)
        std_dev_list.append(std_dev) 
        batting_order_list.append(batting_order)
        win_rate_list.append(win/sample_size)
        average_run_for_9_innings_list.append(total_run_for_n_games/sample_size)
        

batter_info = batter.create_batter_info()


catchers = batter.create_player_list_for_each_position('catchers')
infielders = batter.create_player_list_for_each_position('infielders')
outfielders = batter.create_player_list_for_each_position('outfielders')


batting_order_for_each_combination = batter.create_batting_order_for_each_combination()

nine_innings_lambda = simulate_game.calculate_lambda_for_data_n('9_inning_RA')
extra_inning_lambda = simulate_game.calculate_lambda_for_data_n('Extra_inning')

# Create empty lists for storing lineup information
batting_order_list = []
win_rate_list = []
average_run_for_9_innings_list = []
run_list =[]
std_dev_list = []
payroll_list = []
average_run__allowed_for_9_innings_list = []

# revise n to 10000
count = 0
total_payroll = 0
for batting_order in batting_order_for_each_combination:
    simulate_game.calculate_lineup_win_rate_and_average_run(10000)
    count = count + 10000
    print('simulation process: ','%.2f' % round(count/3780000 * 100,2),'%',sep= '')

    for name in batting_order: 
        total_payroll += batter_info[name]['2023 Base Salary']
    payroll_list.append(total_payroll)
    total_payroll=0


# Convert the lists to a dataframe
lineup_info = {'batting_order':batting_order_list, 'win_rate':win_rate_list, 'average_run_for_9_innings':average_run_for_9_innings_list, 'standard_deviation_for_run':std_dev_list,'average_run__allowed_for_9_innings':average_run__allowed_for_9_innings_list,'payroll':payroll_list}
lineup_info = pd.DataFrame(lineup_info)

# Sort the dataframe by expected runs scored in descending order
lineup_info_sorted = lineup_info.sort_values(by='average_run_for_9_innings', ascending=False)

# Output the lineup dataframe to excel
lineup_info_sorted.to_excel("lineup.xlsx", sheet_name='sheet1')

# Plot the relationship between expected runs scored and standard deviation
sb.regplot(x = 'payroll',
           y = 'average_run_for_9_innings',
           ci = None,
           data = lineup_info_sorted, line_kws={"color": "red"})
plt.xlabel('Payroll')
plt.ylabel('Expected Runs Scored')
plt.ticklabel_format(style = 'plain')
plt.title('Relationship between Expected Runs Scored and Payroll\nof Each Lineup')
plt.savefig('payroll_run.png')
plt.close()

# Plot the relationship between expected runs scored and standard deviation
sb.regplot(x = 'payroll',
           y = 'win_rate',
           ci = None,
           data = lineup_info_sorted, line_kws={"color": "red"})
plt.xlabel('Payroll')
plt.ylabel('Win Rate')
plt.ticklabel_format(style = 'plain')
plt.title('Relationship between Win Rate and Payroll\nof Each Lineup')
plt.savefig('payroll_win.png')
plt.close()

# Plot the relationship between expected runs scored and standard deviation
sb.regplot(x = 'average_run_for_9_innings',
           y = 'standard_deviation_for_run',
           ci = None,
           data = lineup_info_sorted, line_kws={"color": "red"})
plt.xlabel('Expected Runs Scored')
plt.ylabel('Standard Deviation')
plt.title('Relationship between Expected Runs Scored and Standard Deviation \n for Chicago White Sox Lineups')
plt.savefig('run_sd.png')
plt.close()

# Plot the relationship between expected runs scored and win rate
sb.regplot(x = 'average_run_for_9_innings',
           y = 'win_rate',
           ci = None,
           data = lineup_info_sorted, line_kws={"color": "red"})
plt.xlabel('Expected Runs Scored')
plt.ylabel('Win Rate')
plt.title('Relationship between Expected Runs Scored and Win Rate\nfor Chicago White Sox Lineups')
plt.savefig('run_win.png')
plt.close()


# Convert the batting order to a dataframe
batting_order_for_each_combination = pd.DataFrame(batting_order_for_each_combination)
batting_order_for_each_combination['average_run_for_9_innings'] = average_run_for_9_innings_list

# Sort the dataframe by expected runs scored in descending order
batting_order_for_each_combination = batting_order_for_each_combination.sort_values(by='average_run_for_9_innings', ascending=False)

# Extract the second half of the batting order
half_no = int(len(batting_order_for_each_combination)/2)
second_half_batting_order = batting_order_for_each_combination.iloc[half_no:]

# Get the names of the players in the second half of the batting order
second_half_player_names = second_half_batting_order.iloc[:, 0:9].values.flatten()
# Count the number of occurrences of each name in the second half of the batting order
second_half_name_counts = pd.Series(second_half_player_names).value_counts()

# Get the names of the players in whole batting order
all_player_names = batting_order_for_each_combination.iloc[:, 0:9].values.flatten()
# Count the number of occurrences of each name in whole batting order
all_name_counts = pd.Series(all_player_names).value_counts()

# Convert number of occurrences of each name in whole batting order to a dataframe
whole = pd.DataFrame({'name':all_name_counts.index, 'count': all_name_counts.values})
whole = whole.sort_values(by='name')

# Convert number of occurrences of each name in the second half of the batting order to a dataframe
second_half = pd.DataFrame({'name':second_half_name_counts.index, 'count': second_half_name_counts.values})
second_half = second_half.sort_values(by='name')

# Merge the 'second_half' dataframe with 'whole' dataframe
allwithpro =  second_half.merge(whole, left_on='name', right_on='name')
allwithpro.columns = ['name','second half','all']

# Calculate the proportion for each player in second half of batting order
proportion = allwithpro['second half']/allwithpro['all']

# Plot the frequency histogram of players in Second Half of Batting Order
plt.figure(figsize=(15,10))
fig = proportion.plot(kind='bar')
fig.set_xticklabels(second_half['name'])
fig.bar_label(fig.containers[0], label_type='edge')
plt.xticks(rotation=30, ha='right', fontsize=8)
plt.xlabel('Player Name')
plt.ylabel('Frequency')
plt.title('Proportion of Players in Second Half of Lineup\n', fontsize=20)
plt.savefig('player_proportion.png')
plt.close()