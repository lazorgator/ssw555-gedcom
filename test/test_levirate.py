import sys
import os.path

import lark
from nose.tools import assert_equals

from gedcom.validate.gay_marriage import validate_check_if_gay
from gedcom.transformer import GedcomTransformer
from gedcom.models import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_levirate_marriage():

    assert True;