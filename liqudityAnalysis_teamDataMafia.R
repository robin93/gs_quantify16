data <- read.csv("liquidity_events.csv", header=T)
head(data)
hist(data$liquidity,main="liquidity Distribution",xlab="liquidity Values")

data1 <- data[data$EventIndicator==1]

data1 <- subset(data,EventIndicator==1)
hist(data1$liquidity)

data2 <- subset(data,EventIndicator==2)
hist(data2$liquidity)

data3 <- subset(data,EventIndicator==3)
hist(data3$liquidity)
