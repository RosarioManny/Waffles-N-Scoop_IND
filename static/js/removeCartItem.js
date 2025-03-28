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
      // REFRESH PAGE TO UPDATE TOTAL
      window.location.reload();

      console.log("SUCCESS :: Removed from Cart!");
    } else {
      const errorData = await response.json()
      console.log("ERROR :: Failed to remove:",errorData)
    }
  } catch (error) {
    console.error("TRY Error ::", error)
  }
}
