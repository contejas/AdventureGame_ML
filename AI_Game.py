import random
import time

'''
Experiments with Genetic Artificial Intelligence Algorithms on a simple text-based Adventure Game
By: Tejas Shah

CGP Grey's video about "How Machines Learn" had me thinking
Video: https://www.youtube.com/watch?v=R9OHn5ZF4Uo
Maybe I could train a bot to play a simple text based adventure game fairly well
So here's my shot at it using a custom genetic algorithm...
Also I don't use fancy terms like Sigmoid or Perceptron so
This should be fairly easy to understand compared to the mumbo jumbo that is AI articles and tutorials
It's nicely put, much like CGP Grey's video

The structure includes:
playBots (bots that play the game and choose moves according to their scripts)
builderBots (bots that build bots with either random scripts or scripts inherited from a mother and a father)
teacherBots (bots that assess playBots' scripts by how well they can play the game)
judgeBots (bots that use the teacherBots' assessments to decide which playBots will mate to create the next generation)

Gameplay:
The game involves the player choosing between sword, shield, and potion for a duel with an opponent
They can only use their sword by first gaining energy by drinking the potion
Each sip of the potion gives them one energy point, and each sword swing costs one energy point
Shield just blocks sword

Algorithm to build playBots:
Each playBot plays the game by accessing a scripted playsheet that is created as they initialize
Each move in the script is treated as a "trait" that can be passed down from their father and mother
Child Bot's script for when they have and don't have enough energy for the sword = [Dad1, Mom2, Dad3, Mom4, etc. all the way to Mom10]
where "Dad1" refers to the Father's first move in his script
'''


def BotvBot(bot1, bot2):

    print "\nNow we will see the two best bots ever made face off! "
    print "Bot1 vs Bot2, fight!"

    def printf(x):
        bool = False
        if bool:  # Toggle this to make sure
            print x

    energy = 0
    op_energy = 0

    while True:

        # bot opponent

        if op_energy == 0:
            options = ['Shield', 'Potion']
            opponent_move = bot2.make_move(options)
        elif op_energy != 0:
            options = ['Sword', 'Shield', 'Potion']
            opponent_move = bot2.make_move(options)
        else:
            opponent_move = "TELL ME, DO YOU BLEED?"

        if opponent_move == 'Sword':
            op_energy -= 1

        if opponent_move == 'Potion':
            op_energy += 1

        # Bot chooses moves

        if energy == 0:
            options = ['Shield', 'Potion']
            move = bot1.make_move(options)
        elif energy != 0:
            options = ['Sword', 'Shield', 'Potion']
            move = bot1.make_move(options)
        else:
            move = "YOU WILL."

        if move == 'Sword':
            energy -= 1

        if move == 'Potion':
            energy += 1

        if move == 'Sword' and opponent_move == 'Shield':
            printf("Bot struck with its Sword, but the opponent blocked it!")
        elif move == 'Sword' and opponent_move == 'Sword':
            printf("Both used Sword, nothing happens!")
        elif move == 'Sword' and opponent_move == 'Potion':
            printf(
                "Bingo! While the opponent was taking a potion, the bot struck 'em with its sword, killing him! Bot Wins!")
            outcome = True
            break
        elif move == 'Shield' and opponent_move == 'Shield':
            printf("Cowards! Both used their shield!")
        elif move == 'Shield' and opponent_move == 'Sword':
            printf("The opponent went in for the kill with his sword, but the bot blocked it with its shield!")
        elif move == 'Shield' and opponent_move == 'Potion':
            printf("While the bot had its shield up, the opponent took a sip of his potion!")
        elif move == 'Potion' and opponent_move == 'Shield':
            printf("While the opponent used his shield, the bot drank some of its potion!")
        elif move == 'Potion' and opponent_move == 'Sword':
            printf(
                "Alas! While you were drinking your potion, your opponent killed you with his Sword! GAME OVER!")
            outcome = False
            break
        elif move == 'Potion' and opponent_move == 'Potion':
            printf("Whew! This fight is tiring! You both took a swig of your potion!")

    bot1.gameReset()
    bot2.gameReset()

    if outcome:
        print "Bot1 wins!\n"
    else:
        print "Bot2 wins!\n"


def playAgainstBot(my_bot):  # a feature that allows you to play against a chosen bot yourself - Good Luck!
    energy = 0
    op_energy = 0

    print "\nAlright! Let's go. No cheating by looking at the bot's script! Player vs Bot, start!"

    while True:

        # Bot opponent

        if op_energy == 0:
            options = ['Shield', 'Potion']
            opponent_move = my_bot.make_move(options)
        elif op_energy != 0:
            options = ['Sword', 'Shield', 'Potion']
            opponent_move = my_bot.make_move(options)
        else:
            opponent_move = ""

        if opponent_move == 'Sword':
            op_energy -= 1

        if opponent_move == 'Potion':
            op_energy += 1

        # You choose moves
        move = ""
        if energy == 0:
            options = ['Shield', 'Potion']
            move = raw_input("\nShield or Potion, No Sword: ").capitalize()
            while move not in options:
                move = raw_input("Shield or Potion, No Sword: ").capitalize()
        elif energy != 0:
            options = ['Sword', 'Shield', 'Potion']
            move = raw_input("\nSword, Shield, or Potion: ").capitalize()
            while move not in options:
                move = raw_input("Sword, Shield, or Potion: ").capitalize()

        if move == 'Sword':
            energy -= 1

        if move == 'Potion':
            energy += 1

        print "\nYou picked: ", move
        print "Your energy level now: ", energy
        print "Your opponent picked: ", opponent_move + "\n"

        if move == 'Sword' and opponent_move == 'Shield':
            print("You struck with your Sword, but the bot blocked it!")
        elif move == 'Sword' and opponent_move == 'Sword':
            print("Both used Sword, nothing happens!")
        elif move == 'Sword' and opponent_move == 'Potion':
            print("Bingo! While the bot was taking a potion, you struck it with your sword, killing it! You Win!")
            outcome = True
            break
        elif move == 'Shield' and opponent_move == 'Shield':
            print("Cowards! Both used their shield!")
        elif move == 'Shield' and opponent_move == 'Sword':
            print("The bot went in for the kill with his sword, but you blocked it with your shield!")
        elif move == 'Shield' and opponent_move == 'Potion':
            print("While you had your shield up, the bot took a sip of its potion!")
        elif move == 'Potion' and opponent_move == 'Shield':
            print("While the bot used his shield, you drank some of your potion!")
        elif move == 'Potion' and opponent_move == 'Sword':
            print("Alas! While you were drinking your potion, your opponent killed you with his Sword! GAME OVER!")
            outcome = False
            break
        elif move == 'Potion' and opponent_move == 'Potion':
            print("Whew! This fight is tiring! You both took a swig of your potion!")

    my_bot.gameReset()
    if outcome:
        print "\nYou Win! You are smarter than this bot! But not for long..."
    else:
        print "\nThe bot wins! An algorithmic script beat you, a human, at a game of strategy! That's a scary thought..."
    time.sleep(0.5)  # It's customary (in my mind at least) to have it cool down before it exits
    exit('\ncool cool')


def game(my_bot):  # the actual game that is to be played by the bots, or the "teacher's test"
    games = 0

    while games != 10:  # allowed to play 10 games
        # True is victory, False is loss

        energy = 0
        op_energy = 0

        while True:

            # random opponent
            opponent_move = ""
            if op_energy == 0:
                options = ['Shield', 'Potion']
                opponent_move = random.choice(options)
            elif op_energy != 0:
                options = ['Sword', 'Shield', 'Potion']
                opponent_move = random.choice(options)

            if opponent_move == 'Sword':
                op_energy -= 1

            if opponent_move == 'Potion':
                op_energy += 1

            # Bot chooses moves
            move = ""
            if energy == 0:
                options = ['Shield', 'Potion']
                move = my_bot.make_move(options)
            elif energy != 0:
                options = ['Sword', 'Shield', 'Potion']
                move = my_bot.make_move(options)

            if move == 'Sword':
                energy -= 1

            if move == 'Potion':
                energy += 1

            if move == 'Sword' and opponent_move == 'Shield':
                printf("Bot struck with its Sword, but the opponent blocked it!")
            elif move == 'Sword' and opponent_move == 'Sword':
                printf("Both used Sword, nothing happens!")
            elif move == 'Sword' and opponent_move == 'Potion':
                printf(
                    "Bingo! While the opponent was taking a potion, the bot struck 'em with its sword, killing him! Bot Wins!")
                outcome = True
                break
            elif move == 'Shield' and opponent_move == 'Shield':
                printf("Cowards! Both used their shield!")
            elif move == 'Shield' and opponent_move == 'Sword':
                printf("The opponent went in for the kill with his sword, but the bot blocked it with its shield!")
            elif move == 'Shield' and opponent_move == 'Potion':
                printf("While the bot had its shield up, the opponent took a sip of his potion!")
            elif move == 'Potion' and opponent_move == 'Shield':
                printf("While the opponent used his shield, the bot drank some of its potion!")
            elif move == 'Potion' and opponent_move == 'Sword':
                printf(
                    "Alas! While you were drinking your potion, your opponent killed you with his Sword! GAME OVER!")
                outcome = False
                break
            elif move == 'Potion' and opponent_move == 'Potion':
                printf("Whew! This fight is tiring! You both took a swig of your potion!")

        games += 1
        my_bot.gameReset()
        my_bot.add_to_record(outcome)


def printf(x):
    go = False  # used to easily toggle whether things are printed to console or not
    if go:
        print(x)


def isValidInput(x):  # used to check if inputted variables 'initial_population' and 'number_of_generations' are valid
    if str(x) == '':
        return [False, "YOU DIDN'T ENTER ANYTHING!!! "]
    try:
        test = int(x)
        if int(x) <= 1:
            return [False, "You're going to need more than one bot or generation for this to work... "]
        if int(x) > 100:
            return [False, "That's too many bots/generations! Lower your numbers a bit! "]
    except ValueError:
        return [False, "YOU DIDN'T ENTER A NUMBER!!! "]
    return [True, "If you are reading this on the console, this program's creator made a boo-boo. Please annoy him relentlessly. "]


class playBot():  # Bot that actually plays the game, multiple are created and destroyed
    def __init__(self, num):
        self.num = num  # This is each bot's identification factor, how to tell which generation it is
        self.script = {'S': [None for q in range(10)], # Two scripts are created, one for when the bot has enough energy to use the sword and one for when it doesn't
                       'N': [None for w in range(10)]}  # S is with sword, N is without sword
        self.record = []
        self.wins = 0
        self.Smove = None
        self.Sindex = 0
        self.Nmove = None
        self.Nindex = 0

    def write_script(self, with_sword, without_sword):
        self.script['S'] = with_sword
        self.script['N'] = without_sword

    def gameReset(self):
        self.Sindex = 0
        self.Nindex = 0

    def make_move(self, options):
        if "Shield" in options and "Sword" in options and "Potion" in options:
            script = self.script['S']
            try:
                self.Smove = script[self.Sindex]
                self.Sindex += 1
            except IndexError:
                self.Sindex = 0
                self.Smove = script[self.Sindex]
                self.Sindex += 1
            return self.Smove
        elif "Shield" in options and "Potion" in options:
            script = self.script['N']
            try:
                self.Nmove = script[self.Nindex]
                self.Nindex += 1
            except IndexError:
                self.Nindex = 0
                self.Nmove = script[self.Nindex]
                self.Nindex += 1
            return self.Nmove

    def add_to_record(self, outcome):
        self.record.append(outcome)
        if outcome:
            self.wins += 1


class builderBot():  # bot that builds playBots based on genetics or randomness
    def __init__(self):
        self.current_bot_num = 0  # Adam and Eve are always to be 0 and 1

    def create_baby(self, father, mother):
        new_bot = playBot(self.current_bot_num)
        self.current_bot_num += 1

        fS = father.script['S']
        fN = father.script['N']
        mS = mother.script['S']
        mN = mother.script['N']
        cS = [None for e in range(10)]
        cN = [None for r in range(10)]

        isF = True  # if the trait is to be gotten from father
        for i in range(10):  # scripts are to be 10 moves long
            if isF:
                cS[i] = fS[i]
            else:
                cS[i] = mS[i]
            isF = not isF

        isF = True  # if the trait is to be gotten from father
        for i in range(10):
            if isF:
                cN[i] = fN[i]
            else:
                cN[i] = mN[i]
            isF = not isF

        new_bot.write_script(cS, cN)
        return new_bot

    def create_random_bot(self):
        new_bot = playBot(self.current_bot_num)
        self.current_bot_num += 1

        cS = [random.choice(['Shield', 'Sword', 'Potion']) for s in range(10)]
        cN = [random.choice(['Shield', 'Potion']) for n in range(10)]

        new_bot.write_script(cS, cN)
        return new_bot


class teacherBot():  # bot that administers test on playBots and passes the results to judgeBot
    def __init__(self):
        self.bots_tested = 0

    def test_bot(self, my_bot):
        if len(my_bot.record) == 10:
            pass  # shouldn't go through testing process again; record is already complete
        elif len(my_bot.record) == 0:
            self.bots_tested += 1
            game(my_bot)
        else:
            raise Exception


class judgeBot():  # bot that takes tested playBots and discards the bad ones while sending the good ones to builderBot
    def __init__(self):
        self.megalist = []  # list of all bots ever passed through judge
        self.top = {}  # dict of bots that win 7/10 games or higher
        self.gen = 1
        self.nextBest = 0

    def judge_bots(self, botlist):
        ranked = sorted(botlist, key=lambda x: x.wins, reverse=True)
        self.top[self.gen] = []
        for bot in ranked:
            self.megalist.append(bot)
            if bot.wins >= 7:
                self.top[self.gen].append(bot)
        self.gen += 1

    def getGoodBot(self, gen): # returns the next best bot that played the best from a specific generation
        if self.top[gen]:
            return None
        bot = self.top[gen][self.nextBest]
        self.nextBest += 1
        return bot


def main():

    print "\nThis project's aim is to teach a bot how to of play a text-based Adventure game better than a random bot."

    builder = builderBot()
    teacher = teacherBot()
    judge = judgeBot()

    initial_population = raw_input("What should the initial population be? ")  # between 20 and 50 is recommended
    while not isValidInput(initial_population)[0]:
        initial_population = raw_input(isValidInput(initial_population)[1])
    initial_population = int(initial_population)

    number_of_generations = raw_input("How many generations? ")  # between 20 and 50 is recommended
    while not isValidInput(number_of_generations)[0]:
        number_of_generations = raw_input(isValidInput(number_of_generations)[1])
    number_of_generations = int(number_of_generations)

    print "\nProcessing...\n"
    time.sleep(0.5)  # let the program cool off a bit

    ratio = (initial_population, number_of_generations)
    impossible = [(10,10)]  # list of special impossible combinations of pop to gens, added to as needed
    if ratio in impossible:
        exit("This certain ratio of population to generations is impossible for the algorithm to parse. Sorry!")

    try:
        botlist = []
        for i in range(initial_population):  # First generation of random bots
            bot = builder.create_random_bot()
            teacher.test_bot(bot)
            botlist.append(bot)
        judge.judge_bots(botlist)

        for gen in range(1, number_of_generations):  # Generational loop
            next_gen = []
            for dad in botlist:       # Next generation is comprised of babies made from each bot in the previous gen
                for mom in botlist:   # acting as both a mother and a father for various other same-gen bots
                    new_bot = builder.create_baby(dad, mom)  # This means that some bots will be results of a
                    teacher.test_bot(new_bot)                # previous-gen bot pro-creating with itself
                    next_gen.append(new_bot)
            judge.judge_bots(next_gen)
    except IndexError:
        exit("This certain ratio of population to generations is impossible for the algorithm to parse. Sorry!")

    bot1 = judge.top[number_of_generations][0]  # The theoretical all-time best bot
    bot2 = judge.top[number_of_generations][1]  # The close runner-up

    print str(builder.current_bot_num - 1) + " bots were created in " + str(number_of_generations) + " generations"
    print "The best bot is bot number " + str(bot1.num)

    play = raw_input("Do you want to see this bot's script? [y/n] ")
    if play.lower() == 'y':
        print "Best bot's script: " + str(bot1.script)

        if False in bot1.record:
            print "This bot is not perfect, but it did win " + str(bot1.wins) + "/10 games against a random opponent!"
        else:
            print "This bot is perfect and has won every match it has played against a random opponent!"
        print "This script should give you an idea of how the game should be played strategically"

    BotvBot(bot1, bot2) # pin top 2 bots against each other

    play = raw_input("Do you want to play a game against this bot? [y/n] ")
    if play.lower() == 'y':
        playAgainstBot(bot1)
    else:
        time.sleep(0.5)  # let it cool down again, it gets pretty fast around here
        exit("\ncool cool")


if __name__ == '__main__':
    main()
