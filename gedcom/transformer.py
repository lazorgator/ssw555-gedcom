import datetime

import lark

from .models import *


_MONTH_MAP = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP',
              'OCT', 'NOV', 'DEC']


class GedcomTransformer(lark.Transformer):
    def indi_stmt(self, tokens):
        return Individual.from_tokens(tokens)

    def fam_stmt(self, tokens):
        return Family.from_tokens(tokens)

    def birt_stmt(self, tokens):
        (_, date) = tokens
        return Birth(date)

    def deat_stmt(self, tokens):
        (_, date) = tokens
        return Death(date)

    def date_stmt(self, tokens):
        (_, t_day, t_month, t_year) = tokens
        return datetime.date(year=int(t_year.value),
                             month=_MONTH_MAP.index(t_month.value) + 1,
                             day=int(t_day.value))

    def famc_stmt(self, tokens):
        (_, fid) = tokens
        return FamilyChild(fid.value)

    def fams_stmt(self, tokens):
        (_, fid) = tokens
        return FamilySpouse(fid.value)

    def name_stmt(self, tokens):
        (_, first, last) = tokens
        return Name(first.value, last.value)

    def sex_stmt(self, tokens):
        (_, sex) = tokens
        return Sex(sex.value)

    def marr_stmt(self, tokens):
        (_, date) = tokens
        return Marriage(date)

    def husb_stmt(self, tokens):
        (_, id) = tokens
        return Husband(id.value)

    def wife_stmt(self, tokens):
        (_, id) = tokens
        return Wife(id.value)

    def div_stmt(self, tokens):
        (_, date) = tokens
        return Divorce(date)

    def chil_stmt(self, tokens):
        (_, id) = tokens
        return Child(id.value)

    def note_stmt(self, tokens):
        (_, note) = tokens
        return Note(note.value)
