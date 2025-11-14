class Pingouin:
    def __init__(self, id, espece, ile, longueur_bec, profondeur_bec, longueur_nageoire, poids, sexe, annee_naissance):
        self.id = id
        self.espece = espece
        self.ile = ile
        self.longueur_bec = longueur_bec
        self.profondeur_bec = profondeur_bec
        self.longueur_nageoire = longueur_nageoire
        self.poids = poids
        self.sexe = sexe
        self.annee_naissance = annee_naissance

    def __str__(self):
        return 'Pingouin {} {} n°={} de l\'île {}, né en {}. ' \
               'Mesures : [longueur_bec={}, profondeur_bec={}, longueur_nageoire={}, ' \
               'poids={}]'.format('femelle' if self.sexe == 'female' else 'male', self.espece, self.id,
                                  self.ile, self.annee_naissance, self.longueur_bec, self.profondeur_bec,
                                  self.longueur_nageoire, self.poids)
