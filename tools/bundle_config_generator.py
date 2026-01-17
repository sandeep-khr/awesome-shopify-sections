import json

# ==========================================
# BUNDLE CONFIGURATION
# Edit this dictionary to configure your bundle
# ==========================================
BUNDLE_CONFIG = {
    "bundle_name": "Summer Essentials Kit",
    "discount_tiers": [
        {"quantity": 2, "discount_percentage": 10},
        {"quantity": 3, "discount_percentage": 15},
        {"quantity": 4, "discount_percentage": 20}
    ],
    "steps": [
        {
            "step_id": 1,
            "title": "Choose your Bottle",
            "required_quantity": 1,
            "allow_multiple": False,
            "items": [
                {"id": 4455667788, "name": "Matte Black Bottle", "image": "bottle-black.jpg", "price": 2500},
                {"id": 4455667789, "name": "Ocean Blue Bottle", "image": "bottle-blue.jpg", "price": 2500}
            ]
        },
        {
            "step_id": 2,
            "title": "Pick a Notebook",
            "required_quantity": 1,
            "allow_multiple": True,
            "items": [
                {"id": 5566778899, "name": "Hardcover Dot Grid", "image": "notebook-dot.jpg", "price": 1500},
                {"id": 5566778800, "name": "Softcover Lined", "image": "notebook-lined.jpg", "price": 1200}
            ]
        },
        {
            "step_id": 3,
            "title": "Add Accessories (Optional)",
            "required_quantity": 0,
            "allow_multiple": True,
            "items": [
                {"id": 6677889900, "name": "Canvas Tote Bag", "image": "tote.jpg", "price": 800},
                {"id": 6677889911, "name": "sticker Pack", "image": "stickers.jpg", "price": 500}
            ]
        }
    ]
}

# ==========================================
# GENERATOR LOGIC
# Do not edit below this line
# ==========================================

def validate_config(config):
    print("Validating configuration...")
    if not config.get("steps"):
        raise ValueError("Configuration must have at least one step.")
    
    for step in config["steps"]:
        if "step_id" not in step or "items" not in step:
            raise ValueError(f"Step {step} is missing required fields.")
            
    print("Configuration is valid!")

def generate_json_string(config):
    # We minify the JSON to save space in the Shopify setting
    return json.dumps(config, separators=(',', ':'))

if __name__ == "__main__":
    try:
        validate_config(BUNDLE_CONFIG)
        json_output = generate_json_string(BUNDLE_CONFIG)
        
        print("\n" + "="*50)
        print("GENERATED CONFIGURATION STRING")
        print("Copy the line below and paste it into the 'Bundle Config JSON' setting in Shopify:")
        print("="*50 + "\n")
        print(json_output)
        print("\n" + "="*50)
        
        # Optionally write to a file
        with open("bundle_config.json", "w") as f:
            f.write(json.dumps(BUNDLE_CONFIG, indent=2))
            print("Also saved readable version to 'bundle_config.json' for reference.")
            
    except Exception as e:
        print(f"Error: {e}")
