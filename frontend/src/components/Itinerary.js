function Itinerary({ itinerary }) {

  return (

    <div className="card">

      <h2>
        Trip Itinerary
      </h2>

      {itinerary.map((day, index) => (

        <p key={index}>
          {day}
        </p>

      ))}

    </div>
  );
}

export default Itinerary;