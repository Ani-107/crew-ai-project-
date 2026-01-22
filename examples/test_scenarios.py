"""
Test scenarios for the Customer Support AI System
Run different customer support cases to test the multi-agent system
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from customer_support_ai import crew

# Test scenarios
test_cases = [
    {
        "name": "Billing Issue - Double Charge",
        "message": "I was charged twice for my subscription this month. Can you fix it?"
    },
    {
        "name": "Technical Support - Login Problem",
        "message": "I can't log into my account. It keeps saying my password is incorrect but I'm sure it's right."
    },
    {
        "name": "Account Management - Cancellation",
        "message": "I want to cancel my subscription. How do I do that?"
    },
    {
        "name": "Product Inquiry - Feature Request",
        "message": "Does your service support integration with Slack? I need this for my team."
    },
    {
        "name": "Refund Request",
        "message": "I'm not satisfied with the service. Can I get a refund for this month?"
    }
]

def run_test_scenario(scenario):
    """Run a single test scenario"""
    print("\n" + "=" * 80)
    print(f"TEST SCENARIO: {scenario['name']}")
    print("=" * 80)
    print(f"Customer Message: {scenario['message']}")
    print("-" * 80)
    
    inputs = {"customer_message": scenario['message']}
    
    try:
        result = crew.kickoff(inputs=inputs)
        print("\n" + "-" * 80)
        print("RESULT:")
        print("-" * 80)
        print(result)
        print("\n✅ Scenario completed successfully")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
    
    print("=" * 80)

def main():
    """Run all test scenarios"""
    print("\n" + "🤖 " * 20)
    print("CUSTOMER SUPPORT AI - TEST SCENARIOS")
    print("🤖 " * 20)
    
    # Option to run all or select specific scenarios
    print("\nAvailable test scenarios:")
    for i, scenario in enumerate(test_cases, 1):
        print(f"{i}. {scenario['name']}")
    
    print("\nOptions:")
    print("- Press Enter to run ALL scenarios")
    print("- Enter a number (1-5) to run a specific scenario")
    print("- Enter 'q' to quit")
    
    choice = input("\nYour choice: ").strip()
    
    if choice.lower() == 'q':
        print("Exiting...")
        return
    
    if choice == "":
        # Run all scenarios
        for scenario in test_cases:
            run_test_scenario(scenario)
            input("\nPress Enter to continue to next scenario...")
    else:
        # Run specific scenario
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(test_cases):
                run_test_scenario(test_cases[idx])
            else:
                print("Invalid scenario number!")
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    main()
