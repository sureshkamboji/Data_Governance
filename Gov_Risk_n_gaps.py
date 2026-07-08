# ============================================================
# TASK 3 — Identify Governance Risks and Gaps
# Run AFTER Task 1 and Task 2
# Run each block as a separate cell
# ============================================================

# ---- STEP 1: Flag overloaded roles ----
OVERLOAD_THRESHOLD = 10  # hours per week

print("=== Overloaded Roles ===")
overloaded = workload[workload['hours_per_week'] > OVERLOAD_THRESHOLD]
if len(overloaded) > 0:
    for role, row in overloaded.iterrows():
        excess = row['hours_per_week'] - OVERLOAD_THRESHOLD
        print(f"  ⚠️  {role}")
        print(f"      {row['hours_per_week']} hrs/week — {excess:.0f} hrs OVER the threshold")
        print(f"      Tasks: {row['total_tasks']}  |  High priority: {row['high_priority']}")
else:
    print("  No roles currently overloaded")


# ---- STEP 2: Find high priority tasks that are still pending ----
print("\n=== HIGH RISK: High Priority Tasks Still Pending ===")
high_pending = df[(df['priority'] == 'High') & (df['status'] == 'Pending')]
if len(high_pending) > 0:
    print(f"  {len(high_pending)} high-priority tasks are NOT active yet:\n")
    for _, row in high_pending.iterrows():
        print(f"  ❌ {row['task']}")
        print(f"     Role: {row['assigned_role']}  |  {row['hours_per_week']} hrs/week needed")
else:
    print("  None — all high priority tasks are active")


# ---- STEP 3: Find stale tasks (not reviewed recently) ----
print("\n=== Stale Tasks (Not Reviewed in Over 6 Months) ===")
stale = df[df['last_reviewed_months_ago'] > 6].sort_values(
    'last_reviewed_months_ago', ascending=False
)
print(f"  {len(stale)} tasks flagged as stale:\n")
for _, row in stale.iterrows():
    print(f"  🕐 {row['task']}")
    print(f"     Role: {row['assigned_role']}  |  Last reviewed: {row['last_reviewed_months_ago']} months ago")


# ---- STEP 4: Find underutilised roles ----
print("\n=== Underutilised Roles (Under 5 hrs/week) ===")
UNDERLOAD_THRESHOLD = 5
underloaded = workload[workload['hours_per_week'] < UNDERLOAD_THRESHOLD]
if len(underloaded) > 0:
    for role, row in underloaded.iterrows():
        spare = UNDERLOAD_THRESHOLD - row['hours_per_week']
        print(f"  📋 {role}: only {row['hours_per_week']} hrs/week — {spare:.0f} hrs of spare capacity")
else:
    print("  No underutilised roles found")


# ---- STEP 5: Risk summary count ----
print("\n=== Risk Summary ===")
print(f"  Overloaded roles:           {len(overloaded)}")
print(f"  High priority pending:      {len(high_pending)}")
print(f"  Stale tasks:                {len(stale)}")
print(f"  Underutilised roles:        {len(underloaded)}")
total_risks = len(overloaded) + len(high_pending) + len(stale) + len(underloaded)
print(f"  Total issues identified:    {total_risks}")
