import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import scipy.io as sio
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold

data1 = pd.read_csv('/content/Input1.csv', header=None)
data2 = pd.read_csv('/content/Input2.csv', header=None)

data1.head()

data1.info()

data1.describe()

data2.head()

data2.info()

data2.describe()

def bayes_classifier(train_data, train_labels, test_data):
    class_labels = np.unique(train_labels)
    means = []
    stds = []

    # Calcular média e desvio padrão por classe
    for label in class_labels:
        class_data = train_data[train_labels == label]
        means.append(np.mean(class_data, axis=0))
        stds.append(np.std(class_data, axis=0) + 1e-6)  # Adiciona um pequeno valor para evitar divisão por zero

    means = np.array(means)
    stds = np.array(stds)

    predictions = []

    # Classificação com base na probabilidade gaussiana
    for sample in test_data:
        log_probs = []
        for i, label in enumerate(class_labels):
            # Calcular log da probabilidade para evitar subfluxo
            log_prob = -0.5 * np.sum(np.log(2 * np.pi * stds[i]**2) + ((sample - means[i])**2 / (stds[i]**2)))
            log_probs.append(log_prob)

        # A classe com a maior probabilidade logarítmica é a previsão
        predictions.append(class_labels[np.argmax(log_probs)])

    return np.array(predictions)

def lda(train_data, train_labels):
    class_labels = np.unique(train_labels)

    # Separar dados por classe
    class_1_data = train_data[train_labels == class_labels[0]]
    class_2_data = train_data[train_labels == class_labels[1]]

    # Calcular médias
    mean_1 = np.mean(class_1_data, axis=0)
    mean_2 = np.mean(class_2_data, axis=0)

    # Calcular covariância dentro das classes
    cov_1 = np.cov(class_1_data, rowvar=False, bias=False)
    cov_2 = np.cov(class_2_data, rowvar=False, bias=False)

    # Covariância total (dentro das classes)
    cov_within = (len(class_1_data) * cov_1 + len(class_2_data) * cov_2) / (len(class_1_data) + len(class_2_data))

    # Vetor de pesos
    w = np.linalg.inv(cov_within).dot(mean_1 - mean_2)

    # Calcular limiar como ponto médio das projeções das médias das classes
    projection_1 = np.dot(mean_1, w)
    projection_2 = np.dot(mean_2, w)
    threshold = (projection_1 + projection_2) / 2

    return w, threshold

def cross_val_k_fold(X, y, K, bayes_classifier_func, lda_func):
    fold_size = len(X) // K
    indices = np.arange(len(X))
    np.random.shuffle(indices)

    accuracies_bayes = []
    accuracies_lda = []

    for i in range(K):
        # Dividir dados em treino e teste
        test_indices = indices[i*fold_size:(i+1)*fold_size]
        train_indices = np.concatenate([indices[:i*fold_size], indices[(i+1)*fold_size:]])

        X_train, X_test = X[train_indices], X[test_indices]
        y_train, y_test = y[train_indices], y[test_indices]

        # Classificador Bayesiano
        y_pred_bayes = bayes_classifier_func(X_train, y_train, X_test)
        acc_bayes = accuracy_score(y_test, y_pred_bayes)
        accuracies_bayes.append(acc_bayes)

        # LDA
        w, threshold = lda_func(X_train, y_train)
        projections_test = X_test.dot(w)

        # Classificação baseada em limiar
        y_pred_lda = (projections_test >= threshold).astype(int)
        acc_lda = accuracy_score(y_test, y_pred_lda)
        accuracies_lda.append(acc_lda)

    # Resultados
    mean_acc_bayes = np.mean(accuracies_bayes)
    std_acc_bayes = np.std(accuracies_bayes)
    mean_acc_lda = np.mean(accuracies_lda)
    std_acc_lda = np.std(accuracies_lda)

    return mean_acc_bayes, std_acc_bayes, mean_acc_lda, std_acc_lda

# Transpor para obter 2000 amostras com 2 atributos cada
X = data1.values.T  # Agora X tem (4000, 2)
# data1_2000 contém as primeiras 2000 colunas e data1_4000 as colunas de 2001 a 4000
y = np.array([1] * 2000 + [2] * 2000)

# Executar validação cruzada K-fold
mean_acc_bayes, std_acc_bayes, mean_acc_lda, std_acc_lda = cross_val_k_fold(X, y, 10, bayes_classifier, lda)

# Resultados
print(f'Acurácia Média - Bayes: {mean_acc_bayes}')
print(f'Desvio-padrão da Acurácia - Bayes: {std_acc_bayes}')
print(f'Acurácia Média - LDA: {mean_acc_lda}')
print(f'Desvio-padrão da Acurácia - LDA: {std_acc_lda}')

# Gráfico de dispersão 2D dos dados
plt.scatter(X[:2000, 0], X[:2000, 1], color='red', label='Classe 1')
plt.scatter(X[2000:, 0], X[2000:, 1], color='blue', label='Classe 2')
plt.legend()
plt.title('Gráfico de Dispersão dos Dados')
plt.show()

# Transpor para obter 2000 amostras com 2 atributos cada
X = data2.values.T  # Agora X tem (4000, 2)
# data1_2000 contém as primeiras 2000 colunas e data1_4000 as colunas de 2001 a 4000
y = np.array([1] * 2000 + [2] * 2000)

# Executar validação cruzada K-fold
mean_acc_bayes, std_acc_bayes, mean_acc_lda, std_acc_lda = cross_val_k_fold(X, y, 10, bayes_classifier, lda)

# Resultados
print(f'Acurácia Média - Bayes: {mean_acc_bayes}')
print(f'Desvio-padrão da Acurácia - Bayes: {std_acc_bayes}')
print(f'Acurácia Média - LDA: {mean_acc_lda}')
print(f'Desvio-padrão da Acurácia - LDA: {std_acc_lda}')

# Gráfico de dispersão dos dados
plt.scatter(X[:2000, 0], X[:2000, 1], color='red', label='Classe 1')
plt.scatter(X[2000:, 0], X[2000:, 1], color='blue', label='Classe 2')
plt.legend()
plt.title('Gráfico de Dispersão dos Dados')
plt.show()
