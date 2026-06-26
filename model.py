import gurobipy as gp

# Gurobi model
model = gp.Model()

bonds = ["Bond A", "Bond B", "Bond C", "Bond D"]

# variables
x = model.addVars(bonds, name="x", lb=0)

# constraints
# Period 1
model.addConstr(6*x["Bond A"] + 4*x["Bond B"] + 100*x["Bond C"] + 50*x["Bond D"] >= 1200000, name="t1")
# Period 2
model.addConstr(6*x["Bond A"] + 104*x["Bond B"] + 50*x["Bond D"] >= 1000000, name="t2")
# Period 3
model.addConstr(106*x["Bond A"] >= 800000, name="t3")

# objective function
model.setObjective(gp.quicksum([105.8 * x["Bond A"], 100.5 * x["Bond B"], 96.48 * x["Bond C"], 94.62 * x["Bond D"]]), gp.GRB.MINIMIZE)

# Solve it
model.optimize()

# show results
if model.status == gp.GRB.OPTIMAL:
    print("Optimal solution found:")
    for bond in bonds:
        print(f"{bond}: ${x[bond].x:.2f}")
    print(f"Objective value: {model.objVal:.2f}")