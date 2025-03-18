document
  .getElementById("predictionForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    let glucose = parseFloat(document.getElementById("glucose").value);
    let bmi = parseFloat(document.getElementById("bmi").value);

    fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features: [glucose, bmi] }),
    })
      .then((response) => response.json())
      .then(
        (data) =>
          (document.getElementById("result").innerText =
            "Prediction: " + (data.prediction === 1 ? "High Risk" : "Low Risk"))
      )
      .catch((error) => console.error("Error:", error));
  });
