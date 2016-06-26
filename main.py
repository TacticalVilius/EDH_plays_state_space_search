from copy import deepcopy
from random import shuffle
from goals import PlayTypeByTurn
from deck_builder import DeckBuilder
from max_heap import MaxHeap
from state import State

def generate_children(state):
    children = []
    add_if_not_none(generate_mana(state), children)
    add_if_not_none(play_cards(state), children)
    add_if_not_none(next_turn(state), children)
    
    return children
    
def generate_mana(state):
    new_state = state.tap_all_for_mana()
    if new_state:
        return [new_state]
    else:
        return None
    
def play_cards(state):
    new_states = []
    for card in state.get_playable_cards():
        new_state = state.play_card(card.name)
        new_states.append(new_state)
    return new_states if len(new_states) > 0 else None

def next_turn(state):
    new_state = state.new_turn()
    new_state.parent = state
    return [new_state] if new_state else None
    
def add_if_not_none(list, original_list):
    if list is not None:
        original_list += list

def init_state():
    deck = DeckBuilder('slapia-zole-v2.txt').get_deck()
    shuffle(deck)
    hand = deck[len(deck)-7:]
    library = deck[:len(deck)-7]
    return State(library, hand, [], 'game start', None)

def main():
    frontier = MaxHeap()
    goal = PlayTypeByTurn('Snake', 5)
    
    initial_state = init_state()
    frontier.insert((initial_state, goal.score_func(initial_state)))
    
    goal_state = None
    while frontier.size() > 0:
        best_candidate = frontier.extract()
        print("current candidate: " + str(best_candidate[1]) + " " + best_candidate[0].describe())
        if goal.goal_func(best_candidate[0]):
            goal_state = best_candidate[0]
            break
        frontier.insert_list([entry for entry in [(child, goal.score_func(child)) for child in generate_children(best_candidate[0])] if entry[1] > 0])
    
    if not goal_state:
        print('Goal unachievable')
        return
    
    current = goal_state
    goal_to_start = [current]
    while current.parent:
        current = current.parent
        goal_to_start.append(current)
    
    for state in goal_to_start[::-1]:
        print(state.prev_action)
           
if __name__ == '__main__':
    main()