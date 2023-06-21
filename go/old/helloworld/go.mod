module helloworld

go 1.18

require (
  "calculator" v0.0.0
  "calculator2" v0.0.0
)

replace (
  calculator => ../calculator
  calculator2 => ../calculator2
)