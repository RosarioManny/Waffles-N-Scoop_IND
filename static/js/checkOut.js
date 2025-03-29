async function checkOut(event, total) {
  event.preventDefault(); // Stops reload

  try {
    const response = await fetch("/checkout", {
      method: "POST",
      headers: { "Content-Type": 'application/json'},
      body: JSON.stringify({ cart_total: total}),
    });

    const result = await response.json();
    if(response.ok) {
      alert(result.message);
      
      event.target.closest('ul').remove();

      window.location.reload();
    } else {
      const errorData = await response.json()
      alert("ERROR :: Failed to purchase:");
    }
  } catch (error) {
    console.error("TRY Error ::", error);
  }
}

