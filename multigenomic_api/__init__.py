import mongoengine

from .services import evidences
from .services import external_cross_references
from .services import genes
from .services import motifs
from .services import operons
from .services import organisms
from .services import products
from .services import promoters
from .services import publications
from .services import regulatory_complexes
from .services import regulatory_continuants
from .services import regulatory_interactions
from .services import sigma_factors
from .services import terms
from .services import terminators
from .services import transcription_factors
from .services import regulatory_sites
from .services import transcription_units
from .services import regulators


def connect(database, uri):
    mongoengine.connect(database, host=uri, authSource="admin")


def disconnect():
    mongoengine.disconnect()

