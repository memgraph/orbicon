import itertools
import math
from collections import defaultdict
from operator import itemgetter
from typing import List

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import numpy as np

from numpy.linalg import norm
import itertools
from operator import itemgetter

import mgclient
import numpy as np
from numpy.linalg import norm
import math

MODE = "KMEANS" # KMEANS | CLUSTERS_DEBUG


def create_connection():
    connection = mgclient.connect(host='127.0.0.1', port=7687)
    return connection


def call_a_query(connection, query):
    cursor = connection.cursor()

    cursor.execute(query)

    return cursor.fetchall()


def get_node2vec_query_result() -> list:
    connection = create_connection()
    rows = call_a_query(connection, "CALL node2vec_online.get() YIELD *")
    connection.close()
    return rows


def calculate_similarity():
    rows = get_node2vec_query_result()
    max_similarity = 0

    similarities = []
    for result1, result2 in itertools.combinations(rows, 2):
        embedding1, node1 = result1
        embedding2, node2 = result2
        embedding1 = np.array(embedding1)
        embedding2 = np.array(embedding2)
        similarity = math.fabs(np.dot(embedding1, embedding2) / (norm(embedding1) * norm(embedding2)))

        similarities.append([similarity, node1, node2])
        if similarity > max_similarity:
            node_max1 = node1
            node_max2 = node2
            max_similarity = similarity

    similarities = sorted(similarities, key=itemgetter(0))

    return similarities


def calculate_similarities():
    similarities = calculate_similarity()
    i = 0
    for s in similarities:
        print(*s)
        i += 1
        if i > 100:
            break


def visualize_clusters_error(x, y):
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()


def calculate_inertia(embeddings, clusters ):
    scaler = StandardScaler()
    embeddings_scaled = scaler.fit_transform(embeddings)

    inertia = []

    for k in clusters:
        kmeans = KMeans(n_clusters=k, random_state=0).fit(embeddings_scaled)
        print("k:", k, " inertia:", kmeans.inertia_)
        inertia.append(kmeans.inertia_)

    return inertia


def get_groups(number_of_clusters, embeddings, nodes):
    scaler = StandardScaler()
    embeddings_scaled = scaler.fit_transform(embeddings)

    kmeans = KMeans(n_clusters=number_of_clusters, random_state=0).fit(embeddings_scaled)

    kmeans_labels = kmeans.labels_

    classes_embeddings_dict = defaultdict(list)
    classes_embedding_list=[]
    for i in range(len(kmeans_labels)):
        label = kmeans_labels[i]
        classes_embeddings_dict[label].append([embeddings[i], nodes[i]])
        classes_embedding_list.append([nodes[i],label])

    return classes_embeddings_dict, classes_embedding_list


def main():
    query_result = get_node2vec_query_result()
    embeddings = []
    nodes = []
    for embedding, node in query_result:
        embeddings.append(embedding)
        nodes.append(node)

    if MODE == "CLUSTERS_DEBUG":
        clusters = np.arange(2, 11)
        inertia = calculate_inertia(embeddings, clusters)
        visualize_clusters_error(clusters, inertia)
        return

    if MODE == "KMEANS":
        classes_dict, classes_list = get_groups(5, embeddings, nodes)
        output = ""
        for key, value in classes_dict.items():
            print("KEY:" + str(key) + "\n")
            for embedding, node in value:
                print(node, key)
            print("............................")
            print("\n")


if __name__ == "__main__":
    main()


# for i in range(0, 7):
#     group_similarity = []
#     for comb1, comb2 in itertools.combinations(classes_embeddings[i], 2):
#         embedding1, node1 = comb1
#         embedding2, node2 = comb2
#         embedding1 = np.array(embedding1)
#         embedding2 = np.array(embedding2)
#         similarity = math.fabs(np.dot(embedding1, embedding2) / (norm(embedding1) * norm(embedding2)))
#         # print(similarity, node1.properties["name"],node2.properties["name"])
#         group_similarity.append([similarity, node1, node2])
#     print("group:", i, " ,mean:", np.mean(np.array([x[0] for x in group_similarity])))
#
#     group_similarity = sorted(group_similarity, key=itemgetter(0))
#     list.reverse(group_similarity)
#     print("group", i)
#     for i in range(10):
#         similarity, node1, node2 = group_similarity[i]
#         print(similarity, node1.properties["name"], node2.properties["name"])
#
# with open("group-results.txt", "w") as text_file:
#     text_file.write(output)
