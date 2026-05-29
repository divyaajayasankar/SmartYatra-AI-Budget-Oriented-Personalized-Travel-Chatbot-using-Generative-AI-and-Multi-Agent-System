import React, { useState } from "react";
import "./App.css";
import MapComponent from "./components/MapComponent";

function App() {

  const [destination, setDestination] = useState("");
  const [budget, setBudget] = useState(50000);
  const [days, setDays] = useState(3);
  const [travelers, setTravelers] = useState(1);

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const sendQuery = async () => {

    setLoading(true);

    try {

      const response = await fetch("http://127.0.0.1:8000/travel", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          city: destination,
          budget: Number(budget),
          days: Number(days),
          food_preference: "all"
        })
      });

      const data = await response.json();

      setResult(data);

    } catch (error) {

      console.log(error);
      alert("Backend connection failed");

    }

    setLoading(false);
  };

  return (

    <div className="main-container">

      <div className="overlay">

        <div className="hero-section">

          <h1>🇮🇳 India AI Travel Planner</h1>

          <p>
            Smart AI-powered budget travel assistant for discovering
            beautiful places across India ✈️
          </p>

        </div>

        <div className="search-card">

          <input
            type="text"
            placeholder="🌍 Enter Destination"
            value={destination}
            onChange={(e) => setDestination(e.target.value)}
          />

          <div className="input-grid">

            <input
              type="number"
              placeholder="💰 Budget"
              value={budget}
              onChange={(e) => setBudget(e.target.value)}
            />

            <input
              type="number"
              placeholder="📅 Days"
              value={days}
              onChange={(e) => setDays(e.target.value)}
            />

            <input
              type="number"
              placeholder="👨‍👩‍👧 Travelers"
              value={travelers}
              onChange={(e) => setTravelers(e.target.value)}
            />

          </div>

          <button onClick={sendQuery}>
            ✨ Plan My Trip
          </button>

        </div>

        {loading && (

          <div className="loading">
            Generating your AI travel plan...
          </div>

        )}

        {result && (

          <div className="results-container">

            <div className="card">

              <h2>🤖 AI Response</h2>

              <p>{result.ai_response}</p>

            </div>

            <div className="budget-grid">

              <div className="budget-card">
                <h3>🏨 Hotel</h3>
                <p>₹{result.budget?.hotel}</p>
              </div>

              <div className="budget-card">
                <h3>🍛 Food</h3>
                <p>₹{result.budget?.food}</p>
              </div>

              <div className="budget-card">
                <h3>🚌 Transport</h3>
                <p>₹{result.budget?.transport}</p>
              </div>

              <div className="budget-card">
                <h3>📦 Misc</h3>
                <p>₹{result.budget?.misc}</p>
              </div>

            </div>

            <div className="total-budget">
              Total Budget: ₹{result.budget?.total}
            </div>

            <div className="card">

              <h2>📍 Recommended Places</h2>

              <div className="places-grid">

                {result.recommendations?.map((place, index) => (

                  <div className="place-card" key={index}>
                    <div className="place-name">🌴 {place.name}</div>
                    <div className="place-type">{place.type}</div>
                    <div className="place-details">
                      <div className="good-bad">
                        <span className="good">✅ {place.good_places?.[0]}</span>
                        <span className="bad">⚠️ {place.bad_places?.[0]}</span>
                      </div>
                    </div>
                    <div className="place-hotel">
                      🏨 {place.hotel_name} - ₹{place.hotel_price}
                    </div>
                  </div>

                ))}

              </div>

            </div>

            <div className="card">

              <h2>🗺️ Interactive Map</h2>

              <MapComponent places={result.recommendations} />

            </div>

            <div className="card">

              <h2>🛡 Safety Information</h2>

              <div className="safety-grid">

                <div className="safe-box">
                  👩 Women Safety
                  <span>{result.safety?.women_safety}</span>
                </div>

                <div className="safe-box">
                  👨‍👩‍👧 Child Friendly
                  <span>{result.safety?.child_friendly}</span>
                </div>

                <div className="safe-box">
                  🌙 Night Travel
                  <span>{result.safety?.night_risk}</span>
                </div>

              </div>

            </div>

            <div className="card">

              <h2>🗓 Trip Itinerary</h2>

              <div className="timeline">

                {result.itinerary?.map((day, index) => (

                  <div className="timeline-item" key={index}>

                    <div className="circle">
                      {index + 1}
                    </div>

                    <div className="timeline-content">
                      {day}
                    </div>

                  </div>

                ))}

              </div>

            </div>

          </div>

        )}

      </div>

    </div>

  );
}

export default App;