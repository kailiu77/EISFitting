MODEL_META_INDUCTANCE = 0
MODEL_META_ZARC_INDUCTANCE = 1
MODEL_META_WARBURG_INCEPTION = 2
MODEL_META_ZARC = 3
NUMBER_OF_ZARC = 3
NUMBER_OF_PARAM = 1 + 1 + NUMBER_OF_ZARC + 1 + 1 + 1 + NUMBER_OF_ZARC + 1 + NUMBER_OF_ZARC + 1 + 1



INDEX_R = 0
INDEX_R_ZARC_INDUCTANCE = 1
INDEX_R_ZARC_OFFSET = INDEX_R_ZARC_INDUCTANCE + 1
INDEX_Q_WARBURG = INDEX_R_ZARC_OFFSET + NUMBER_OF_ZARC
INDEX_Q_INDUCTANCE = INDEX_Q_WARBURG + 1
INDEX_W_C_INDUCTANCE = INDEX_Q_INDUCTANCE + 1
INDEX_W_C_ZARC_OFFSET = INDEX_W_C_INDUCTANCE + 1
INDEX_PHI_WARBURG = INDEX_W_C_ZARC_OFFSET + NUMBER_OF_ZARC
INDEX_PHI_ZARC_OFFSET = INDEX_PHI_WARBURG + 1
INDEX_PHI_INDUCTANCE = INDEX_PHI_ZARC_OFFSET + NUMBER_OF_ZARC
INDEX_PHI_ZARC_INDUCTANCE = INDEX_PHI_INDUCTANCE + 1