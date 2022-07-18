import networkx as nx
import matplotlib.pyplot as plt
from math import *
from corresp import *
import _pickle as pkl

import scipy.optimize as optimize
tsp = nx.approximation.traveling_salesman_problem
SA_tsp = nx.approximation.simulated_annealing_tsp
atsp = nx.approximation.asadpour_atsp

def print_Graph(G):
    """
    pos = nx.spring_layout(G)
    nodes = nx.draw_networkx_nodes(G, pos,edgecolors='black',node_color='yellow',)
    nx.draw_networkx_edges(G, pos,)"""

    pos = nx.spring_layout(G,k=10/sqrt(G.order()),iterations=700,threshold=0.000001)
    nx.draw(G,pos,with_labels=True,node_color='yellow',font_size='8',node_shape='o',node_size=500,edgecolors='black')
    plt.show()


def graph_line(line,i):
    G = nx.DiGraph()
    k = 0
    for stop in range(len(line)-1):
        if line[stop] != '' and line[stop+1] != '' and line[stop] != 'v':
            if line[stop + 1] == 'v':
                G.add_edge(line[stop], line[stop+2],weight=w[i][k])
                k+=1
                stop+=1
            else:
                #print(line[stop] + " to " + line[stop+1] + " : " + str(w[i][k]) + " with : i=" + str(i) + " and k= " + str(k))
                G.add_edge(line[stop],line[stop+1],weight=w[i][k])
                G.add_edge(line[stop + 1], line[stop],weight=w[i][k])
                k+=1



    return G

def wiki_to_list(path):
    f = open(path, "r",encoding="windows-1258")
    L = []
    while f :
        line = f.readline()
        if line == "":
            break
        L.append(line[:-1]) if line[len(line)-1] == '\n' else L.append(line)
    f.close()
    return L

def weighted_graph(G,i):
    for node in range(G.order()-1):
        G[node][node+1]["weight"] = w[i][node]
        G[node+1][node]["weight"] = w[i][node]
    return G

def graph_RATP():
    G = nx.DiGraph()
    for line in range(len(RATP)):
        G = nx.compose(G,graph_line(RATP[line],line))
    return G

def corresp_cost(G):
    for station in range(len(RATP)):
        for stop in RATP[station]:
            for i in range(len(RATP)):
                for s in RATP[i] :
                    if len(stop) > 2 and i != station and stop[2:] == s[2:]:
                        print("correspondance between : " + s + " and " + stop)
                        print("i= " + str(i) + " station : " + str(station))
                        print(corresp[station][i])
                        print( [y[1]for y in corresp[station][i]] )

                        print(corresp[station][i][[y[1] for y in corresp[station][i]].index(s[2:])])
                        G.add_edge(s, stop, weight=corresp[i][station][[y[1] for y in corresp[station][i]].index(s[2:])][0])
                        G.add_edge(stop, s, weight=corresp[station][i][[y[1] for y in corresp[station][i]].index(s[2:])][0])

RATP = [
    wiki_to_list("../lignes/M00.txt"),#60s / arret (moyenne)
    wiki_to_list("../lignes/M01.txt"), #86.4s / arret (moyenne)
    wiki_to_list("../lignes/M02.txt"), #79.2s / arret (moyenne)
    wiki_to_list("../lignes/M03.txt"), #74.4s / arret (moyenne)
    wiki_to_list("../lignes/M04.txt"), #74.48s / arret (moyenne)
    wiki_to_list("../lignes/M05.txt"),#72.73s / arret (moyenne)
    wiki_to_list("../lignes/M06.txt"),#66.43s / arret (moyenne)
    wiki_to_list("../lignes/M07.txt"),#72.63s / arret (moyenne)
    wiki_to_list("../lignes/M08.txt"),#82.105s / arret (moyenne)
    wiki_to_list("../lignes/M09.txt"),#84.32s / arret (moyenne)
    wiki_to_list("../lignes/M10.txt"),#73.04s / arret (moyenne)
    wiki_to_list("../lignes/M11.txt"),#69.23s / arret (moyenne)
    wiki_to_list("../lignes/M12.txt"),#73.55s / arret (moyenne)
    wiki_to_list("../lignes/M13.txt"),#69.375s / arret (moyenne)
    wiki_to_list("../lignes/M14.txt"),#106.15s / arret (moyenne)
    wiki_to_list("../lignes/M15.txt")# 60s / arret (moyenne)
]

w = [[60]*3,[86.4]*24,[79.2]*24,[74.4]*24,[74.48]*28,[72.73]*21,[66.43]*27,[72.63]*37,[82.105]*37,[84.32]*36,
     [73.04]*23,[69.23]*12,[73.55]*30,[69.375]*31,[106.15]*12,[60]*8]


RATP_Graph = graph_RATP()
corresp_cost(RATP_Graph)
print_Graph(RATP_Graph)
pkl.dump(RATP_Graph,open("dump_RATP_Graph","wb"))

