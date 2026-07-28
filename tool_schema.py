calculator_schema = {
    "name": "calculator",
    "description": "Evaluates a mathematical expression.",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "The mathematical expression to evaluate."
            }
        },
        "required": ["expression"]
    }
}