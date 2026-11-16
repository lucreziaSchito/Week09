from dataclasses import dataclass

@dataclass
class Film:
    id: int
    titolo: str
    genere: str
    serata: int
    numero_voti: int
    somma_voti: float

    @property
    def media(self):
        return self.somma_voti / self.numero_voti

    def __str__(self):
        return f'{self.serata:02d}. {self.id} {self.titolo} - {self.genere} - voto medio {self.media:.2f}'
