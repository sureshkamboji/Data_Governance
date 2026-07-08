# ============================================================
# TASK 1 — Load the Governance Task Data and Explore It
# Open a new notebook, run each block as a separate cell
# ============================================================

# ---- STEP 1: Create the dataset ----
import pandas as pd

data = {
    'task_id': list(range(1, 26)),
    'task': [
        'Define Data Policy', 'Approve Data Standards', 'Monitor Data Quality',
        'Manage Data Access Requests', 'Classify Data Assets',
        'Handle Data Incidents', 'Train Business Users', 'Maintain Data Catalog',
        'Run Compliance Audit', 'Report KPIs to Executive',
        'Review Data Sharing Agreements', 'Resolve Data Conflicts',
        'Update Data Dictionary', 'Perform Data Profiling',
        'Approve New Data Sources', 'Manage Metadata', 'Enforce Retention Rules',
        'Conduct Stakeholder Interviews', 'Document Data Lineage',
        'Review Third Party Data Contracts', 'Define Data Glossary',
        'Assess Data Risks', 'Manage Master Data', 'Review AI Data Usage',
        'Publish Governance Newsletter'
    ],
    'assigned_role': [
        'CDO', 'Data Owner', 'Data Steward', 'Data Custodian', 'Data Steward',
        'Data Steward', 'Data Steward', 'Data Steward', 'CDO', 'CDO',
        'Data Owner', 'Data Steward', 'Data Steward', 'Data Analyst',
        'Data Owner', 'Data Custodian', 'Data Custodian', 'Data Steward',
        'Data Analyst', 'CDO', 'Data Steward', 'CDO', 'Data Owner',
        'CDO', 'Data Steward'
    ],
    'department': [
        'Executive','Finance','HR','IT','HR',
        'IT','HR','IT','Executive','Executive',
        'Finance','HR','IT','IT','Finance',
        'IT','IT','HR','IT','Executive',
        'IT','Executive','Finance','Executive','HR'
    ],
    'priority': [
        'High','High','High','Medium','High',
        'High','Medium','Medium','High','High',
        'Medium','High','Low','Medium','High',
        'Low','High','Medium','Medium','High',
        'Low','High','Medium','High','Low'
    ],
    'hours_per_week': [
        3,2,4,3,2,5,3,4,2,2,
        2,3,2,3,1,2,3,4,3,2,
        2,3,2,4,1
    ],
    'status': [
        'Active','Active','Active','Active','Active',
        'Active','Active','Active','Active','Active',
        'Pending','Active','Pending','Active','Active',
        'Pending','Active','Active','Active','Pending',
        'Active','Active','Pending','Active','Pending'
    ],
    'last_reviewed_months_ago': [
        1,3,1,6,2,1,4,2,1,1,
        8,2,12,3,5,10,2,3,4,2,
        7,1,9,1,15
    ]
}

df = pd.DataFrame(data)
df.to_csv('governance_tasks.csv', index=False)
print(f"Dataset created: {df.shape[0]} tasks, {df.shape[1]} columns")
print(df.head(10))


# ---- STEP 2: Basic overview ----
print("\n=== Dataset Overview ===")
print(f"Total tasks:      {len(df)}")
print(f"Unique roles:     {df['assigned_role'].nunique()}")
print(f"Departments:      {df['department'].nunique()}")
print(f"Active tasks:     {(df['status']=='Active').sum()}")
print(f"Pending tasks:    {(df['status']=='Pending').sum()}")
print(f"Total hrs/week:   {df['hours_per_week'].sum()}")


# ---- STEP 3: Data types and missing values ----
print("\n=== Data Info ===")
df.info()

print("\n=== Missing Values per Column ===")
print(df.isnull().sum())

print("\n=== Priority Breakdown ===")
print(df['priority'].value_counts())

print("\n=== Status Breakdown ===")
print(df['status'].value_counts())


# ---- STEP 4: Tasks per role (text bar chart) ----
print("\n=== Tasks Assigned per Role ===")
role_counts = df['assigned_role'].value_counts()
for role, count in role_counts.items():
    bar = '█' * count
    print(f"  {role:22s} {bar} ({count} tasks)")
