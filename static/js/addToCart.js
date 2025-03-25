async function addToCart(event, productId) {
  event.preventDefault(); // Stops reload

  try {
    const response = await fetch("/cart", {
      method: "POST",
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify({ product_id: productId}),
    });

    console.log(response)
    if(response.ok) {
      const data = await response.json()
      console.log("SUCCESS", data)
      alert("Added to Cart!");
    } else {
      const errorData = await response.json()
      console.log("ERROR",errorData)
      alert("Failed to add to cart. :(");
    }
  } catch (error) {
    console.error("Error", error)
  }
}

