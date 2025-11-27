# Classificador Bayesiano com LDA

## Descrição do Projeto

Este projeto implementa um **Classificador Bayesiano** com atributos contínuos e **Análise Discriminante Linear (LDA)** para a classificação de duas classes de dados. O objetivo é realizar a classificação utilizando uma abordagem probabilística com o classificador Bayesiano e explorar a redução de dimensionalidade através do LDA. O modelo é avaliado usando a técnica de **Validação Cruzada K-Fold** com K=10, e os resultados são apresentados em termos de **acurácia média** e **desvio-padrão** da acurácia.

## Funcionalidades

- **Classificador Bayesiano com Atributos Contínuos**: Implementação manual de um classificador probabilístico.
- **Análise Discriminante Linear (LDA)**: Aplicação do LDA para redução de dimensionalidade e posterior classificação.
- **Validação Cruzada K-Fold**: Avaliação do modelo usando validação cruzada para garantir generalização.
- **Gráfico de Dispersão**: Visualização 2D das amostras e das fronteiras de decisão do classificador.
- **Cálculo de Acurácia e Desvio-Padrão**: Cálculo da acurácia média e do desvio-padrão da acurácia nos K folds.

## Requisitos

Para executar este projeto, são necessárias as seguintes dependências:

- `Python 3.x`
- `numpy`
- `matplotlib`
- `scikit-learn` (opcional, para comparação de resultados)

## Descrição da Base de Dados

A base de dados utilizada contém 4000 amostras divididas em duas classes. As amostras possuem dois atributos contínuos que são usados como entrada para o classificador. As amostras da **Classe 1** correspondem às amostras de 1 até 2000, e as da **Classe 2** correspondem às amostras de 2001 até 4000.

### Estrutura dos Dados:

- **Atributos de Entrada**: Dois atributos contínuos para cada amostra.
- **Classes**: Duas classes (Classe 1 e Classe 2) com 2000 amostras cada.

## Resultados

Os resultados do projeto incluem a acurácia média e o desvio-padrão da acurácia ao longo dos 10 folds da validação cruzada. Abaixo estão os resultados para dois conjuntos de dados, **Input1** e **Input2**:

### Conjunto de Dados Input1:

- **Acurácia Média - Bayes**: 1.0
- **Desvio-padrão da Acurácia - Bayes**: 0.0
- **Acurácia Média - LDA**: 0.5
- **Desvio-padrão da Acurácia - LDA**: 0.0263

### Conjunto de Dados Input2:

- **Acurácia Média - Bayes**: 0.6275
- **Desvio-padrão da Acurácia - Bayes**: 0.0254
- **Acurácia Média - LDA**: 0.257
- **Desvio-padrão da Acurácia - LDA**: 0.0215

Esses resultados mostram que o Classificador Bayesiano teve um desempenho superior em ambos os conjuntos de dados, especialmente no **Conjunto de Dados Input1**, onde obteve uma acurácia perfeita. Já o LDA, apesar de sua simplicidade e eficiência computacional, obteve uma acurácia mais baixa, refletindo a complexidade dos dados.

## 👨‍💻 Autor

**Vitor Hugo Muniz de Sousa Santos**

💼 Engenheiro de Computação | Cientista de Dados

📧 [vitormunnizzdev@gmail.com](mailto:vitormunnizzdev@gmail.com)
🌐 [www.linkedin.com/in/vitormunnizz](https://www.linkedin.com/in/vitormunnizz)

## 📝 Licença

Este projeto está licenciado sob a **MIT License**.
Sinta-se livre para usar e modificar conforme necessário, mantendo os créditos ao autor.

⭐ **Se este projeto te ajudou, deixe uma estrela no repositório!**```
