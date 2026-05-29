function BudgetCard({ budget }) {

  return (

    <div className="card">

      <h2>
        Budget Details
      </h2>

      <p>
        Hotel Cost: ₹{budget.hotel}
      </p>

      <p>
        Food Cost: ₹{budget.food}
      </p>

      <p>
        Transport Cost: ₹{budget.transport}
      </p>

      <h3>
        Total Cost: ₹{budget.total}
      </h3>

    </div>
  );
}

export default BudgetCard;