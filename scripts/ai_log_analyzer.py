import os
import sys
from openai import OpenAI

def main():
    log_file = "failure.log"

    if not os.path.exists(log_file):
        print("No failure.log file found.")
        sys.exit(0)

    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        logs = f.read()

    # Keep the payload small and safer for a demo project
    logs = logs[:4000]

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    prompt = f"""
You are a DevOps CI/CD troubleshooting assistant.

Analyze the following GitHub Actions pipeline failure log and return:
1. What failed
2. Why it likely failed
3. The most likely fix
4. A short plain-English explanation for a beginner

Failure log:
{logs}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print("\n=== AI Failure Analysis ===\n")
    print(response.output_text)

if __name__ == "__main__":
    main()