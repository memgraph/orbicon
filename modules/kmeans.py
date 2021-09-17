from collections import defaultdict
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def calculate_inertia(embeddings, clusters ):
    scaler = StandardScaler()
    embeddings_scaled = scaler.fit_transform(embeddings)

    inertia = []

    for k in clusters:
        kmeans = KMeans(n_clusters=k, random_state=0).fit(embeddings_scaled)
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
