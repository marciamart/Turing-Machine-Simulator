from Edge import Edge
from Transition import Transition

class State:
    def __init__(self, name: str):
        self.name = name
        self.isFinal = False
        self.transitions = []

    def getName(self): return self.name
	
    def setFinal(self): self.isFinal = True

    def addTransition(self, state, read, write: str, d: str):
        return self.addTransitions(state, Edge.instance(read), write=write, d=d)

    def addTransitions(self, state, *edges, write, d):
        for edge in edges:
            transition = Transition(state, edge, write, d)
            if transition in self.transitions: 
                continue
            self.transitions.append(transition)
        return self

    def transition(self, _c: str):
        for t in self.transitions:
            e = t.getEdge()
            if e.getC()!=None and e.getC()==_c:
                return t
        return None
    
    def equals(self, s):
        if isinstance(s, State):
            return s.getName()==self.getName()
        return False
    
    def hashCode(self):
        return hash(self.getName())