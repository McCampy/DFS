# Title     : pca_regression
# Objective : Create a regression to predict player fantasy performance from a variety of statistics
# Created by: Nicholas Kubas
# Created on: 12/15/20

pca_predict <- function (csv_file) {
  library(Metrics)

  df <- read.csv(paste(csv_file), header=TRUE, sep=",")

  points <- df$Points
  trainer <- df[-1*ncol(df)]
  trainer.matrix <- data.matrix(trainer)
  for (i in 1:ncol(trainer.matrix)) {
    trainer.matrix[,i] <- (trainer.matrix[,i] - mean(trainer.matrix[,i]))/sd(trainer.matrix[,i])
  }
  # print(trainer.matrix)

  pca <- prcomp(trainer.matrix, center=TRUE, scale=TRUE)
  comps <- pca$sdev
  new.vars <- comps[comps > 1]
  # print(new.vars)

  rotations <- pca$rotation
  pca.transform <- rotations[,1:length(new.vars)]
  # print(pca.transform)
  pca.trainer <- trainer.matrix %*% pca.transform
  # print(pca.trainer)

  pca.df <- data.frame(cbind(pca.trainer, points))
  # print(pca.df)
  pca.reg <- lm(points ~ ., data=pca.df)

  print(summary(pca.reg))
  plot(pca.reg$fitted.values, points)
  print(mae(df$Points, pca.reg$fitted.values))

  # write.csv(pca.transform, file='E:\fanduel_programs\pca_regression(folder)/qb_pca_matrix.csv')
  return(pca.transform)

}
