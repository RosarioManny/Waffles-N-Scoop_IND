async function addToCart(event, productId) {

  try {
    const response = await fetch("/cart", {
      method: "POST",
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify({ product_id: productId}),
    });

    if(response.ok) {
      alert("Added to Cart!");
    } else {
      alert("Failed to add to cart. :(");
    }
  } catch (error) {
    console.error("Error", error)
  }
}