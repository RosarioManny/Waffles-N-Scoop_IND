async function removeCartItem(event, productId ) {
  event.preventDefault();

  try {
    const response = await fetch("/cart/remove", {
      method: "DELETE",
      headers: { "Content-Type": "application/json"},
      body: JSON.stringify({ product_id: productId}),
    });

    if(response.ok) {
      const data = await response.json()
      event.target.closest('li').remove();
      event.target.closest('hr').remove();
      console.log("SUCCESS", data)
      alert("Removed from Cart!");
    } else {
      const errorData = await response.json()
      console.log("ERROR",errorData)
      alert("Failed to remove. :(");
    }
  } catch (error) {
    console.error("Error", error)
  }
}