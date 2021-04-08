import math

class Particula:

    def __init__(self, x_atual, y_atual, velocidade_x, velocidade_y):
        self.x_atual = x_atual
        self.y_atual = y_atual
        
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

        self.valor_fitness = None

        self.x_best = x_atual
        self.y_best = y_atual
    
    
    def calcula_aptidao(self):
        return -(self.y_atual + 47) * math.sin(  abs(((self.x_atual/2) + (self.y_atual + 47))) ** (1/2) ) -self.x_atual * math.sin(  ( abs(self.x_atual - (self.y_atual + 47)) ** (1/2) )   )

    def set_x_y_best(self, x_best, y_best):
        self.x_best = x_best
        self.y_best = y_best
    
    def set_valor_fitness(self, valor_fitness):
        self.valor_fitness = valor_fitness
    
    def get_valor_fitness(self):
        return self.valor_fitness
        
    def set_velocidade_x(self, velocidade):
        self.velocidade_x = velocidade
    
    def set_velocidade_y(self, velocidade):
        self.velocidade_y = velocidade