async function addToCart(event, productId) {
  event.preventDefault(); // Stops reload
  const form = event.target
  const quantity = form.querySelector('.quantity-input').value;

  console.log(`Adding to cart: Product ID ${productId}, Quantity ${quantity}`);
  try {
    const response = await fetch("/shop", {
      method: "POST",
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify({ 
        product_id: productId,
        quantity: quantity
      }),
    });

    console.log(response)
    if(response.ok) {
      const data = await response.json()
      const addToCart_btn = form.querySelector((".add-product-btn"))
      addToCart_btn.textContent = "Added ✔"
      // addToCart_btn.style.background()
      console.log("SUCCESS :: Added to Cart!");
    } else {
      const errorData = await response.json()
      console.log("ERROR :: Failed to add:",errorData)
    }
  } catch (error) {
    console.error("TRY Error ::", error)
  }
}

