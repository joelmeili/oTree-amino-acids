from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Joël Meili'

doc = """
Amino acids quiz / BIO117
"""

import random

class Constants(BaseConstants):
    name_in_url = 'amino_acids'
    players_per_group = None
    num_rounds = 20

    amino_acids = ["glycine", "alanine", "valine", "leucine",
    "isoleucine", "proline", "serine", "threonine", "cysteine",
    "methionine", "asparagine", "glutamine", "lysine", "arginine",
    "histidine", "aspartate", "glutamate", "phenylalanine",
    "tyrosine", "tryptophan"]

class Subsession(BaseSubsession):
    def creating_session(self):
        amino_acids = Constants.amino_acids.copy()
        random.shuffle(amino_acids)
        for p in self.get_players():
            p.participant.vars['amino_acids'] = amino_acids

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass
