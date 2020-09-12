import random
import discord
import discord.ext
#############
#Dice Roller#
#############
async def roll_dice(inp1, ctx):
    seperated_numbers = inp1.split("d")
    for i in range(0, len(seperated_numbers)):
        seperated_numbers[i] = int(seperated_numbers[i])
    times_rolled = seperated_numbers[0]
    amount = seperated_numbers[1]
    total = 0
    for i in range(times_rolled):
        total += random.randint(1, amount)
        return total

#############
#Stat roller#
#############
def roll_a_line():
    #Establishes global variables
    stats = []
    iteration = 1

    #Generates the stats and appends them to a list
    for i in range(4):
        i+1 #this line doesn nothing, its here just for the IDE to stop telling me it is unused
        stats.append(random.randint(1, 6))

    #I need to establish a lowest, and i need to do it after the stats are generated. aka why it is not at the top.
    lowest = stats[0]

    #logic to handle which number is the lowest
    for i in stats:
        if lowest > stats[iteration]:
            lowest = stats[iteration]
            if iteration < (len(stats)-1):
                iteration+=1
        else:
            if iteration < (len(stats)-1):
                iteration+=1
    stats.remove(lowest)
    return stats

#Creates, and formats the final list for the bot to send
def create_stats():
    current_list = []
    emp = []
    big_list = []
    total = 0
    line_total = []
    for i in range(6):
        i+1 #this line doesn nothing, its here just for the IDE to stop telling me it is unused
        current_list = roll_a_line()
        big_list.append(current_list)
        total += sum(current_list + emp)
        line_total.append(sum(current_list))
    big_list_final = f'''
  
`{big_list[0]}` **{line_total[0]}**
`{big_list[1]}` **{line_total[1]}**
`{big_list[2]}` **{line_total[2]}**
`{big_list[3]}` **{line_total[3]}**
`{big_list[4]}` **{line_total[4]}**
`{big_list[5]}` **{line_total[5]}**
**Your Total is: {total}**
'''
    #return(total, line_total, big_list_final)
    return big_list_final
