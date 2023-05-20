# Estudo de Caso - Deep Learning em R Para Classificação de Imagens

# O objetivo deste Estudo de Caso é reproduzir o Mini-Projeto 6 para classificação de imagens.
# Lá trabalhamos em Python. Agora trabalharemos em R.

# Esse exercício vai ajudar você a consolidar o conhecimento sobre Deep Learning, ao mesmo tempo que 
# aprimora suas habilidades em R.

# Leia todos os comentários e execute todas as linhas. Os pacotes precisam ser instalados apenas uma vez!

# Os detalhes do Estudo de Caso (incluindo a fonte de dados) estão no manual em pdf.

# Diretório de trabalho
getwd()
setwd("E:/Curso_FCD/4-MachineLearning/Arquivos/Cap14/EstudoCaso")

# Pacotes reticulate e devtools serão usados para instalar Keras e TensorFlow
install.packages("reticulate", type="binary")
library(reticulate)
install.packages("devtools", type="binary")
library(devtools)
search()
install.packages("Rcpp", type="binary")
library(Rcpp)
install.packages("rlang", type="binary")
library(rlang)
install.packages("glue", type="binary")
library(glue)
install.packages("backports", type="binary")
library(backports)
install.packages("tfautograph", type="binary")
library(tfautograph)

install.packages("keras", type="binary")

# Vamos instalar o Keras para criação do modelo CNN
devtools::install_github("rstudio/keras")
force = TRUE
library(keras)

# O Keras depende do TensorFlow, que também deve ser instalado
install.packages("tensorflow")
library(tensorflow)
install_tensorflow()

# Carregando a lista de labels disponíveis no dataset
labels <- read.table("cifar-10-batches-bin/batches.meta.txt")

# Criando listas para imagens e labels
images.rgb <- list()
images.lab <- list()

# Vamos extrair 10000 imagens de cada arquivo binário
num.images = 10000 

# Loop por todos arquivos binários para carregar as listas de imagens e labels
for (f in 1:5) {
  
  # Loop por cada arquivo
  arquivo <- file(paste("cifar-10-batches-bin/data_batch_", f, ".bin", sep = ""), "rb")
  for(i in 1:num.images) {
    
    # Lê o arquivo
    l <- readBin(arquivo, integer(), size = 1, n = 1, endian = "big")
    
    # Carrega os pixels para os 3 canais de cores: red, green e blue
    r <- as.integer(readBin(arquivo, raw(), size = 1, n = 1024, endian = "big"))
    g <- as.integer(readBin(arquivo, raw(), size = 1, n = 1024, endian = "big"))
    b <- as.integer(readBin(arquivo, raw(), size = 1, n = 1024, endian = "big"))
    
    # Índice
    index <- num.images * (f-1) + i
    
    # Listas
    images.rgb[[index]] = data.frame(r, g, b)
    images.lab[[index]] = l+1
  }
  
  # Fechamos o arquivo e removemos os objetos temporários para liberar memória
  close(arquivo)
  remove(l,r,g,b,f,i, index, arquivo)
}

# Função para imprimir uma imagem
# Aqui organizamos os pixels para mostrar a imagem como um plot
drawImage <- function(index) {
  img <- images.rgb[[index]]
  img.r.mat <- matrix(img$r, ncol = 32, byrow = TRUE)
  img.g.mat <- matrix(img$g, ncol = 32, byrow = TRUE)
  img.b.mat <- matrix(img$b, ncol = 32, byrow = TRUE)
  img.col.mat <- rgb(img.r.mat, img.g.mat, img.b.mat, maxColorValue = 255)
  dim(img.col.mat) <- dim(img.r.mat)

  # Cria o grid
  library(grid)
  grid.raster(img.col.mat, interpolate=FALSE)

  # Remove objetos temporários
  remove(img, img.r.mat, img.g.mat, img.b.mat, img.col.mat)
  
  # Define labels
  labels[[1]][images.lab[[index]]]
}

# Executa a função
drawImage(sample(1:(num.images * 5), size = 1))

# Vamos ler novamente a lista de classes, mas agora usaremos para as imagens de teste
labels1 <- read.table("cifar-10-batches-bin/batches.meta.txt")

# Listas de imagens e labels
images.rgb1.test <- list()
images.lab.test <- list()

# Temos 10 mil imagens de teste
num.images1 = 10000

# Carrega o arquivo com as imagens de teste
arquivo_teste <- file(paste("cifar-10-batches-bin/test_batch", ".bin", sep = ""), "rb")

# Loop para carregar as listas de imagens e labels de teste (igual ao que fizemos em treino)
for(i in 1:num.images1) {
  l <- readBin(arquivo_teste, integer(), size = 1, n = 1, endian = "big")
  r <- as.integer(readBin(arquivo_teste, raw(), size = 1, n = 1024, endian = "big"))
  g <- as.integer(readBin(arquivo_teste, raw(), size = 1, n = 1024, endian = "big"))
  b <- as.integer(readBin(arquivo_teste, raw(), size = 1, n = 1024, endian = "big"))
  images.rgb1.test[[i]] <- data.frame(r,g,b)
  images.lab.test[[i]] <- l+1
}

# Vamos encerrar o objeto para liberar memória do computador
close(arquivo_teste)
remove(l,r,g,b,i, arquivo_teste)

# Dados de treino e teste
dados_treino <- images.rgb
dados_teste <- images.rgb1.test

# Criamos agora um array de 32x32x3 (altura x largura x canais de cores)
# O array terá 50.000 imagens que serão usadas para treinar o modelo CNN

# Shape da matriz de treino com 4 dimensões
matriz_treino <- array(dim = c(length(dados_treino), 32, 32, 3))
dim(matriz_treino)

# Loop para preparar a matriz de dados de treino
for (i in 1:length(dados_treino)){
  d_1 <- matrix(dados_treino[[i]][,1], nrow = 32, ncol = 32, byrow = TRUE)
  for (j in 1:32){
    matriz_treino[i,j,,1] <- as.numeric(unlist(d_1[j,]))
  }
  d_2 <- matrix(dados_treino[[i]][,2], nrow = 32, ncol = 32, byrow = TRUE)
  for (j in 1:32){
    matriz_treino[i,j,,2] <- as.numeric(unlist(d_2[j,]))
  }
  d_3 <- matrix(dados_treino[[i]][,3], nrow = 32, ncol = 32, byrow = TRUE)
  for (j in 1:32){
    matriz_treino[i,j,,3] <- as.numeric(unlist(d_3[j,]))
  }
  rm(d_1,d_2,d_3)
}

# Shape da matriz de teste com 4 dimensões
matriz_teste <- array(dim = c(length(dados_teste), 32, 32, 3))
dim(matriz_teste)

# Loop para carregar a matriz com dados de teste
for (i in 1:length(dados_teste)){
  d_1 <- matrix(dados_teste[[i]][,1], nrow = 32, ncol = 32, byrow = TRUE)
  for (j in 1:32){
    matriz_teste[i,j,,1] <- as.numeric(unlist(d_1[j,]))
  }
  d_2 <- matrix(dados_teste[[i]][,2], nrow = 32, ncol = 32, byrow = TRUE)
  for (j in 1:32){
    matriz_teste[i,j,,2] <- as.numeric(unlist(d_2[j,]))
  }
  d_3 <- matrix(dados_teste[[i]][,3], nrow = 32, ncol = 32,byrow = TRUE)
  for (j in 1:32){
    matriz_teste[i,j,,3] <- as.numeric(unlist(d_3[j,]))
  }
  rm(d_1,d_2,d_3)
}

# Agora separamos imagens e labels em treino e teste
set.seed(02122020)

# Imagens de treino e teste
x_treino <- matriz_treino[1:50000,,,]
x_teste <- matriz_teste[1:10000,,,]

# Labels de treino e teste
y_treino <- array(unlist(images.lab[1:50000]), dim = c(50000,1))
y_teste <- array(unlist(images.lab.test[1:10000]), dim = c(10000,1))

# Os labels estão no intervalo de 0 a 9, então estamos subtrair 1
# Se não for feito, pode haver um erro como índice fora do limite
y_treino1 <- y_treino - 1
y_teste1 <- y_teste - 1

# One Hot Encoding para formatar os labels
y_treino2 <- to_categorical(y_treino1, num_classes = 10)
y_teste2 <- to_categorical(y_teste1, num_classes = 10)

# Criação do Modelo CNN
modelo_cnn <- keras_model_sequential()

# Arquitetura do Modelo CNN
modelo_cnn %>%
  layer_conv_2d(filter = 32, 
                kernel_size = c(3,3),
                padding = "same",
                input_shape = c(32,32,3),
                activation = "relu") %>%
  layer_conv_2d(filter = 32,
                kernel_size = c(3,3),
                activation = "relu") %>% 
  layer_max_pooling_2d(pool_size = c(2,2)) %>% 
  layer_dropout(0.25) %>% 
  layer_conv_2d(filter = 32,
                kernel_size = c(3,3),
                padding = "same",
                activation = "relu") %>%
  layer_conv_2d(filter = 32, kernel_size = c(3,3),
                activation = "relu" ) %>% 
  layer_max_pooling_2d(pool_size = c(2,2)) %>%
  layer_dropout(0.25) %>%
  layer_flatten() %>% 
  layer_dense(units = 512,
              activation = "relu") %>%
  layer_dropout(0.5) %>%
  layer_dense(10) %>% 
  layer_activation("softmax")

# Otimizador para o modlo
opt <- optimizer_adam(lr = 0.0001, decay = 1e-6)

# Compila o modelo com a função de custo e o otimizador
modelo_cnn %>% compile(loss = "categorical_crossentropy",
                       optimizer = opt,
                       metrics = "accuracy")

# Sumário do modelo
summary(modelo_cnn)

# Treinamento do modelo (aumente ou diminua o número de epochs se desejar)
hist_cnn <- modelo_cnn %>% fit(x_treino, 
                               y_treino2, 
                               batch_size = 32,
                               epochs = 50,
                               validation_data = list(x_teste, y_teste2),
                               shuffle = TRUE)

# Histórico de treinamento
plot(hist_cnn)

# Avaliação do modelo
aval <- modelo_cnn %>% evaluate(x_teste, y_teste2)
aval

# Fim




