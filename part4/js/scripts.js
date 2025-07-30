function getCookie(name) {
  const cookieValue = document.cookie
    .split("; ")
    .find((row) => row.startsWith(name))
    ?.split("=")[1];
  return cookieValue;
}

/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById("login-link");
  const logoutLink = document.getElementById("logout-link");
  const placesList = document.getElementById("places-list");
  const footer = document.querySelector('footer');

  if (!token) {
    loginLink.style.display = "block";
    logoutLink.style.display = "none";
    if (placesList) {
      placesList.innerHTML =
        `<a href="login.html">
          <p class='noLogged'>You need to be logged in to display places.</p>
        </a>`;
        footer.style.position = 'fixed';
    }
  } else {
    loginLink.style.display = "none";
    logoutLink.style.display = "block";
    fetchPlaces(token);
  }
}


/** Login/Logout Form  */
document.addEventListener("DOMContentLoaded", () => {
  // Authentification check for user based on the token cookie
  checkAuthentication();

  // Logout functionnality, deleting the cookie token
  const logoutLink = document.getElementById("logout-link");
  if (logoutLink) {
    logoutLink.addEventListener("click", function (event) {
      event.preventDefault();
      deleteTokenCookie();
      window.location.href = "login.html";
    });
  }

  // Submit event for login ( receiveing email and password from form)
  const loginForm = document.getElementById("login-form");
  if (loginForm) {
    loginForm.addEventListener("submit", async (event) => {
      event.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;

      try {
        await loginUser(email, password);
      } catch (error) {
        console.log("error:" + error);
      }
    });
  }

});

// Ftech detailed place if token and place id identified
const token = getCookie("token");
const urlParams = new URLSearchParams(window.location.search);
const placeId = urlParams.get("id");
try {
  if (token && placeId) {
    fetchDetailedPlace(token, placeId);
  }
} catch (error) {
  console.error(error);
}


/** Login User */
async function loginUser(email, password) {
  const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (response.ok) {
    const data = await response.json();
    document.cookie = `token=${data.access_token}; path=/`;
    window.location.href = "index.html";
    console.log(`${data.access_token}`);
  } else {
    alert("Login failed: " + response.statusText);
  }
}

/** Places fetch and display */
async function fetchPlaces(token) {
  try {
    const response = await fetch("http://127.0.0.1:5000/api/v1/places/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const places = await response.json();
    displayPlaces(places);
  } catch (error) {
    console.error("Error fetching places:", error);
  }
}


function displayPlaces(places) {
  const placesList = document.getElementById("places-list");
  if (!placesList)
    return;
  placesList.innerHTML = "";
  
  places.forEach((place) => {
    const placeCard = document.createElement("div");
    placeCard.className = "place-card";
    placeCard.innerHTML = `
      <div class="place-card-content">
         <p class="title"><u>${place.title}</u>&nbsp;<a href="place.html?id=${place.id}">Détail</a></p>
        <p class="description">${place.description}</p>
        <p class="price-card"><strong>${place.price} €</strong> per night</p>
      </div>
    `;
    placesList.appendChild(placeCard);
  });
  applyPriceFilter('All');
}

function applyPriceFilter(filterprice) {
  console.log('prix:' + filterprice);
  const priceOptions = document.querySelectorAll(".price-option");
  const places = document.querySelectorAll(".place-card");


  const selectedPrice = filterprice;

  places.forEach((card) => {
    const price = parseInt(
      card
        .querySelector(".price-card strong")
        .textContent.replace(" €", ""),
      10
    );
    if (selectedPrice === "All" || price <= parseInt(selectedPrice, 10)) {
      card.style.display = "flex";
    } else {
      card.style.display = "none";
    }
  });

}

/** Place Details Fetch and Display */
async function fetchDetailedPlace(token, placeId) {
  try {
    const response = await fetch(
      `http://127.0.0.1:5000/api/v1/places/${placeId}`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    if (response.ok) {
      const detailedPlace = await response.json();
      displayDetailedPlaces(detailedPlace);
    } else {
      console.error("Failed to fetch detailed place.");
    }
  } catch (error) {
    console.error("Error fetching place detail:", error);
  }
}

/** Usefull functions */
function getPlaceIdFromURL() {
  const url = new URLSearchParams(window.location.search);
  return url.get("id");
}

// Get review text and rating from form and submit it
document.addEventListener("DOMContentLoaded", () => {
  const reviewForm = document.getElementById("review-form");
  const token = getCookie("token");
  const placeId = getPlaceIdFromURL();

  if (reviewForm) {
    reviewForm.addEventListener("submit", async (event) => {
      event.preventDefault();

      const text = document.getElementById("review").value;
      const rating = document.getElementById("rating").value;

      try {
        if (text && rating) {
          submitReview(token, placeId, text, rating);
        }
      } catch (error) {
        console.error(error);
      }
    });
  }
});

/** Review Submit */
async function submitReview(token, placeId, reviewText, rating) {
  try {
    const body = {
      text: reviewText,
      rating: parseInt(rating, 10),
      place_id: placeId,
    };
    console.log("Request body:", body);
    console.log(token);

    const response = await fetch(`http://127.0.0.1:5000/api/v1/reviews/`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    handleResponse(response, placeId);
  } catch (error) {
    console.error("Error:", error);
  }
}

function handleResponse(response, placeId) {
  if (response.ok) {
    alert("Review submitted successfully!");
    window.location.href = `place.html?id=${placeId}`;
    document.getElementById("review-form").reset();
  } else {
    alert("Failed to submit review");
  }
}

function displayDetailedPlaces(place) {
  document.getElementById("place-details").innerHTML = `
        <h1 class="detailedTitle">${place.title}</h1>
        <p class="detailedDescription">${place.description}</p>
        <p class="amenities">What this place offers: 

        </p>
    `;

  const reviewsPlace = document.getElementById("reviews");

  if (place.reviews && place.reviews.length > 0) {
    place.reviews.forEach((review) => {
      const reviewCard = document.createElement("div");
      reviewCard.classList.add("review-card");
      reviewCard.innerHTML = `
                <p>${review.text}</p>
                <p><strong>Rating: ${review.rating}/5</strong></p>
            `;
      reviewsPlace.appendChild(reviewCard);
    });
  } else {
    reviewsPlace.innerHTML += "<p>No reviews available for this place.</p>";
  }
  //initializeCarousel();
}

function deleteTokenCookie() {
  document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/";
}