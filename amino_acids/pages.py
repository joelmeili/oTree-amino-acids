from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class AminoAcid(Page):

    def vars_for_template(self):
        return dict(
            image_path = "amino_acids/{}.png".format(self.player.participant.vars['amino_acids'][self.round_number - 1]),
            amino_acid = self.player.participant.vars['amino_acids'][self.round_number - 1]
        )

page_sequence = [AminoAcid]