"""Deseja-se armazenar as informações dos projetos integradores desenvolvidos por alunos de
ensino médio. Um projeto integrador (PI) contém título, ano, nomes dos alunos e nomes
dos professores orientadores. Cada aluno pertence a uma turma (por exemplo: técnico em
informática integrado 301) e cada professor orientador atua em uma ou mais áreas (por
exemplo: educação física, nutrição e competição esportiva). Cada área de atuação possui
periódicos e eventos apropriados para publicação de artigos que possam ser produzidos
a partir dos PI’s. Periódicos são produzidos por uma editora e possuem ISSN, enquanto
eventos são realizados anualmente e ocorrem em um local específico. Artigos apresentados
em eventos são publicados nos anais do evento. Modele as classes necessárias para armazenar
as informações dos PI’s"""

class Projeto_Integrador():
    def __init__(self, titulo, ano, alunos, prof_orientadores):
        self.titulo = titulo
        self.ano = ano
        self.alunos = alunos
        self.profs_orientadores = prof_orientadores

class Aluno():
    def __init__(self, nome, turma):
        self.nome = nome
        self.turma = turma

class Professor():
    def __init__(self, nome, areas):
        self.nome = nome
        self.areas = areas

class Area():
    def __init__(self, nome, periodico, evento):
        self.nome = nome 
        self.periodico = periodico
        self.evento = evento 

class Periodico():
    def __init__(self, nome, editora, issn):
        self.nome = nome 
        self.editora = editora
        self.issn = issn

class Evento():
    def __init__(self, nome, local, anais_do_evento):
        self.nome = nome
        self.local = local 
        self.anais_do_evento = anais_do_evento

class Anais_do_Evento():
    def __init__(self, nome, artigos): 
        self.nome = nome
        self.artigos = artigos
"""if __name__ == "__main__":
a=""" 