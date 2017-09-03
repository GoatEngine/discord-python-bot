import discord
import random
import datetime
import time
count69 = 0
import emojiList
import asyncio
isPoll = False
yes = 0
no = 0
userVoted = []
logsChannel = ''
bcChannels = []
chan69 = {}
numlist = {'0' : 'zero', '1' : 'one', '2': 'two', '3' : 'three', '4' : 'four', '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
responses = [
'Yes, definitely.',
'Most likely.',
'Assuredly, yes.',
'Definitely.',
'Probably.',
'Possibly.',
'Yes, probably.',
'Yes!',

'Ask again.',
'Ask again later.',
'Not sure, ask again.',
'It could go either way.',

'Most likely, no.',
'Assuredly not.',
'Definitely no.',
'No.',
'Probably not.',
'No, definitely not.',
'No!'
]
def getName(b):
    if b.nick != None:
        return b.nick
    return b.name
logs = open('logs.txt', 'a')
client = discord.Client()






@client.event



async def on_message(message):
        # we do not want the bot to reply to itself


    if message.author == client.user:
        return ''

    if message.content.lower().startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        print(msg)
        print('')
        logs.write(msg)
        logs.write(str(datetime.datetime.now()))
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('!hey'):
        msg = 'Hey to you too, {0.author.mention}'.format(message)
        print(msg)
        print('')

        await client.send_message(message.channel, msg)
    if message.content.lower().startswith('!channels'):
        print(message.server.id)


        await client.send_message(message.channel, "Channel Info *gotten and *hopefully* sorted")
    if message.content.lower().startswith('!emoji'):
        msg = ''
        for i in message.content[7:]:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz':
                msg += ':regional_indicator_' + i.lower() + ': '
            elif i in ' ':
                msg += ':black_small_square: '
            elif i in '0123456789':
                msg += ':' + numlist[i] + ':'
        logs.write(msg)
        logs.write(str(datetime.datetime.now()))
        if len(msg) > 0:
            await client.send_message(message.channel,msg)




    if message.content.lower().startswith('!8ball'):
        msg = random.choice(responses)
        print(msg)
        print('')
        logs.write(msg)
        logs.write(str(datetime.datetime.now()))
        await client.send_message(message.channel,':8ball: ' + msg)

    if message.content.lower().startswith('!choose'):
        chooseText = message.content.split()
        chooseText.remove(chooseText[0])
        results = ''
        try:
            print(chooseText[0])
            choices = int(chooseText[0])
            print(choices)
            chooseText.remove(str(choices))
            print(chooseText)
        except:
            choices = 1
        if choices > len(chooseText):
            choices = len(chooseText)
        for i in range(choices):
            n = random.choice(chooseText)
            chooseText.remove(n)
            results += n + ', '
        results = results[:-2]
        await client.send_message(message.channel,results)






#SHOOT FUNCTION HERE, SHOOT FUNCTION HERE. ONLINES AND TEST RIGHT ABOVE, !CHOOSE A BIT FURTHER UP. IF YOU GO DOWN, YOU SEE !HELP. AND NICE.


    if message.content.lower().startswith("!blam"):
        for i in message.mentions:
            await client.send_message(message.channel,"<:heresy:332727090581340171> <:blam:332728652489949185> :skull:")
            await client.send_message(message.channel,"RIP " + getName(i))



    
    if message.content.lower().startswith('!help'):
        msg = '''```HELP DOC
        !choose : Chooses between things. Put a number after !choose to choose multiple items
            \n
        !emoji : Converts text to emoji.\n
        !8ball : Magic 8 ball. Gives yes or no answers to help you predict the future.\n
        !random : Gives a random emoji. Use !random help for the list.



        !poll : Sets up a poll.
            !poll Length Question
            Length is in seconds.
            Use !yes or !no to vote.

        !roll : Rolls dice.
            !roll 3d20, for instance
            !roll 6d12+2

        !blam : Shoots a user.
            !blam @user (can tag as many as you want to blam)


        Use !hey or !hello to say hi.```'''
        print(msg)
        print('')
        logs.write(msg)
        logs.write(str(datetime.datetime.now()))

        await client.send_message(message.author,msg)


    if '69' in message.content or (('sixty' in message.content.lower()) and 'nine' in message.content.lower()):
		global chan69
		try:
			chan69[message.channel.id] += 1
		except:
			chan69[message.channel.id] = 1
        if chan69[message.channel.id] < 7:
            await client.send_message(message.channel,emojiList.combo69[chan69[message.channel.id]])
        else:
            await client.send_message(message.channel,emojiList.counter69(chan69[message.channel.id]))
        
        
    else:

        chan69[message.channel.id] = 0

    if message.content.lower().startswith('!moon'):
        msg = await client.send_message(message.channel,":full_moon:")
        for i in range(8):
            for phase in range(8):
                await asyncio.sleep(0.25)
                await client.edit_message(msg,emojiList.moonPhases[phase])



    if message.content.lower().startswith('!random'):
        randChoice = message.content.split()
        try:
            try:
                print("\n\nGetting random emoji from section " + randChoice[2])

                choices = int(randChoice[2])
                randChoice.remove(str(choices))

            except:
                choices = 1

            finalMsg = ''
            try:
                print("ok let's try that function implementation boyo")
                emojiChoices = emojiList.randEmojis[randChoice[1]](message)
                print("alright we got your function kid")
                hnn = ', '
            except:
                print("function machine broke")
                emojiChoices = list(emojiList.randEmojis[randChoice[1]])
                hnn = '  ' 
            if randChoice[1].lower() == "emoji":
                for i in message.server.emojis:
                    print(i)
                    print(str(i))
                    print('\n\n')
                    emojiChoices += [str(i)]
            
            if choices > len(emojiChoices):
                choices = len(emojiChoices)

            for i in range(choices):
                n = random.choice(emojiChoices)
               
                emojiChoices.remove(n)

                finalMsg += n + hnn
            print(finalMsg)
            finalMsg = finalMsg[:-2]
            await client.send_message(message.channel,finalMsg)



            await client.send_message(message.channel,msg)
        except:
            return ''
    if message.content.lower().startswith('!clean') and message.author.id == "146068146476810240":
        try:
            deleteCount = int(message.content.split()[1])
        except:
            deleteCount = 10
        q = 0
        async for mess in client.logs_from(message.channel):
            if mess.author == client.user:
                await client.delete_message(mess)
                q += 1
            if q >= deleteCount:
                break
    if message.content.lower().startswith('!roll'):
        try:
            roll = message.content.lower().split()[1]
            if roll[0] == 'd':
                roll = '1' + roll
            result = []
            addResult = []
            dLoc = roll.find('d')
            numDice= roll[0:dLoc]
            numSide= roll[dLoc+1:]
            if '+' in roll:
                plusLoc = roll.find('+')
                numAdd = int(roll[plusLoc+1:])
                roll = roll[0:plusLoc]
                numSide = roll[dLoc+1:plusLoc]
            else:
                numAdd = 0
            for i in range(int(numDice)):
                rollResult = random.choice(range(int(numSide)))+1


                result += [rollResult]

            if numAdd == 0:
                addResult = None
                dice = '{} d{}s'.format(numDice,numSide)
            else:
                dice = '{} d{}s+{}'.format(numDice,numSide,numAdd)

            print(result)
            print(sum(result))
            msg = "You rolled " + dice + " and got {}\n{} + {}".format(sum(result)+numAdd,result,numAdd)

            await client.send_message(message.channel,msg)
        except:
            print("Error with rolling dice")

    if message.content.lower().startswith('!roles'):
        print('-------------\nGetting Roles\n-------------')
        for i in message.server.roles:
            print(str(i))

    if message.content.lower().startswith('!perms'):
        print('----------\nUser Perms\n----------')
        for i in iter(message.author.server_permissions):
            print(i)

    if message.content.lower().startswith('!poll'):
        global isPoll
        if isPoll:
            return ''
        pollQuestion = message.content
        try:
            pollTime = int(message.content.split()[1])
            pollQuestion = message.content.replace(str(pollTime),"")


        except:
            pollTime = 30.0
        pollQuestion = pollQuestion.replace('!poll', '')
        await client.send_message(message.channel, 'Poll Started:\n' + pollQuestion + '\nYou have {} seconds to respond\n \nUse !yes or !no to vote'.format(pollTime))

        global yes
        global no
        global userVoted
        isPoll = True

        yes = 0
        no = 0
        userVoted = []
        def pollCheck(n):
            return n.content == '!end'

        endPoll = await client.wait_for_message(timeout=pollTime, author=message.author, check=pollCheck)

        if endPoll is None:
            await client.send_message(message.channel, 'Yes Votes: {}\n No Votes: {}'.format(yes,no))
            if yes > no:
                await client.send_message(message.channel,'The consensus is... Yes.')
            if no > yes:
                await client.send_message(message.channel,'The consensus is... No.')
            if no == yes:
                await client.send_message(message.channel,'The consensus is... A tie.')
            isPoll = False

        elif endPoll.content == '!end':
            await client.send_message(message.channel, 'Yes Votes: {}\n No Votes: {}'.format(yes,no))
            if yes > no:
                await client.send_message(message.channel,'The consensus is... Yes.')
            if no > yes:
                await client.send_message(message.channel,'The consensus is... No.')
            if no == yes:
                await client.send_message(message.channel,'The consensus is... A tie.')
            isPoll = False
    if message.content.lower().startswith('!yes'):



        if  isPoll and message.author not in  userVoted:
             userVoted += [message.author]
             yes += 1

    if message.content.lower().startswith('!no'):



        if  isPoll and message.author not in  userVoted:
             no += 1
             userVoted += [message.author]
    if message.content.lower().startswith('!send') and message.author.id == "146068146476810240":

        channelSend = int(message.content.split()[1])
        print(bcChannels)
        print(channelSend)
        print(bcChannels[channelSend])
        whatev = message.content.split()
        whatev.remove(whatev[0])
        whatev.remove(whatev[0])
        j = ''
        for i in whatev:
            j += i + ' '

        await client.send_message(bcChannels[channelSend],j)

    elif message.content.lower().startswith('!send'):
        print("no bueno, bud")

    if "craxiboo" in message.content.lower():
        await client.send_message(message.author, "Hey, **don't** call him that, " + message.author.mention + ".")

    
"""
    if "has been updated" in message.content.lower():
        print("got what you wanted boss")
        client.pin_message(message)


    au = str(getName(message.author))
    try:
        ch = str(message.channel.name) + ' ' + str(bcChannels.index(message.channel))
    except:
        ch = str(message.channel.name)
    me = str(message.content)
    print(au)
    print(ch)
    print(me)
    print("")
    await client.send_message(logsChannel, "\n{}\n{}\n{}".format(au,ch,me))
"""

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Logs\n\n')

    global bcChannels
    bcServer = client.get_server("326925801528229899")
    bcChannels = list(bcServer.channels)
    for i in bcChannels:
        if (i.type == discord.ChannelType.voice) or not(i.permissions_for(i.server.me).send_messages):
            bcChannels.remove(i)
            print(i)
    bcChannels = sorted(bcChannels, key=lambda channel:channel.position)
    print(bcChannels)

    for i in bcChannels:
        print(i.name + str(bcChannels.index(i)))

    print(bcChannels[1].name)
    print('\n\n')

    global logsChannel
    logsChannel = client.get_channel("327490803897335808")

    def getOnlines(message):
        memsList = []
        for i in message.server.members:
            if i.status != discord.Status.offline:
                memsList += [getName(i)]
        return memsList

    def getMems(message):
        memsList = []
        for i in message.server.members:
            memsList += [getName(i)]
        return memsList

    def getChans(message):
        chanList = []
        for i in message.server.channels:
            chanList += [i.name]
        return chanList

    def getBots(message):
        botList = []
        for i in message.server.members:
            if i.bot:
                botList += [i.name]
        return botList

    

    emojiList.randEmojis["user"] = getMems
    emojiList.randEmojis["online"] = getOnlines
    emojiList.randEmojis["channel"] = getChans
    emojiList.randEmojis["bot"] = getBots


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}! Ignore the Beta 42 bot\'s message, this is a safe and happy place.'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_member_remove(member):
    server = member.server
    fmt = "Goodbye {0.mention}! Hope you enjoyed {1.name}."
    await client.send_message(server, fmt.format(member,server))

client.run("MzI3NDkzNjQ2MzM5NTM4OTQ0.DC2N0w.BoLOfSiZEi_axYISm6XY9RQ4bfE")
logs.close()

'''notes!

my user id:     146068146476810240

                326925801528229899
bc squad id     326925801528229899
bot testing id :327490803897335808

#chat in bcDiscord id = 326925801528229899
'''
