import random

alphabet = list("abcdefghijklmnopqrstuvwxyz")

complete_words = sorted(['gapings', 'graping', 'loathes', 'matters', 'oranges', 'abated', 'abates', 'abided', 'abides', 'aflame', 'agates', 'amidst', 'antics', 'arider', 'astray', 'bassos', 'bather', 'bathes', 'bladed', 'blades', 'blamed', 'blamer', 'blames', 'blinks', 'bowing', 'braids', 'brands', 'brandy', 'brides', 'brinks', 'busing', 'camels', 'cameos', 'canted', 'canton', 'cantor', 'cantos', 'cheats', 'chicks', 'chided', 'chides', 'chinks', 'chinos', 'clamps', 'classy', 'clinks', 'cramps', 'cranks', 'cranky', 'crated', 'crater', 'crates', 'discos', 'drinks', 'elapse', 'elated', 'elates', 'elites', 'espies', 'finery', 'finest', 'flamed', 'flames', 'flashy', 'franks', 'fusing', 'gaping', 'glades', 'glands', 'glassy', 'grants', 'grasps', 'grated', 'grater', 'grates', 'haters', 'hawing', 'heaths', 'irater', 'japing', 'lamest', 'lapsed', 'lapses', 'lassos', 'laxest', 'liters', 'llamas', 'lowing', 'manses', 'mantes', 'mantis', 'marshy', 'matted', 'matter', 'mattes', 'mawing', 'mayors', 'mowing', 'musing', 'opined', 'opines', 'orange', 'orated', 'orates', 'palest', 'panels', 'panted', 'papaws', 'parkas', 'parsec', 'parsed', 'parses', 'pastas', 'pasted', 'pastel', 'pastes', 'pipers', 'pirate', 'plaids', 'plated', 'platen', 'plates', 'pranks', 'prated', 'prates', 'prided', 'prides', 'raided', 'ranged', 'ranger', 'ranges', 'ranted', 'raping', 'riders', 'rowing', 'sawing', 'scampi', 'scamps', 'scants', 'scanty', 'scrams', 'shaded', 'shades', 'shamed', 'shames', 'shandy', 'sheath', 'sinews', 'sinewy', 'singed', 'singer', 'singes', 'slates', 'slider', 'slides', 'slinks', 'slinky', 'smarts', 'smiled', 'smiles', 'sowing', 'spanks', 'spared', 'sparer', 'spares', 'sparks', 'sparse', 'spasms', 'spates', 'spawns', 'spines', 'spinet', 'spited', 'spites', 'splays', 'sprays', 'stamps', 'stanks', 'sticks', 'sticky', 'stings', 'stingy', 'stints', 'strays', 'swanks', 'swanky', 'swines', 'swings', 'tamers', 'tangos', 'taping', 'tinged', 'tinges', 'towing', 'tramps', 'trashy', 'twined', 'twines', 'united', 'unites', 'vowing', 'waders', 'whited', 'whiten', 'whiter', 'whites', 'withed', 'withes', 'yawing', 'abash', 'abate', 'abide', 'adzes', 'agate', 'aided', 'aides', 'amass', 'amids', 'anted', 'antes', 'antic', 'antis', 'apart', 'aping', 'awash', 'aways', 'awing', 'bands', 'bandy', 'baned', 'banes', 'bangs', 'banks', 'basks', 'bassi', 'basso', 'bated', 'bates', 'bathe', 'baths', 'beats', 'bided', 'bides', 'bidet', 'binds', 'bites', 'blabs', 'blade', 'blame', 'bland', 'blink', 'boats', 'braid', 'brand', 'brash', 'brats', 'brays', 'bride', 'brink', 'camel', 'cameo', 'camps', 'campy', 'caned', 'canes', 'canto', 'cants', 'casks', 'chats', 'cheat', 'chick', 'chide', 'china', 'chink', 'chino', 'chins', 'chips', 'chits', 'clamp', 'clams', 'claps', 'clash', 'class', 'claws', 'clink', 'coats', 'cramp', 'crams', 'crank', 'crash', 'crate', 'dados', 'dames', 'damns', 'damps', 'dated', 'dates', 'dined', 'diner', 'dines', 'dingo', 'dings', 'dingy', 'dinky', 'disco', 'discs', 'disks', 'drama', 'drams', 'drank', 'drays', 'drink', 'eking', 'elate', 'elite', 'faded', 'fades', 'fangs', 'fared', 'fares', 'farms', 'farts', 'fated', 'fates', 'faxed', 'faxes', 'feats', 'finds', 'fined', 'finer', 'fines', 'finks', 'flags', 'flame', 'flaps', 'flash', 'flaws', 'flays', 'flits', 'frank', 'frats', 'frays', 'gasps', 'gated', 'gates', 'glade', 'glads', 'gland', 'glass', 'goats', 'grams', 'grant', 'grasp', 'grate', 'grays', 'grids', 'hands', 'handy', 'hasps', 'hated', 'hater', 'hates', 'hawks', 'heath', 'heats', 'hided', 'hides', 'irate', 'jambs', 'jinni', 'jinns', 'kinda', 'kinds', 'kings', 'kinks', 'kinky', 'kited', 'kites', 'kiths', 'knits', 'laded', 'laden', 'lades', 'lamas', 'lambs', 'lamed', 'lamer', 'lames', 'lamps', 'lands', 'lapse', 'lasso', 'later', 'latex', 'lawns', 'laxes', 'links', 'liter', 'lites', 'llama', 'loath', 'maids', 'manes', 'manse', 'mares', 'marks', 'marsh', 'marts', 'masks', 'masts', 'mated', 'mates', 'matte', 'matts', 'maxed', 'maxes', 'mayor', 'meats', 'meaty', 'miler', 'miles', 'milks', 'milky', 'mills', 'minks', 'moats', 'neath', 'oaths', 'obits', 'oinks', 'opals', 'opine', 'orate', 'owing', 'paled', 'paler', 'pales', 'palls', 'palms', 'palmy', 'palsy', 'panel', 'panes', 'pangs', 'pansy', 'pants', 'panty', 'papal', 'papas', 'papaw', 'pared', 'pares', 'parka', 'parks', 'parse', 'parts', 'party', 'pasta', 'paste', 'pasts', 'pasty', 'pates', 'paths', 'patsy', 'pawls', 'pawns', 'piers', 'pined', 'pines', 'pings', 'pinks', 'pinky', 'pinto', 'pints', 'piped', 'piper', 'pipes', 'pithy', 'plaid', 'plate', 'plays', 'prank', 'prate', 'prays', 'pride', 'raids', 'ramps', 'range', 'rangy', 'ranks', 'rants', 'rasps', 'raspy', 'rated', 'rates', 'rider', 'rides', 'rinks', 'sands', 'sandy', 'sassy', 'sated', 'sates', 'saxes', 'scads', 'scamp', 'scams', 'scans', 'scant', 'scats', 'scram', 'seats', 'shade', 'shads', 'shady', 'shags', 'shahs', 'shame', 'shams', 'shied', 'shies', 'shims', 'ships', 'shits', 'sinew', 'singe', 'sings', 'sinks', 'sited', 'sites', 'skids', 'skins', 'skits', 'slabs', 'slags', 'slams', 'slaps', 'slash', 'slate', 'slays', 'slide', 'slink', 'slits', 'smart', 'smash', 'smile', 'snits', 'spank', 'spans', 'spare', 'spark', 'spars', 'spasm', 'spate', 'spats', 'spawn', 'spays', 'spied', 'spies', 'spine', 'spins', 'spiny', 'spite', 'spits', 'splay', 'spray', 'stamp', 'stank', 'stats', 'stick', 'sties', 'sting', 'stint', 'stray', 'swank', 'swans', 'swash', 'sways', 'swine', 'swing', 'tamed', 'tamer', 'tames', 'tamps', 'tango', 'tangs', 'tangy', 'tanks', 'tansy', 'tasks', 'taxed', 'taxes', 'taxis', 'teats', 'thaws', 'ticks', 'tiers', 'tined', 'tines', 'tinge', 'tings', 'tints', 'tipsy', 'tramp', 'trams', 'trash', 'trays', 'twine', 'twins', 'twits', 'unite', 'units', 'unity', 'using', 'vamps', 'vanes', 'waded', 'wader', 'wades', 'wadis', 'wands', 'waned', 'wanes', 'wants', 'wasps', 'waxed', 'waxes', 'whams', 'whats', 'wheat', 'whims', 'whips', 'white', 'whits', 'winds', 'windy', 'wined', 'wines', 'wings', 'winks', 'winos', 'withe', 'withs', 'yawls', 'yawns', 'adds', 'adze', 'afar', 'ahas', 'aide', 'aids', 'akin', 'alit', 'amid', 'amps', 'ands', 'ante', 'anti', 'ants', 'arid', 'ashy', 'asks', 'asps', 'ates', 'away', 'axed', 'axes', 'ayes', 'bade', 'bahs', 'band', 'bane', 'bang', 'bani', 'bank', 'bans', 'bash', 'bask', 'bass', 'bate', 'bath', 'bats', 'bays', 'beat', 'bide', 'bids', 'bind', 'bins', 'bite', 'bits', 'blab', 'boat', 'bran', 'brat', 'bray', 'cads', 'came', 'camp', 'cams', 'cane', 'cans', 'cant', 'cash', 'cask', 'cats', 'chat', 'chic', 'chid', 'chin', 'chip', 'chit', 'clad', 'clam', 'clap', 'claw', 'clay', 'coat', 'cram', 'dado', 'dads', 'dame', 'damn', 'damp', 'dams', 'dash', 'date', 'days', 'dine', 'ding', 'dins', 'dint', 'disc', 'dish', 'disk', 'diss', 'dram', 'dray', 'eats', 'fade', 'fads', 'fags', 'fang', 'fans', 'fare', 'farm', 'fart', 'fate', 'fats', 'feat', 'find', 'fine', 'fink', 'fins', 'fits', 'flab', 'flag', 'flap', 'flaw', 'flax', 'flay', 'flit', 'frat', 'fray', 'gads', 'gash', 'gasp', 'gate', 'gays', 'gins', 'glad', 'goat', 'gram', 'gray', 'grid', 'hags', 'hahs', 'hams', 'hand', 'hash', 'hasp', 'hate', 'hath', 'hats', 'hawk', 'haws', 'hays', 'heat', 'hide', 'hied', 'hies', 'hims', 'hips', 'hiss', 'hits', 'inks', 'inky', 'inns', 'isms', 'jamb', 'jams', 'jays', 'jinn', 'kids', 'kind', 'king', 'kink', 'kins', 'kite', 'kith', 'kits', 'knit', 'labs', 'lade', 'lads', 'lady', 'lags', 'laid', 'lama', 'lamb', 'lame', 'lamp', 'lams', 'land', 'laps', 'lash', 'lass', 'late', 'lawn', 'laws', 'lays', 'lids', 'link', 'lite', 'made', 'maid', 'mane', 'mans', 'many', 'maps', 'mare', 'mark', 'mars', 'mart', 'mash', 'mask', 'mass', 'mast', 'mate', 'math', 'mats', 'matt', 'maws', 'mayo', 'meat', 'mild', 'mile', 'milk', 'mill', 'mils', 'mink', 'mixt', 'moat', 'nays', 'neat', 'nits', 'oath', 'oats', 'obit', 'oink', 'opal', 'pads', 'paid', 'pale', 'pall', 'palm', 'pals', 'pane', 'pang', 'pans', 'pant', 'papa', 'paps', 'pare', 'park', 'pars', 'part', 'pass', 'past', 'pate', 'path', 'pats', 'pawl', 'pawn', 'paws', 'pays', 'peat', 'pied', 'pier', 'pies', 'pigs', 'pine', 'ping', 'pink', 'pins', 'pint', 'pipe', 'pips', 'piss', 'pita', 'pith', 'pits', 'pity', 'play', 'pram', 'pray', 'raid', 'ramp', 'rams', 'rang', 'rank', 'rant', 'rash', 'rasp', 'rate', 'rats', 'rays', 'ride', 'rids', 'rink', 'said', 'sand', 'sash', 'sass', 'sate', 'says', 'scad', 'scam', 'scan', 'scat', 'seat', 'shad', 'shag', 'shah', 'sham', 'shat', 'shim', 'ship', 'shit', 'sine', 'sing', 'sink', 'sins', 'site', 'sits', 'skid', 'skin', 'skit', 'slab', 'slag', 'slam', 'slap', 'slaw', 'slay', 'slid', 'slit', 'snit', 'span', 'spar', 'spas', 'spat', 'spay', 'spin', 'spit', 'swan', 'sway', 'tads', 'tame', 'tamp', 'tams', 'tang', 'tank', 'tans', 'task', 'tats', 'taxi', 'teat', 'that', 'thaw', 'this', 'tick', 'tics', 'tied', 'tier', 'ties', 'tine', 'ting', 'tins', 'tint', 'tiny', 'tips', 'tits', 'tram', 'tray', 'twin', 'twit', 'unit', 'vamp', 'vane', 'vans', 'vats', 'wade', 'wadi', 'wads', 'wand', 'wane', 'want', 'wash', 'wasp', 'waxy', 'ways', 'wham', 'what', 'whim', 'whip', 'whit', 'wind', 'wine', 'wing', 'wink', 'wino', 'wins', 'wite', 'with', 'wits', 'yaks', 'yams', 'yaps', 'yawl', 'yawn', 'yaws', 'zany', 'zits', 'add', 'ado', 'ads', 'adz', 'aha', 'aid', 'amp', 'and', 'ani', 'ant', 'any', 'ash', 'ask', 'asp', 'ass', 'ate', 'axe', 'aye', 'bad', 'bah', 'ban', 'bat', 'bay', 'bid', 'bin', 'bit', 'cad', 'cam', 'can', 'cat', 'chi', 'dad', 'dam', 'day', 'did', 'din', 'dis', 'eat', 'fad', 'fag', 'fan', 'far', 'fat', 'fax', 'fin', 'fit', 'gad', 'gas', 'gay', 'gin', 'had', 'hag', 'hah', 'ham', 'has', 'hat', 'haw', 'hay', 'hid', 'hie', 'him', 'hip', 'his', 'hit', 'ids', 'ifs', 'ink', 'inn', 'ins', 'ism', 'its', 'jam', 'jay', 'kid', 'kin', 'kit', 'lab', 'lad', 'lag', 'lam', 'lap', 'law', 'lax', 'lay', 'lid', 'lit', 'mad', 'man', 'map', 'mar', 'mas', 'mat', 'maw', 'may', 'mid', 'mil', 'mix', 'nay', 'nit', 'oat', 'pad', 'pal', 'pan', 'pap', 'par', 'pas', 'pat', 'paw', 'pay', 'pie', 'pig', 'pin', 'pip', 'pis', 'pit', 'ram', 'ran', 'rat', 'ray', 'rid', 'sad', 'sat', 'sax', 'say', 'sin', 'sis', 'sit', 'spa', 'tad', 'tam', 'tan', 'tat', 'tax', 'tic', 'tie', 'tin', 'tip', 'tit', 'van', 'vat', 'wad', 'wan', 'was', 'wax', 'way', 'win', 'wit', 'yak', 'yam', 'yap', 'yaw', 'zit', 'ad', 'ah', 'am', 'an', 'as', 'at', 'ax', 'ay', 'fa', 'ha', 'hi', 'id', 'if', 'in', 'is', 'it', 'la', 'ma', 'mi', 'pa', 'pi', 'ti', 'ya', 'a', 'i'])


def binary_search(array, start, stop, item):
    middle = (start+stop)/2
    if stop < start:
        return -1
    if array[middle] > item:
        return binary_search(array, start, middle-1, item)
    if array[middle] < item:
        return binary_search(array, middle+1, stop, item)
    return middle

def sorted_insert(array, item):
    if binary_search(array, 0, len(array)-1, item) >= 0:
        return array
    for index, word in enumerate(array): #The array will be small enough that sequential is close enough
        if word > item:
            array.insert(index, item)
            return array
    array.append(item)
    return array


with open("C:\Users\Calvin\Documents\PracticeCode\python\words.txt", "r") as f:
    words = [i.strip() for i in f.readlines()]
    counter = 0
    while True:
        counter += 1
        string = random.choice(['a', 'i'])
        pos = 0
        while pos >= 0:
            next_letter = random.choice(alphabet)
            if random.randint(0, 1):
                pos = binary_search(words, pos, len(words)-1, string + next_letter)
                if pos >= 0:
                    string = string + next_letter
            else:
                pos = binary_search(words, 0, len(words)-1, next_letter + string)
                if pos >= 0:
                    string = next_letter + string
        complete_words = sorted_insert(complete_words, string)
        if counter % 100000 == 0:
            print sorted(complete_words, key=len, reverse=True)
            print len(complete_words)
            print counter
        if len(string) > 5:
            print string