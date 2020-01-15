"""
Main module, defining functions for generating light novel titles.
Lots of ugly lambdas to simulate laziness xd
"""
import sys
import random


def pluralize(noun):
    """Pluralize a given noun string."""
    if noun.endswith(("x", "s")):
        return noun + "es"
    if noun.endswith("y"):
        return noun[:-1] + "ies"
    return noun + "s"


def get_noun():
    """Pick a random noun."""
    return random.choice(
        [
            lambda: "House",
            lambda: "Sister",
            lambda: "Index",
            lambda: "Fantasy",
            lambda: "Game",
            lambda: "NEET",
            lambda: "Angel",
            lambda: "Girl",
            lambda: "Father",
            lambda: "Apocalypse",
            lambda: "Demon Lord",
            lambda: "War",
            lambda: "Magic System",
            lambda: "Library",
            lambda: "Truck",
            lambda: "Sword Master",
            lambda: "MMO",
            lambda: "Box",
            lambda: "Alchemist",
            lambda: "Magician",
        ]
    )


def get_adjective(plural=False):
    """Pick a random adjective."""
    return random.choice(
        [
            lambda: "Fair",
            lambda: "Nice",
            lambda: "Cute",
            lambda: "Certain",
            lambda: "Brilliant",
            lambda: "Realist",
            lambda: "Lost",
            lambda: "Irregular",
            lambda: "Crazy",
            lambda: "Dark",
            lambda: "Horrible",
            lambda: "Whiny",
            lambda: "Delicious",
            lambda: "Seductive",
            lambda: "Wandering",
            lambda: "Youthful",
        ]
        + (
            [
                lambda: "Too Many",
                lambda: "Whole Bunch Of",
                lambda: "Tons Of",
                lambda: "Numerous",
            ]
            if plural
            else []
        )
    )


def get_past_participle(target=False):
    """Pick a random past participle verb."""
    return random.choice(
        [
            lambda: "Caused",
            lambda: "Created",
            lambda: "Summoned",
            lambda: "Bumped Into",
            lambda: "Got Reincarnated As",
            lambda: "Moved Out With",
            lambda: "Fell In Love With",
            lambda: "Started Seeing",
            lambda: "Fell In Bed With",
            lambda: "Rebuilt",
        ]
        if target
        else [
            lambda: "Saved",
            lambda: "Ate",
            lambda: "Died",
            lambda: "Got Reincarnated",
            lambda: "Was Killed",
            lambda: "Got Eaten",
        ]
    )


def get_present_continuous(target=False):
    """Pick a random present continuous verb."""
    return random.choice(
        [
            lambda: "Slaying",
            lambda: "Falling In Love With",
            lambda: "Wandering With",
            lambda: "Travelling With",
            lambda: "Falling In Love With",
            lambda: "Picking Up",
        ]
        if target
        else [
            lambda: "Eating",
            lambda: f"Sleeping And {get_present_continuous()()}",
            lambda: "Killing",
            lambda: "Hunting",
            lambda: "Loving",
        ]
    )


def get_infinitive(target=False):
    """Pick a random infinitive verb."""
    return random.choice(
        [
            lambda: "Eat",
            lambda: "Pick Up",
            lambda: "Summon",
            lambda: "Overcome",
            lambda: "Look At",
            lambda: "Love",
            lambda: "Start Life Again With",
            lambda: "Miss",
            lambda: "Make",
            lambda: "Create",
            lambda: "Play With",
        ]
        if target
        else [
            lambda: "Eat",
            lambda: "Meditate",
            lambda: "Sleep",
            lambda: "Start Life Again",
            lambda: "Cry",
        ]
    )


def get_suffix():
    """Generate a random suffix clause."""
    return random.choice(
        [
            lambda: f"With A {get_adjective()()} {get_noun()()}",
            lambda: f"In Fact {get_action()()}",
            lambda: f"Without The {get_adjective()()} {get_noun()()}",
            lambda: f"And So {get_action()()}",
            lambda: f"And It Was {get_adjective()()}",
            lambda: f"But Whatever, {get_action()()}",
            lambda: f"So Why Do {pluralize(get_noun()())} Keep {get_present_continuous(target=True)()} Me?",
        ]
    )


def get_prefix():
    """Generate a random prefix clause."""
    return random.choice(
        [
            lambda: f"If It's For My {get_noun()()},",
            lambda: f"Is It Wrong That",
            lambda: f"I've Been {get_present_continuous()()} And",
            lambda: f"How Not To {get_infinitive(target=True)()} {pluralize(get_noun()())}:",
            lambda: f"I Keep {get_present_continuous()()} And",
            lambda: f"I Love To {get_infinitive()()} But",
            lambda: f"Didn't I Say",
            lambda: f"It's Not {get_adjective()()} That",
            lambda: f"Suppose",
            lambda: f"That Time",
            lambda: f"So What",
        ]
    )


def get_action():
    """Generate an action sentence."""
    return random.choice(
        [
            lambda: f"I {get_past_participle(target=True)()} A {get_adjective()()} {get_noun()()}",
            lambda: f"I {get_infinitive()()} A Lot",
            lambda: f"I'm {get_present_continuous(target=False)()}",
            lambda: f"A {get_adjective()()} {get_noun()()} {get_past_participle(target=True)()} Me",
            lambda: f"I'd Even {get_infinitive(target=True)()} A {get_adjective()()} {get_noun()()}",
            lambda: f"I {get_past_participle(target=True)()} {get_adjective(plural=True)()} {pluralize(get_noun()())}",
            lambda: f"My {get_adjective()()} {get_noun()()} Is {get_adjective()()}",
            lambda: f"You {get_past_participle(target=True)()} Some {get_adjective()()} {pluralize(get_noun()())}",
            lambda: f"I Can't {get_infinitive(target=True)()} You",
            lambda: f"I Got {get_past_participle()()} By A {get_adjective()()} {get_noun()()}",
        ]
    )


def get_title():
    """Generate a random title."""
    return lambda: f"{get_prefix()()} {get_action()()} {get_suffix()()}".replace(
        "Picking Up Me", "Picking Me Up"
    )


def run():
    """Run the program, generating a number of titles and printing them to stdout."""
    count = 1
    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    print("\n\n".join(get_title()() for _ in range(count)))


if __name__ == "__main__":
    run()
