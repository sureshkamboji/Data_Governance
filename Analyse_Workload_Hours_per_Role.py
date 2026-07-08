# ============================================================
# TASK 2 — Analyse Workload and Hours per Role
# Run AFTER Task 1 (df must already exist in your notebook)
# Run each block as a separate cell
# ============================================================

# ---- STEP 1: Full workload summary per role ----
workload = df.groupby('assigned_role').agg(
    total_tasks      = ('task_id',        'count'),
    active_tasks     = ('status',         lambda x: (x=='Active').sum()),
    pending_tasks    = ('status',         lambda x: (x=='Pending').sum()),
    hours_per_week   = ('hours_per_week', 'sum'),
    high_priority    = ('priority',       lambda x: (x=='High').sum()),
    avg_hrs_per_task = ('hours_per_week', 'mean')
).sort_values('hours_per_week', ascending=False).round(1)

print("=== Full Workload Summary by Role ===")
print(workload.to_string())


# ---- STEP 2: Text bar chart of hours per role ----
print("\n=== Hours per Week by Role ===")
max_hrs = workload['hours_per_week'].max()
for role, row in workload.iterrows():
    filled = int((row['hours_per_week'] / max_hrs) * 20)
    bar    = '█' * filled + '░' * (20 - filled)
    flag   = '  ⚠️  OVERLOADED' if row['hours_per_week'] > 10 else ''
    print(f"  {role:22s} {bar} {row['hours_per_week']:.0f} hrs{flag}")


# ---- STEP 3: High priority task load per role ----
print("\n=== High Priority Tasks per Role ===")
high_p = df[df['priority'] == 'High'].groupby('assigned_role').agg(
    high_priority_tasks = ('task_id',        'count'),
    high_priority_hours = ('hours_per_week', 'sum')
).sort_values('high_priority_hours', ascending=False)

print(high_p.to_string())
print(f"\nTotal high priority hours committed per week: {high_p['high_priority_hours'].sum()}")


# ---- STEP 4: Department workload breakdown ----
print("\n=== Hours per Week by Department ===")
dept = df.groupby('department').agg(
    tasks        = ('task_id',        'count'),
    total_hours  = ('hours_per_week', 'sum'),
    high_p_tasks = ('priority',       lambda x: (x=='High').sum())
).sort_values('total_hours', ascending=False)

print(dept.to_string())


# ---- STEP 5: Which role owns the most high-priority work? ----
print("\n=== Top 3 Most Burdened Roles ===")
top3 = workload.nlargest(3, 'hours_per_week')
for i, (role, row) in enumerate(top3.iterrows(), 1):
    print(f"  {i}. {role}")
    print(f"     Tasks: {row['total_tasks']}  |  Hours/week: {row['hours_per_week']}  |  High priority: {row['high_priority']}")
