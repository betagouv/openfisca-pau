 # -*- coding: utf-8 -*-
from openfisca_france.model.base import *  # noqa analysis:ignore

from numpy import (logical_not as not_)


class residence_pau(Variable):
    value_type = bool
    entity = Individu
    definition_period = MONTH
    label = u"Le lieu de résidence est Pau"

    def formula(individu, period):
        code_insee_commune = individu.menage('depcom', period)
        return code_insee_commune == '64445'


class pau_transport_tarification_solidaire(Variable):
    value_type = float
    entity = Individu
    definition_period = MONTH
    label = u"Tarification solidaire des transports de la ville de Pau"

    def formula(individu, period, parameters):
        return 29 * individu('residence_pau', period)
