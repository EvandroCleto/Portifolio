# Estudo de Caso - Prevendo os Efeitos do Consumo de Álcool em Doenças do Fígado

# Leia o manual em pdf no Capítulo 13 do curso com a especificação do estudo de caso.

# Obs: Caso tenha problemas com a acentuação, consulte este link:
# https://support.rstudio.com/hc/en-us/articles/200532197-Character-Encoding

# Definindo o diretório de trabalho
getwd()
setwd("E:/Curso_FCD/4-MachineLearning/Arquivos/Cap13/R")

# Pacotes
library(dplyr)
library(caret)
library(neuralnet)

##### Carregando os dados ##### 
df_pacientes <- read.csv("dados/dataset.csv")
View(df_pacientes)

##### Análise Explorória ##### 

# Vamos verificar os tipos de dados
str(df_pacientes)

# Vamos checar se temos valores missing
sum(is.na(df_pacientes))

# Resumo estatístico
summary(df_pacientes)

# Proporção da classe
# Em nosso dataset, a coluna target "classe" representa:
# 1 significa a presença de doença do fígado
# 2 significa que nenhuma doença do fígado foi identificada
table(df_pacientes$classe)
prop.table(table(df_pacientes$classe))

# As classes estão desbalanceadas, com mais registros da classe positiva (tem doença).
# Cuidaremos disso daqui a pouco

##### Pré-Processamento e Engenharia de Atributos ##### 

# Vamos criar outra coluna chamada "doente" e preencher com os valores sim/nao
# Esse passo não é obrigatório, sendo apenas didático
# Usaremos essa nova coluna como coluna target
df_pacientes["doente"] <- ifelse(df_pacientes$classe == 2, "nao", "sim")
View(df_pacientes)
str(df_pacientes)

# Transformando a coluna target em fator
df_pacientes["doente"] <- factor(df_pacientes$doente)
str(df_pacientes)

# A coluna alkphos possui 4 valores nulos. Vamos fazer imputação substituindo pela mediana.
alkphos_mediana <- median(df_pacientes$alkphos, na.rm = T)
df_pacientes$alkphos[is.na(df_pacientes$alkphos)] <- alkphos_mediana
sum(is.na(df_pacientes))

# Vamos criar variáveis dummy para o sexo do paciente
df_pacientes["Mulher"] <- ifelse(df_pacientes$sexo == "Mulher",1,0)
df_pacientes["Homem"] <- ifelse(df_pacientes$sexo == "Homem",1,0)
View(df_pacientes)
str(df_pacientes)

# Divisão dos dados em treino e teste com proporção 70/30
df_treino <- df_pacientes[1:as.integer(0.70 * nrow(df_pacientes)),]
df_teste <- df_pacientes[-c(1:as.integer(0.70 * nrow(df_pacientes))),]

# Verificamos os dados
View(df_treino)
View(df_teste)

# Verificamos os tipos de dados
str(df_treino)
str(df_teste)

# Vimos na análise exploratória que as classes estão desbalanceadas.
# Vamos aplicar o upsampling e criar amostras para a classe negativa
# Fazemos isso apenas para dados de treino
#upSample->upSample samples with replacement to make the class distributions equal
df_treino <- upSample(x = df_treino, df_treino$doente)
prop.table(table(df_treino$doente))
str(df_treino)

# Função para padronização das variáveis quantitativas
func_normaliza <- function(x){
  return ((x - min(x)) / (max(x) - min(x)))
}

# Aplica a função
# Observe que estamos excluindo da padronização as colunas de índice 2 e de 11 a 15
# Por que? Porque são colunas categóricas, onde a padronização não é necessária
str(df_treino)
df_treino_norm <- as.data.frame(lapply(df_treino[,-c(2,11:15)], FUN = func_normaliza))
df_teste_norm <- as.data.frame(lapply(df_teste[,-c(2,11:15)], FUN = func_normaliza))

# Agora criamos o dataframe final retornando as colunas que não precisam de padronização
# e que usaremos para modelagem preditiva
df_treino_final <- data.frame(df_treino_norm, df_treino[,c(13,14,12)]) 
df_teste_final <- data.frame(df_teste_norm, df_teste[,c(13,14,12)]) 

# Visualiza os dados
View(df_treino_final)
View(df_teste_final)

# Verifica os tipos de dados e toal de variáveis
str(df_treino_final)
str(df_teste_final)

##### Modelagem Preditiva ##### 

# Construindo o modelo
formula_nn <- paste("doente", paste(colnames(df_treino_final[-12]), collapse = "+"), sep = "~")
modelo_figado <- neuralnet(formula_nn, data = df_treino_final)

# Resumo do modelo
str(modelo_figado)
plot(modelo_figado)

# Previsões com o modelo treinado
set.seed(7)
previsoes_figado <- predict(modelo_figado, df_teste_final[1:11]) 
View(previsoes_figado)

# O resultado das previsões é em probabilidade. Vamos ajustar a saída.
previsoes_figado_final <- ifelse(previsoes_figado[,1] > previsoes_figado[,2], "nao", "sim")
View(previsoes_figado_final)

# Acurácia do modelo
mean(previsoes_figado_final == df_teste_final$doente) 

# Previsão com novos dados
# Vejamos de os 5 novos pacientes podem desenvolver doença do fígado
# com base nos resultados dos exames de sangue

##### Carregando os dados ##### 
df_novos_pacientes <- read.csv("dados/novos_pacientes.csv")
View(df_novos_pacientes)
str(df_novos_pacientes)

# Padronizamos os novos dados
df_novos_pacientes_norm <- as.data.frame(lapply(df_novos_pacientes, FUN = func_normaliza))
View(df_novos_pacientes_norm)

# Previsões
previsoes_novos_pacientes <- predict(modelo_figado, df_novos_pacientes_norm) 
previsoes_novos_pacientes_final <- ifelse(previsoes_novos_pacientes[,1] > previsoes_novos_pacientes[,2], "nao", "sim")
View(previsoes_novos_pacientes_final)

# Previsões feitas com sucesso!


