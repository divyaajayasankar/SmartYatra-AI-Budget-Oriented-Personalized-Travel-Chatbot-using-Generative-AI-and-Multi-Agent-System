function SafetyCard({ safety }) {

  return (

    <div className="card">

      <h2>
        Safety Information
      </h2>

      <p>
        Women Safety:
        {safety.women_safety}
      </p>

      <p>
        Child Friendly:
        {safety.child_friendly}
      </p>

      <p>
        Night Travel Risk:
        {safety.night_travel_risk}
      </p>

    </div>
  );
}

export default SafetyCard;