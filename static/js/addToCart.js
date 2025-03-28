async function addToCart(event, productId) {
  event.preventDefault(); // Stops reload

  try {
    const response = await fetch("/shop", {
      method: "POST",
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify({ product_id: productId}),
    });

    console.log(response)
    if(response.ok) {
      const data = await response.json()
      console.log("SUCCESS :: Removed from Cart!");
    } else {
      const errorData = await response.json()
      console.log("ERROR :: Failed to remove:",errorData)
    }
  } catch (error) {
    console.error("TRY Error ::", error)
  }
}

