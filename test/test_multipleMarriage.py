
import sys
import os.path

import lark
from nose.tools import assert_equals

from gedcom.validate.incest import validate_incest
from gedcom.transformer import GedcomTransformer
from gedcom.models import *

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


