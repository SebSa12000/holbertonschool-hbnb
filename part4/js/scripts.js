/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    /* DO SOMETHING */
    fetchPlaces('');
  });

/** Places fetch and display */
async function fetchPlaces(token) {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {

    });
    /*      headers: {
        Authorization: `Bearer ${token}`,
      },*/
    const places = await response.json();
    displayPlaces(places);
  } catch (error) {
    console.error("Error fetching places:", error);
  }
}


function displayPlaces(places) {
  const placesList = document.getElementById("places-list");
  placesList.innerHTML = "";
  places.forEach((place) => {
    const placeCard = document.createElement("div");
    placeCard.className = "place-card";
    placeCard.innerHTML = `
      <a href="place.html?id=${place.id}" class="place-card-image">
        ${place.title}
      </a>
      <div class="place-card-content">
        <h2>${place.title}</h2>
        <p class="description">${place.description}</p>
        <p class="price-card"><strong>${place.price} €</strong> per night</p>
      </div>
    `;
    placesList.appendChild(placeCard);
  });
  /*applyPriceFilter();*/
}

