async function checkOut(event, total) {
  event.preventDefault(); // Stops reload

  try {
    const response = await fetch("/checkout", {
      method: "POST",
      headers: { "Content-Type": 'application/json'},
      body: JSON.stringify({ cart_total: total}),
    });

    console.log(response)
    if(response.ok) {
      const data = await response.json();
      event.target.closest("ul").remove();
      window.location.reload();
      alert("Thank you for Your Purchase!", data);
    } else {
      const errorData = await response.json()
      console.log("ERROR :: Failed to add:",errorData);
    }
  } catch (error) {
    console.error("TRY Error ::", error);
  }
}

