from State import State
from Transition import Transition
from Edge import Edge
from MT import MT

def runArq():
    arquivo = input('digite o nome do arquivo: ')
    with open(arquivo, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    states = []
    final_states = []
    w = ""
    vazio = ""

    for line in lines:
        line = line.strip()
        
        if line.startswith('titulo'):
            exec(f'print("{line.split("=", 1)[1].strip()}")')
        
        elif line.startswith('Q'):
            states = line.split('=')[1].strip('{} ').split(',')
            for state in states:
                exec(f"{state} = State('{state}')")
        
        elif line.startswith('F'):
            final_states = line.split('=')[1].strip('{} ').split(',')
            for state in final_states:
                exec(f"{state}.setFinal()")
        
        elif line.startswith('delta'):
            continue 
        
        elif line.startswith('q'):

            parts = line.split('=')  
            from_state, read_symbol = parts[0].split(',')  
            to_state, write_symbol, direction = parts[1].split(',')  

            exec(f"{from_state}.addTransition({to_state.strip()}, '{read_symbol.strip()}', '{write_symbol.strip()}', '{direction.strip()}')")
        
        elif line.startswith('vazio'):
            vazio = line.split('=')[1].strip('{} ')

        elif line.startswith('w'):
            w = line.split('=')[1].strip().strip("'")
            exec(f"w = '{w}'")
            exec(f"mt = MT({states[0]}, w, max(1,len(w)), '{vazio}')")
            exec("mt.run()")

if __name__ == "__main__": 
    runArq()