function toggleAdvancedSearch() {
  const advancedSearch = document.getElementById("advanced-search");
  const toggleButton = document.getElementById("toggle-advanced-search");

  // Toggle visibility of advanced filters
  if (advancedSearch.style.display === "none") {
    advancedSearch.style.display = "flex";
    toggleButton.innerText = "Basic Search";
  } else {
    advancedSearch.style.display = "none";
    toggleButton.innerText = "Advanced Search";
  }
}

function searchHospitals() {
  // Get search values
  const searchQuery = document.getElementById("search").value.toLowerCase();
  const hospitalFilter = document
    .getElementById("hospital")
    ?.value.toLowerCase();
  const locationFilter = document
    .getElementById("location")
    ?.value.toLowerCase();
  const availabilityFilter = document
    .getElementById("availability")
    ?.value.toLowerCase();

  // Get all doctor cards
  const doctorCards = document.querySelectorAll(".doctor-card");

  doctorCards.forEach((doctorCard) => {
    const doctorName = doctorCard.querySelector("h2").innerText.toLowerCase();
    const doctorSpecialties = doctorCard
      .querySelector(".box-style p")
      ?.innerText.toLowerCase();
    const hospitalName = doctorCard
      .querySelector(".availability strong")
      ?.innerText.toLowerCase();
    const doctorLocation = doctorCard
      .querySelector("p:last-child")
      ?.innerText.toLowerCase();
    const doctorAvailability = doctorCard
      .querySelector(".availability")
      .innerText.toLowerCase();

    // Check search query match (name or specialties)
    const matchesSearchQuery =
      !searchQuery ||
      doctorName.includes(searchQuery) ||
      (doctorSpecialties && doctorSpecialties.includes(searchQuery));

    // Check hospital filter match
    const matchesHospitalFilter =
      !hospitalFilter ||
      (hospitalName && hospitalName.includes(hospitalFilter));

    // Check location filter match
    const matchesLocationFilter =
      !locationFilter ||
      (doctorLocation && doctorLocation.includes(locationFilter));

    // Check availability filter match
    const matchesAvailabilityFilter =
      !availabilityFilter ||
      (doctorAvailability && doctorAvailability.includes(availabilityFilter));

    // Show or hide card based on filters
    const matchesAll =
      matchesSearchQuery &&
      matchesHospitalFilter &&
      matchesLocationFilter &&
      matchesAvailabilityFilter;

    doctorCard.style.display = matchesAll ? "block" : "none";
  });
}
