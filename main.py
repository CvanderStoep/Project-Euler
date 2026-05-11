import matplotlib.pyplot as plt

def fmt_millions(value: int) -> str:
    """Format large integers like 8100000 → '8.1M'."""
    return f"{value/1_000_000:.1f}M"

data = [
    {"name": "Basic", "users": 1800, "cost": 4500},
    {"name": "ERP",   "users": 1800, "cost": 3000},
    {"name": "CAD",   "users": 400,  "cost": 5000},
]

# One color per box
colors = ["tab:blue", "tab:green", "tab:red"]

fig, ax = plt.subplots(figsize=(10, 8))

y_offset = 0
max_users = max(item["users"] for item in data)

for item, color in zip(data, colors):
    width = item["users"]
    height = item["cost"]
    total_cost = item["users"] * item["cost"]
    total_fmt = fmt_millions(total_cost)

    ax.broken_barh(
        [(0, width)],
        (y_offset, height),
        facecolors=color,
        edgecolor="black",
        alpha=0.75
    )

    # Label inside the box: name + formatted total cost
    ax.text(
        width / 2,
        y_offset + height / 2,
        f"{item['name']}\n{total_fmt}",
        ha="center",
        va="center",
        fontsize=14,
        color="white",
        weight="bold"
    )

    y_offset += height

# X‑axis ticks every 500
ax.set_xticks(range(0, max_users + 1, 500))

ax.set_xlabel("Users")
ax.set_ylabel("Cost per user")
ax.set_title("Stacked Cost/User Footprint (Name + Total Cost in Millions)")

plt.tight_layout()
plt.show()
