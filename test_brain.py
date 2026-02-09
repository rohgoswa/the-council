from agents import app

# The Test Decision
decision = "We should replace 50% of our customer support staff with AI chatbots to save money."

print(f"🤖 Testing The Council on: {decision}\n")

# Run the Graph
result = app.invoke({"topic": decision})

print("\n--- 💰 CFO SAYS ---")
print(result['cfo_opinion'])

print("\n--- 🤝 UNION SAYS ---")
print(result['union_opinion'])

print("\n--- 🚀 VISIONARY SAYS ---")
print(result['visionary_opinion'])