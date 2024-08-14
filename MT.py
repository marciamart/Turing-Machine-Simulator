from State import State
class MT: #MT = (Q, Σ, Γ, q0, F, δ)
    def __init__(self, q: State, w: str, _range: int, symbol_vazio: str):
        self.q = q
        self.w = w
        self.symbol_vazio = symbol_vazio

        self.set_fita(_range)
        self.init_fita(w)

    def run(self):
        if(self.q==None or self.w==None): return False

        while True:
            transition = self.q.transition(self.fita[self.current])
            if transition != None:
                qNext = transition.getState()
                write = transition.getWrite()
                direction = transition.getDirection()

                self.fita[self.current] = write
                self.move_fita(direction)

                print(f'{self.q.getName()} ({self.fita[self.current]}) -> {qNext.getName()} GRAVA:{write} POSICAO:{direction}-ATUAL:{self.current}  ')
                self.q = qNext
                print(self.fita)
            else:
                break
        print(self.q.getName())
        return self.print_result()
    
    def move_fita(self, direction: str):
        if direction == 'D':
            self.current += 1
        elif direction == 'E':
            self.current -= 1
        else:
            self.current = self.current
    
    def print_result(self):
        if(self.q.isFinal):
            print(f'Reconheceu: {self.w}')
        else:
            print(f'Nao reconheceu: {self.w}')
        return self.q.isFinal


    def init_fita(self, w):
        for a in list(w):
            self.fita[self.current] = a
            self.current += 1
        
        self.current = self.range

        print(f'{self.fita}\nLEN: {len(self.fita)}\nMAX: {self.max}')
        print(f'current -> {self.current}')
    
    def set_fita(self, _range):
        self.fita = []
        self.range = _range
        self.max = self.range*3

        for i in range(1, self.max+1):
            self.fita.append(self.symbol_vazio)
        
        self.current = self.range
        self.max = self.max