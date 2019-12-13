library(readr)

latest <- read_csv("./latest_data.csv")
previous <- read_csv("./previous_data.csv")

latest_data <- data.frame(latest$CERT, latest$`Closing Date`)
names(latest_data) <- c("cert", "fail_date")

previous_data <- data.frame(previous$CERT, previous$FAILDATE)
names(previous_data) <- c("cert", "fail_date")
previous_data <- subset(previous_data, !is.na(cert))

data <- data.frame(rbind(previous_data, latest_data))
write_csv(data, "./certs_and_fail_dates.csv")
