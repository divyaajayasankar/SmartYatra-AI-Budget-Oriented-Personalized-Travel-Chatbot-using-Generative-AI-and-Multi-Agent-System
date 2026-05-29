function Recommendations({ places }) {

  return (

    <div className="card">

      <h2>Recommended Places</h2>

      {places.map((place, index) => (

        <div key={index} className="item">

          <h3>{place.name}</h3>

          <p>City: {place.city}</p>

          <p>State: {place.state}</p>

          <p>Type: {place.type}</p>

          <p>Total Budget: ₹{place.budget}</p>

          <p>Safety Score: {place.safety}</p>

          <hr />

          <p>🚆 Railway Station Distance: {place.railway_distance} km</p>

          <p>🚌 Bus Stand Distance: {place.bus_distance} km</p>

          <p>✈ Airport Distance: {place.airport_distance} km</p>

        </div>
      ))}

    </div>
  );
}

export default Recommendations;