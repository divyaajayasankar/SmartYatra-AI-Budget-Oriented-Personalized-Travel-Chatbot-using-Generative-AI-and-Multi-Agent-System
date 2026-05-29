import React, { useState } from "react";

function ChatBox() {

  const [destination, setDestination] = useState("");

  const [result, setResult] = useState({
    ai_response: "",

    budget: {
      hotel: 0,
      food: 0,
      transport: 0,
      misc: 0,
      total: 0
    },

    recommendations: [],

    safety: {
      women_safety: "",
      child_friendly: "",
      night_risk: ""
    },

    itinerary: []
  });

  const sendQuery = async () => {

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/travel",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            city: destination,
            budget: 50000,
            days: 3,
            food_preference: "Veg"
          })
        }
      );

      const data = await response.json();

      console.log(data);

      setResult({
        ai_response: data.ai_response || "No response",

        budget: data.budget || {
          hotel: 0,
          food: 0,
          transport: 0,
          misc: 0,
          total: 0
        },

        recommendations: data.recommendations || [],

        safety: data.safety || {
          women_safety: "Unknown",
          child_friendly: "Unknown",
          night_risk: "Unknown"
        },

        itinerary: data.itinerary || []
      });

    } catch (error) {

      console.error(error);

      setResult({
        ai_response: "Backend connection failed",

        budget: {
          hotel: 0,
          food: 0,
          transport: 0,
          misc: 0,
          total: 0
        },

        recommendations: [],

        safety: {
          women_safety: "Unknown",
          child_friendly: "Unknown",
          night_risk: "Unknown"
        },

        itinerary: []
      });
    }
  };

  return (

    <div
      style={{
        padding: "30px",
        fontFamily: "Arial",
        maxWidth: "900px",
        margin: "auto"
      }}
    >

      <h1>🇮🇳 India AI Travel Planner</h1>

      <p>
        Plan your budget-friendly India trip with AI recommendations,
        nearby places, safety analysis and smart itinerary planning.
      </p>

      <input
        type="text"
        placeholder="Enter destination"
        value={destination}
        onChange={(e) => setDestination(e.target.value)}
        style={{
          padding: "12px",
          width: "300px",
          marginRight: "10px",
          fontSize: "16px"
        }}
      />

      <button
        onClick={sendQuery}
        style={{
          padding: "12px 20px",
          cursor: "pointer",
          backgroundColor: "#ff9933",
          color: "white",
          border: "none",
          fontSize: "16px"
        }}
      >
        Plan Trip
      </button>

      <div style={{ marginTop: "30px" }}>

        <h2>🤖 AI Response</h2>

        <p>{result.ai_response}</p>

        <h2>💰 Budget Details</h2>

        <p>🏨 Hotel Cost: ₹{result.budget.hotel}</p>

        <p>🍛 Food Cost: ₹{result.budget.food}</p>

        <p>🚌 Transport Cost: ₹{result.budget.transport}</p>

        <p>📦 Misc Cost: ₹{result.budget.misc}</p>

        <h3>Total Budget: ₹{result.budget.total}</h3>

        <h2>📍 Nearby Recommended Places</h2>

        {
          result.recommendations.length > 0 ? (

            <ul>
              {
                result.recommendations.map((place, index) => (
                  <li key={index}>{place}</li>
                ))
              }
            </ul>

          ) : (

            <p>No places found</p>

          )
        }

        <h2>🛡 Safety Information</h2>

        <p>
          <strong>Women Safety:</strong>{" "}
          {result.safety.women_safety}
        </p>

        <p>
          <strong>Child Friendly:</strong>{" "}
          {result.safety.child_friendly}
        </p>

        <p>
          <strong>Night Travel Risk:</strong>{" "}
          {result.safety.night_risk}
        </p>

        <h2>🗓 Trip Itinerary</h2>

        {
          result.itinerary.length > 0 ? (

            <ul>
              {
                result.itinerary.map((day, index) => (
                  <li key={index}>{day}</li>
                ))
              }
            </ul>

          ) : (

            <p>No itinerary available</p>

          )
        }

      </div>

    </div>
  );
}

export default ChatBox;