function decrementQuantity (button) {
  const input = button.parentElement.querySelector('.quantity-input')
  console.log("Input:", input)
  let value = parseInt(input.value)
  // console.log(t)
  if (value > parseInt(input.min))
    input.value = value - 1
  console.log("Change: ", input.value)
}

function incrementQuantity (button) {
  const input = button.parentElement.querySelector('.quantity-input')
  console.log("Input:", input)
  let value = parseInt(input.value)
  // console.log("Value : ", value)
  if (value < parseInt(input.max))
    input.value = value + 1
    console.log("Change: ", input.value)
}