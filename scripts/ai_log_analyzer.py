try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print("\n=== AI Failure Analysis ===\n")
    print(response.output_text)

except Exception as e:
    print("\n=== AI Analysis Failed ===\n")
    print("Could not reach AI service. Possible reasons:")
    print("- API quota exceeded")
    print("- Network issue")
    print("- Invalid API key")
    print("\nFallback suggestion:")
    print("Check test logs above. Likely assertion or import error.")