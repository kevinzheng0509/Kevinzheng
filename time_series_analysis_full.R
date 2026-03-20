# MediaTek (2454) Time Series Analysis
# Author: Kevin (Cheng-Chieh) Zheng

# 1. Load packages -----------------------------------------------------------
library(tidyverse)
library(dplyr)
library(lubridate)
library(forecast)
library(tseries)   # adf.test
library(zoo)
library(moments)
library(patchwork)
# If you want to fit GARCH later:
# library(rugarch)

# 2. Read and combine data ---------------------------------------------------
data1 <- read_csv("2454_history.csv")
data2 <- read_csv("2454_history 2.csv")

data <- bind_rows(data1, data2) %>%
  mutate(Date = ymd(.data$日期)) %>%
  arrange(Date) %>%
  distinct(Date, .keep_all = TRUE)

glimpse(data)

# 3. Build price and return series -------------------------------------------
price <- data$收盤
dates <- data$Date

# Log return: log(P_t) - log(P_{t-1})
ret <- diff(log(price))
ret_dates <- dates[-1]
ret_series <- zoo(ret, order.by = ret_dates)

# Mean log return
r_mean <- mean(ret)
r_mean

# 4. Quick plots --------------------------------------------------------------
p_price <- autoplot(zoo(price, order.by = dates)) +
  ggtitle("2454 Closing Price") +
  xlab("Date") + ylab("Closing Price")
p_price
ggsave("closing_price.png", p_price, width = 8, height = 4.5, dpi = 300)

p_ret <- autoplot(ret_series) +
  ggtitle("2454 Daily Logarithmic Return") +
  xlab("Date") + ylab("Return")
p_ret
ggsave("log_return.png", p_ret, width = 8, height = 4.5, dpi = 300)

# 5. Stationarity test --------------------------------------------------------
adf_result <- adf.test(ret)
adf_result

# 6. Fit ARIMA model ----------------------------------------------------------
n <- length(ret)
test_len <- 60

train_ret <- ret[1:(n - test_len)]
test_ret  <- ret[(n - test_len + 1):n]

train_ts <- ts(train_ret, frequency = 1)

fit_arima <- auto.arima(train_ts)
summary(fit_arima)

# Residual diagnostics
checkresiduals(fit_arima)

# Save residual plot
png("residual.png", width = 1800, height = 900, res = 180)
plot(residuals(fit_arima), type = "l",
     main = "Residuals of ARIMA Model",
     xlab = "Index", ylab = "Residuals")
dev.off()

# 7. Forecast ----------------------------------------------------------------
h <- test_len
fc <- forecast(fit_arima, h = h)

p_fc <- autoplot(fc) +
  ggtitle("ARIMA Model Forecast of Returns")
p_fc
ggsave("arima_forecast.png", p_fc, width = 8, height = 4.5, dpi = 300)

# Convert predicted returns back to prices
last_train_price <- price[length(price) - test_len]

pred_ret <- as.numeric(fc$mean)
pred_price <- numeric(length = h)
pred_price[1] <- last_train_price * exp(pred_ret[1])

if (h >= 2) {
  for (i in 2:h) {
    pred_price[i] <- pred_price[i - 1] * exp(pred_ret[i])
  }
}

# 8. Evaluate performance -----------------------------------------------------
test_price <- price[(length(price) - test_len + 1):length(price)]

rmse <- sqrt(mean((pred_price - test_price)^2))
mae  <- mean(abs(pred_price - test_price))

rmse
mae

result_tbl <- tibble(
  Date = dates[(length(dates) - test_len + 1):length(dates)],
  Actual = test_price,
  Predicted = pred_price
)
write_csv(result_tbl, "result_arima.csv")

desc_tbl <- tibble(
  Statistic = c("Mean", "SD", "Min", "Max", "Skewness", "Kurtosis"),
  Value = c(
    mean(ret),
    sd(ret),
    min(ret),
    max(ret),
    skewness(ret),
    kurtosis(ret)
  )
)
write_csv(desc_tbl, "return_description.csv")
desc_tbl

coefs <- coef(fit_arima)
coef_tbl <- tibble(
  Parameter = names(coefs),
  Estimate = as.numeric(coefs)
)
write_csv(coef_tbl, "arima_params.csv")
coef_tbl

# 9. ACF / PACF plots ---------------------------------------------------------
p_acf_ret <- ggAcf(ret, main = "ACF of Log Returns")
p_pacf_ret <- ggPacf(ret, main = "PACF of Log Returns")

p_acf_ret
ggsave("acf_ret.png", p_acf_ret, width = 7, height = 4.5, dpi = 300)

p_pacf_ret
ggsave("pacf_ret.png", p_pacf_ret, width = 7, height = 4.5, dpi = 300)

p_all <- p_acf_ret + p_pacf_ret
p_all
ggsave("acf_pacf_combined.png", p_all, width = 10, height = 4.5, dpi = 300)

# 10. Optional GARCH section --------------------------------------------------
# Uncomment if rugarch is installed
# library(rugarch)
# spec <- ugarchspec()
# fit_garch <- ugarchfit(spec, ret)
# fit_garch
