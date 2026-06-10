def handler(input):
    chat = input.get("chat_history", "")

    # Basic risk logic (demo version)
    if "3 lần" in chat or "complain" in chat or "quá tệ" in chat:
        risk = "CRITICAL"
    elif "lâu vậy" in chat or "chờ" in chat:
        risk = "HIGH"
    else:
        risk = "LOW"

    return {
        "risk_level": risk,
        "reason": "Detected keywords indicating customer frustration",
        "suggested_action": "Apologize and provide clear resolution timeline"
    }
