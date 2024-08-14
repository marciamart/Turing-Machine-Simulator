class Transition:
    def __init__(self, state, edge, write:str, direction:str):
        self.state = state
        self.edge = edge
        self.write = write
        self.direction = direction

    def getEdge(self): return self.edge
    def getState(self): return self.state
    def getWrite(self): return self.write
    def getDirection(self): return self.direction

    def equals(self, t):
        if isinstance(t, Transition):
            return t.getEdge().equals(self.edge) and t.getState().equals(self.state)
        return False

    def hashCode(self):
        hc = self.state.hashCode() if self.state != None else 0
        hc = 47 * hc +  (self.edge.hashCode() if self.edge != None else 0)
        return hc

    def __repr__(self):
        return f'{self.edge} --> {self.state.getName()}'